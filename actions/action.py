import sys
import os

class Action(object):
    STATUS_SUCCESS = 0
    STATUS_NEUTRAL = 78
    STATUS_FAILURE = 1

    def __init__(self, *args, **kwargs):
        if kwargs.get("require_github_token", False) is True and self.get_github_token() is None:
            print("The GITHUB_TOKEN secret is required for this action. Please enable and try again.")
            self.exit(self.STATUS_FAILURE)

    def exit(self, code):
        sys.exit(code)

    @property
    def env(self):
        return os.environ

    def get_github_token(self):
        return self.env.get("GITHUB_TOKEN")

    def get_home_path(self):
        return self.env.get("HOME")

    def get_event_path(self):
        return self.env.get("GITHUB_EVENT_PATH")
    
    def get_event_name(self):
        return self.env.get("GITHUB_EVENT_NAME")
    
    def get_action_name(self):
        return self.env.get("GITHUB_ACTION")

    def get_workflow_name(self):
        return self.env.get("GITHUB_WORKFLOW")

    def get_actor_name(self):
        return self.env.get("GITHUB_ACTOR")

    def get_repository_name(self):
        return self.env.get("GITHUB_REPOSITORY")

    def get_sha(self):
        return self.env.get("GITHUB_SHA")

    def get_ref(self):
        return self.env.get("GITHUB_REF")

    def get_secret(self, secret_name):
        return self.env.get(secret_name)
