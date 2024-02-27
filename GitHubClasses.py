from datetime import datetime

class GitHubCommit():

    """ ATTRIBUTES """

    username: str
    email: str
    repo_url: str
    commit_url: str
    commit_message: str
    commit_date: str

    """ CONSTRUCTOR """

    def __init__(self, username: str, email: str, repo_name: str, repo_url: str, commit_url: str, commit_message: str, commit_date: str) -> None:
        self.username = username
        self.email = email
        self.repo_name = self.repo_name_shortener(username, repo_name)
        self.repo_url = repo_url
        self.commit_url = commit_url
        self.commit_message = commit_message
        self.commit_date = self.commit_date_formatter(commit_date)

    """ GETTERS """

    @property
    def username(self) -> str:
        return self._username

    @property
    def email(self) -> str:
        return self._email

    @property
    def repo_name(self) -> str:
        return self._repo_name

    @property
    def repo_url(self) -> str:
        return self._repo_url

    @property
    def commit_url(self) -> str:
        return self._commit_url

    @property
    def commit_message(self) -> str:
        return self._commit_message

    @property
    def commit_date(self) -> str:
        return self._commit_date
    
    """ SETTERS """

    @username.setter
    def username(self, value: str):
        self._username = value

    @email.setter
    def email(self, value: str):
        self._email = value

    @repo_name.setter
    def repo_name(self, value: str):
        self._repo_name = value

    @repo_url.setter
    def repo_url(self, value: str):
        self._repo_url = value

    @commit_url.setter
    def commit_url(self, value: str):
        self._commit_url = value

    @commit_message.setter
    def commit_message(self, value: str):
        self._commit_message = value

    @commit_date.setter
    def commit_date(self, value: str):
        self._commit_date = value

    """ METHODS """
    
    @staticmethod
    def repo_name_shortener(username, repo_name) -> str:
        return (repo_name.replace(f"{username}/",""))

    @staticmethod
    def commit_date_formatter(commit_date) -> str:
        commit_date = datetime.strptime(commit_date,"%Y-%m-%dT%H:%M:%SZ")
        return (commit_date.strftime("%d-%m-%Y"))
    
    def __str__(self) -> str:
        return (f"""
            Commiter Username: {self.username}
            Comitter Email: {self.email}
            Repo Name: {self.repo_name}
            Repo URL: {self.repo_url}
            Commit Message: {self.commit_message}
            Commit Date: {self.commit_date}
            Commit URL: {self.commit_url}
            """
        )
    



class GitHubUser():
    
    """ ATTRIBUTES """
    
    username: str
    full_name: str
    location: str
    bio: str
    avatar_url: str
    repos_url: str

    """ CONSTRUCTOR """

    def __init__(self, username, full_name, location, bio, avatar_url, repos_url) -> None:
        self.username = username
        self.full_name = full_name
        self.location = location
        self.bio = bio
        self.avatar_url = avatar_url
        self.repos_url = self.repos_api_to_html(repos_url)

    """ GETTERS """

    @property
    def username(self) -> str:
        return self._username

    @property
    def name(self) -> str:
        return self._full_name

    @property
    def location(self) -> str:
        return self._location

    @property
    def bio(self) -> str:
        return self._bio

    @property
    def avatar(self) -> str:
        return self._avatar_url
    
    @property
    def repos(self) -> str:
        return self._repos_url
    
    
    """ SETTERS """

    @username.setter
    def username(self, value: str):
        self._username = value

    @name.setter
    def name(self, value: str):
        self._full_name = value

    @location.setter
    def location(self, value: str):
        self._location = value

    @bio.setter
    def bio(self, value: str):
        self._bio = value

    @avatar.setter
    def avatar(self, value: str):
        self._avatar_url = value

    @repos.setter
    def repos(self, value: str):
        self._repos_url = value


    """ METHODS """

    @staticmethod
    def repos_api_to_html(repos_url: str) -> str:
        repos_url = repos_url.replace("api.github.com/users/","github.com/")
        repos_url = repos_url.replace("/repos","?tab=repositories")
        return (repos_url)
    
    """ TO STRING """

    def __str__(self) -> str:
        return (f"""
            Username: {self.username}
            Name: {self.full_name}
            Location: {self.location}
            Bio: {self.bio}
            Avatar: {self.avatar_url}
            Repos: {self.repos_url}
            """
        )