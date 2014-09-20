from django.http import HttpResponse

def start(request):
	return HttpResponse("Hello World, This is the Bloomberg app for Hack The North. Please enter a company")
def home(request,company_tag):
	#Connect to bloomberg API with company tag
	#Parse Data from twitter
	#AJAX? How to implement that? Separate view?
	return HttpResponse ("Hello! This page will be used to display the graphs about %s" % company_tag)

