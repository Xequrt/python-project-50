import json


def parse(data, extension):
    if extension == 'json':
        return json.loads(data)