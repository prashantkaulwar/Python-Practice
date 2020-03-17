from github import Github

# First create a Github instance:

# using username and password
g = Github("prashantkaulwar@gmail.com", "pr@sh@ntk16191")

# or using an access token
g = Github("ba4571518e8811d98d1bb460b5ef1cb4f060151e")

# Github Enterprise with custom hostname
g = Github(base_url="https://github.com/prashantkaulwar/api/v3", login_or_token="ba4571518e8811d98d1bb460b5ef1cb4f060151e")


# Then play with your Github objects:
#users = g.get_user();
#repos = g.get_repos()
#repo = repos[0]
#repos.totalCount
#repo = g.get_repo("prashantkaulwar/python_documentation_test");
print(g.get_user())
'''
for repo in g.get_user().get_repos():
    print(dir(repo.name))
'''
# to see all the available attributes and methods
#print(dir(g))

#pip install PyGithub['integrations']
