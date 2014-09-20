from django.http import HttpResponse
#used for json returns
import json


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

	#temporary Test Data:
	response_array = []
	response_data = {}
	response_data['value'] = 'THE VALUE OF THE THING'
	response_data['time'] = "THE TIME OF THE THING"
	response_array.append(response_data)
	response_array.append(response_data)
	response_array.append(response_data)
	return HttpResponse(json.dumps(response_array), content_type="application/json")
