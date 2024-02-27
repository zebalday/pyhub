import requests
from .GitHubClasses import GitHubUser, GitHubCommit


USER_ENDPOINT: str = "https://api.github.com/users/{}"
COMMITS_ENDPOINT: str = "https://api.github.com/users/{}/events/public"


class GitHubApi():
    
    """ ATTRIUTES """
    headers: dict = {}
    use_headers: bool = False

    """ CONSTRUCTOR """
    def __init__(self, use_headers: bool, auth_token: str = "", request_id: str = "") -> None:
        self.use_headers = use_headers
        self.headers["Authorization"] = auth_token
        self.headers["request_id"] = request_id

    """ METHODS """
    @classmethod
    def getUser(self, username) -> GitHubUser:
        
        if self.use_headers:
            r = requests.get(USER_ENDPOINT.format(username), headers= self.headers)
        else:
            r = requests.get(USER_ENDPOINT.format(username))
        
        if r.status_code == 200:
            r = r.json()
            user = GitHubUser(
                            username=r["login"],
                            user_url=r["html_url"],
                            full_name=r["name"],
                            location=r["location"],
                            bio = r["bio"],
                            avatar_url=r["avatar_url"],
                            repos_url=r["repos_url"]
            )
            return user
        
        raise Exception("User couldn't be found.")

    @classmethod
    def getLastCommits(self, username, number) -> list:
        
        if self.use_headers:
            r = requests.get(COMMITS_ENDPOINT.format(username), headers= self.headers)
        else:
            r = requests.get(COMMITS_ENDPOINT.format(username))
        

        if r.status_code == 200:
            # Filter PushEvents and number of commits
            push_list = [x for x in r.json() if x["type"]== "PushEvent"]
            push_list = push_list[:number]
            
            last_commits_info = []
            
            for push in push_list:
                
                commit_url = push["payload"]["commits"][-1]["url"]
                email, commit_html = self.getCommitAdditionalInfo(commit_url)
                repo_url = self.getRepoHtmlUrl(push["repo"]["url"])
                
                commit = GitHubCommit(
                    username= push["actor"]["display_login"],
                    email= email,
                    repo_name= push["repo"]["name"],
                    repo_url= repo_url,
                    commit_message= push["payload"]["commits"][-1]["message"],
                    commit_url= commit_html,
                    commit_date= push["created_at"]
                )
                
                last_commits_info.append(commit)
        
            return last_commits_info
        
        raise Exception ("User couldn't be found.")

    @classmethod
    def getCommitAdditionalInfo(self, commit_url):
        
        if self.use_headers:
            r = requests.get(commit_url, headers= self.headers)
        else:
            r = requests.get(commit_url)

        r = r.json()
        return (r["commit"]["author"]["email"], r["html_url"])
    
    @classmethod
    def getRepoHtmlUrl(self, repo_url):
        
        if self.use_headers:
            r = requests.get(repo_url, headers= self.headers)
        else:
            r = requests.get(repo_url)

        r = r.json()
        return (r["html_url"])



