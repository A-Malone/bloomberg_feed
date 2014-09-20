from twython import Twython

APP_KEY = 'LLMtc9HXCYl7Bh65f3R90QHpc'
ACCESS_TOKEN ='AAAAAAAAAAAAAAAAAAAAAGN3aQAAAAAAhapChctFWnFZAJCbHztynwjBFvw%3DTd24FR9IdmDJMZH7QwKH2LiHXY5HP38bLSbbqrTfiD3SgV3PS0'
twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

search_terms = ["MSFT", "Microsoft","Bill Gates", "Windows", "xbox", "azure", "cortana"]

query  = " OR ".join(search_terms)
print query
tweets = twitter.search(q=query, since="2014-09-18", until="2014-09-19")#Retrieve all of thursday's tweets
for tweet in tweets['statuses']:
	print tweet['text'].encode('utf-8')