import json

class CustomEncoder(json.JSONEncoder):

    def default(self, toenconde):
        return toenconde.__dict__
