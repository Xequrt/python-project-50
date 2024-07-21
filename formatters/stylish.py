PREFIX = {
    "added": '+ ',
    "removed": '- ',
    "unchanged": '  ',
    "tree": '  '
}
DEFAULT_INDENT = 4


def convert_to_str(value, depth=0, indent_char=' '):
    indent_size = (indent_char * (DEFAULT_INDENT - 2))
    if isinstance(value, dict):
        child_indent = get_indent(depth + 1)
        lines = ["{"]
        for key, val in value.items():
            if isinstance(val, dict):
                lines.append(f"{indent_size}{child_indent}{key}: "
                             f"{convert_to_str(val, depth + 1)}")
            else:
                lines.append(f'{indent_size}{child_indent}{key}: '
                             f'{convert_to_str(val, depth)}')
        lines.append(f"{get_indent(depth)}{indent_size}}}")
        return "\n".join(lines)
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return str(value)


def get_indent(depth, indent_char=' ', indent_size=DEFAULT_INDENT):
    indent_size = (depth * indent_size - 2)
    indent = indent_char * indent_size
    return indent


def stylish(diff, depth=0):
    if diff['type'] == 'root':
        lines = list(
            map(
                lambda x: stylish(x, depth + 1),
                diff['children']
            )
        )
        result = '\n'.join(lines)
        return f'{{\n{result}\n}}'
    elif diff['type'] == 'tree':
        lines = list(
            map(
                lambda x: stylish(x, depth + 1),
                diff['children']))
        result = '\n'.join(lines)
        return (f"{get_indent(depth)}{PREFIX['tree']}{diff['key']}:"
                f" {{\n{result}\n{get_indent(depth)}{PREFIX['tree']}}}")
    elif diff['type'] == 'added':
        return (f"{get_indent(depth)}{PREFIX['added']}{diff['key']}:"
                f" {convert_to_str(diff['value'], depth)}")
    elif diff['type'] == 'removed':
        return (f"{get_indent(depth)}{PREFIX['removed']}{diff['key']}:"
                f" {convert_to_str(diff['value'], depth)}")
    elif diff['type'] == 'unchanged':
        return (f"{get_indent(depth)}{PREFIX['unchanged']}{diff['key']}:"
                f" {convert_to_str(diff['value'], depth)}")
    elif diff['type'] == 'changed':
        return (f"{get_indent(depth)}{PREFIX['removed']}{diff['key']}:"
                f" {convert_to_str(diff['old'], depth)}\n"
                f"{get_indent(depth)}{PREFIX['added']}{diff['key']}:"
                f" {convert_to_str(diff['new'], depth)}")
