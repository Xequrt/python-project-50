def convert_to_str(value):
    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, int):
        return value
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return str(value)


def get_plain(diff, path=''):
    result = []
    for elem in diff:
        full_path = f'{path}.{elem["key"]}' if path else elem["key"]

        if elem['type'] == 'tree':
            result.append(get_plain(elem['children'], full_path))
        elif elem['type'] == 'added':
            result.append(f"Property '{full_path}' was added with value: {convert_to_str(elem['value'])}")
        elif elem['type'] == 'removed':
            result.append(f"Property '{full_path}' was removed")
        elif elem['type'] == 'changed':
            result.append(f"Property '{full_path}' was updated. "
                          f"From {convert_to_str(elem['old'])} "
                          f"to {convert_to_str(elem['new'])}")
    return "\n".join(result)
