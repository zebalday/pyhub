from rest_framework import serializers
from .GitHubClasses import GitHubUser, GitHubCommit

class GithubUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=250)
    user_url = serializers.CharField(max_length=250)
    full_name = serializers.CharField(max_length=250)
    location = serializers.CharField(max_length=250)
    bio = serializers.CharField(max_length=250)
    avatar_url = serializers.CharField(max_length=250)
    repos_url = serializers.CharField(max_length=250)

class GithubCommitSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=250)
    email = serializers.CharField(max_length=250)
    repo_url = serializers.CharField(max_length=250)
    commit_url = serializers.CharField(max_length=250)
    commit_message = serializers.CharField(max_length=250)
    commit_date = serializers.CharField(max_length=250)