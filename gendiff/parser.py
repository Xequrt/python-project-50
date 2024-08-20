import json
import yaml


def parse(data, extension):
    if extension == 'json':
        return json.loads(data)
    elif extension == 'yml' or extension == 'yaml':
        return yaml.load(data, Loader=yaml.FullLoader)
    raise ValueError(f"Unrecognized extension: {extension}")
