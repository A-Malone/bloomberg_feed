from twython import TwythonStreamer

class MyStreamer (TwythonStreamer):
	def on_success(self,data):
		if 'text' in data:
			print data['text'].encode('utf-8') #Should add the item to the database if its different enough or newer
			#Difference processing: http://www.nltk.org/howto/wordnet.html
	def on_error(self,status_code,data):
		print status_code

APP_KEY = 'LLMtc9HXCYl7Bh65f3R90QHpc'
APP_SECRET = 'IeJ4gp2dSz7Gf1TAb4y5IfuIpodydYXLh28KsATuDFo60hnBfh'
OAUTH_TOKEN = '1599600042-PjahYW0zM3dvp8gGWMKOhVBANEDt0XxuT5TwAwO'
OAUTH_TOKEN_SECRET = 'leQ6kmtD46WbvIVClm16Mo3BnW8BRKWVOt0MyHVUbKJI9'

stream = MyStreamer (APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
stream.statuses.filter(track='#yolo') #Streams all items that contain #yolo