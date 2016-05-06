import redis
serverRedis = redis.Redis("localhost")
splitStringRequest=[]
splitStringData=[]
listOfRows=[]
rows={}
for pull_Request in serverRedis.smembers("Pull_Request"):
	splitString=pull_Request.split(",")
	for teste in splitString:
		splitStringData=teste.split(":")
		rows[splitStringData[0]]=splitStringData[1]
print rows
#print serverRedis.smembers("Pull_Request")