import requests
from .GitHubClasses import GitHubUser, GitHubCommit


USER_ENDPOINT: str = "https://api.github.com/users/{}"
COMMITS_ENDPOINT: str = "https://api.github.com/users/{}/events/public"
ZEN_ENDPOINT: str = "https://api.github.com/zen"

class GitHubApi():
    
    """ ATTRIBUTES """
    token: str
    use_headers: bool = False
    headers: dict = {}

    """ CONSTRUCTOR """
    def __init__(self, token: str = "") -> None:
        if token:
            self.token = token
            self.use_headers = True
            self.headers = {"Authorization" : f"Bearer {token}"}

    """ GETTERS """
    @property
    def token(self) -> str:
        return self._token

    @property
    def use_headers(self) -> bool:
        return self._use_headers

    @property
    def headers(self) -> dict:
        return self._headers

    """ SETTERS """
    @token.setter
    def token(self, value: str):
        self._token = value

    @use_headers.setter
    def use_headers(self, value: bool):
        self._use_headers = value

    @headers.setter
    def headers(self, value: dict):
        self._headers = value

    """ METHODS """

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


    def getCommitAdditionalInfo(self, commit_url):
        
        if self.use_headers:
            r = requests.get(commit_url, headers= self.headers)
        else:
            r = requests.get(commit_url)

        r = r.json()
        return (r["commit"]["author"]["email"], r["html_url"])
    

    def getRepoHtmlUrl(self, repo_url):
        
        if self.use_headers:
            r = requests.get(repo_url, headers= self.headers)
        else:
            r = requests.get(repo_url)

        r = r.json()
        return (r["html_url"])

    
    def get_zen_info(self):
        if self.use_headers:
            r = requests.get(ZEN_ENDPOINT, headers=self.headers)
        else:
            r = requests.get(ZEN_ENDPOINT)

        return (f"""
            Server: {r.headers["Server"]}
            Date: {r.headers["Date"]}
            RateLimit-Limit: {r.headers["X-RateLimit-Limit"]}
            RateLimit-Used: {r.headers["X-RateLimit-Used"]}
            RateLimit-Remaining: {r.headers["X-RateLimit-Remaining"]}
        """)

    
    def __str__(self) -> str:
        return (f"""
        Use headers: {self.use_headers}
        Headers: {self.headers}
        """)

