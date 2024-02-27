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

    @classmethod
    def repos_api_to_html(self, repos_url: str) -> str:
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