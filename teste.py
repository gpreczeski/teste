from github import Github

g=Github("9872b3b2fb662eaddaf41bab058c127ff50a59be");
#repositories = list(g.get_repos())
for repo in g.get_user().get_repos():
    print repo.name
