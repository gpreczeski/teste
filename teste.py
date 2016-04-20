from github import Github

g=Github("c3f3c3b1b432d0496c9e3305ba647121da44156f");
#repositories = list(g.get_repos())
for repo in g.get_user().get_repos():
    if(repo.name == "teste"):
    	repositorie = repo
print repo.