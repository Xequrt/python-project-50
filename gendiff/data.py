from os.path import splitext


EXTENSIONS = ('json', 'yml', 'yaml')


def extensions_data(path_file):
    extension = splitext(path_file)[1][1:]
    if extension in EXTENSIONS:
        with open(path_file) as path_file:
            data = path_file.read()
        return data, extension
    raise ValueError(f"Unrecognized extension: {extension}")
