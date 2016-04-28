from github import Github
import redis

serverRedis = redis.Redis("localhost")
pullRequests= []
githubAccount=Github("09124264d954adbb6462fa0fe8ae2399ddd9cca7")
#repositories = list(g.get_repos())
for repositorie in githubAccount.get_user().get_repos():
    for pull in repositorie.get_pulls(): 
    		if(pull.state == "open"):
    			pullRequests.append(pull)
    			serverRedis.sadd("Pull_Request","title:"+pull.title+",state:"+pull.state+",created_at:"+pull.created_at.strftime("%m/%d/%Y")+",repositorie:"+repositorie.name+",User:"+pull.user.name)			
print serverRedis.smembers("Pull_Request")	
	