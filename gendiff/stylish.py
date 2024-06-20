PREFIX = {
    "added": '+ ',
    "removed": '- ',
    "unchanged": '  ',
    "tree": '  '
}
DEFAULT_INDENT = 4


def stylish(diff, depth=0, indent_char=' ', indent_size=DEFAULT_INDENT):
    child_indent = indent_char * (depth * indent_size - 2)
    if diff['value'] == 'root':
        lines = list(map(lambda x: stylish(x, depth + 1, indent_char, indent_size), diff['children']))
        result = '\n'.join(lines)
        return f'{{\n{result}\n}}'
    elif diff['value'] == 'tree':
        lines = list(map(lambda x: stylish(x, depth + 1, indent_char, indent_size), diff['children']))
        result = '\n'.join(lines)
        return f"{child_indent}  {diff['key']}: {{\n{result}\n{child_indent}  }}"
    elif diff['value'] == 'added':
        return f"{child_indent}{PREFIX['added']}{diff['key']}: {diff['old']}"
    elif diff['value'] == 'removed':
        return f"{child_indent}{PREFIX['removed']}{diff['key']}: {diff['new']}"
    elif diff['value'] == 'unchanged':
        return f"{child_indent}{PREFIX['unchanged']}{diff['key']}: {diff['meta']}"
    elif diff['value'] == 'changed':
        return f"{child_indent}{PREFIX['removed']}{diff['key']}: {diff['new']}\n{child_indent}{PREFIX['added']}{diff['key']}: {diff['old']}"

