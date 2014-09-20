from django.http import HttpResponse
#used for json returns
import json
import datetime

import blpapi

#A helper function
def getPreviousTradingDate():
    tradedOn = datetime.date.today()

    while True:
        try:
            tradedOn -= datetime.timedelta(days=1)
        except OverflowError:
            return None

        if tradedOn.weekday() not in [5, 6]:
            return tradedOn


def start(request):
    return HttpResponse("Hello World, This is the Bloomberg app for Hack The North. Please enter a company")

def home(request,company_tag):
    #Connect to bloomberg API with company tag
    #Parse Data from twitter
    #AJAX? How to implement that? Separate view?
    return HttpResponse ("Hello! This page will be used to display the graphs about %s" % company_tag)

def getJSON(request, company_tag,last_call):
    #Data should be newer than last_call
    #Send the company_tag to bloomberg api
    #return json response

    sessionOptions = blpapi.SessionOptions()
    sessionOptions.setServerHost("10.8.8.1")
    sessionOptions.setServerPort(8194)

    print "Connecting to %s:%d" % ("10.8.8.1", 8194)

    # Create a Session
    session = blpapi.Session(sessionOptions)

    # Start a Session
    if not session.start():
        print "Failed to start session."
        return
    if not session.openService("//blp/refdata"):
        print "Failed to open //blp/refdata"
        return

    tradedOn = getPreviousTradingDate()
    if not tradedOn:
        print "unable to get previous trading date"
        return

    startTime = datetime.datetime.combine(tradedOn, datetime.time(13, 30))
    endTime = datetime.datetime.combine(tradedOn, datetime.time(20, 30))

    refDataService = session.getService("//blp/refdata")
    request = refDataService.createRequest("IntradayBarRequest")
    request.set("security", "AAPL US Equity")
    request.set("eventType", "TRADE");    
    request.set("interval", 5);    
    request.set("startDateTime", startTime)    
    request.set("endDateTime", endTime)


    print "Sending Request:", request
    session.sendRequest(request)

    #The response string for the JSON objects
    response_string = ""

    try:
        # Process received events
        while(True):
            # We provide timeout to give the chance to Ctrl+C handling:
            ev = session.nextEvent(500)
            for msg in ev:
                response_string += str(msg)
            #for msg in ev:
            #    print msg
            # Response completly received, so we could exit
            if ev.eventType() == blpapi.Event.RESPONSE:
                break
    finally:
        # Stop the session
        session.stop()

    #temporary Test Data:
    #response_array = []
    #response_data = {}
    #response_data['value'] = 'THE VALUE OF THE THING'
    #response_data['time'] = "THE TIME OF THE THING"
    #response_array.append(response_data)
    #response_array.append(response_data)
    #response_array.append(response_data)


    return HttpResponse(response_string, content_type="application/json")
