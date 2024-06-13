PREFIX = {
    "added": '+ ',
    "removed": '- ',
    "unchanged": '  ',
    "tree": '  '
}
DEFAULT_INDENT = 4


def format_line(dictionary, key, depth, prefix):
    return f'{" " * depth}{prefix}{dictionary[key]}: {str(dictionary[key]).lower()}\n'

def stylish(diff, depth=0):
    result = ["{"]
    for elem in diff:
        key = elem['key']
        value = elem['value']
        if value == 'unchanged':
            result.append(format_line(elem, elem['meta'], depth, PREFIX['unchanged']))
        if value == 'added':
            result.append((format_line(elem, 'new', depth, PREFIX['added'])))
        if value == 'removed':
            result.append(format_line((elem, 'old', depth, PREFIX['removed'])))
        if value == 'changed':
            result.append(format_line((elem, 'new', depth, PREFIX['added'])))
        if value == 'tree':
            new_meta = stylish(diff['meta'], depth + DEFAULT_INDENT)
            result.append(
                f'{" " * depth}    {key}: {new_meta}')
            result.append(f'{" " * depth}}}')
            return '\n'.join(result)

def output_stylish(diff):
    return stylish(diff)