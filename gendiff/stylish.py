PREFIX = {
    "added": '+ ',
    "removed": '- ',
    "unchanged": '  ',
    "tree": '  '
}
DEFAULT_INDENT = 4


def convert_to_str(value, depth=0, indent_char=' ', indent_size=DEFAULT_INDENT):
    if isinstance(value, dict):
        current_indent = indent_char * depth
        child_indent = indent_char * (depth + indent_size)
        lines = ["{"]
        for key, val in value.items():
            lines.append(f"{child_indent}{key}: "
                         f"{convert_to_str(val, depth + 1, indent_char, indent_size)}")
        lines.append(f"{current_indent}}}")
        return "\n".join(lines)
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return str(value)


def stylish(diff, depth=0, indent_char=' ', indent_size=DEFAULT_INDENT):
    child_indent = indent_char * (depth * indent_size - 2)
    if diff['type'] == 'root':
        lines = list(
            map(
                lambda x: stylish(x, depth + 1, indent_char, indent_size),
                diff['children']
            )
        )
        result = '\n'.join(lines)
        return f'{{\n{result}\n}}'
    elif diff['type'] == 'tree':
        lines = list(
            map(
                lambda x: stylish(x, depth + 1, indent_char, indent_size),
                diff['children']))
        result = '\n'.join(lines)
        return (f"{child_indent}{PREFIX['tree']}{diff['key']}:"
                f" {{\n{result}\n{child_indent}}}")
    elif diff['type'] == 'added':
        return (f"{child_indent}{PREFIX['added']}{diff['key']}:"
                f" {convert_to_str(diff['old'], depth, indent_char, indent_size)}")
    elif diff['type'] == 'removed':
        return (f"{child_indent}{PREFIX['removed']}{diff['key']}:"
                f" {convert_to_str(diff['new'], depth, indent_char, indent_size)}")
    elif diff['type'] == 'unchanged':
        return (f"{child_indent}{PREFIX['unchanged']}{diff['key']}:"
                f" {convert_to_str(diff['value'], depth, indent_char, indent_size)}")
    elif diff['type'] == 'changed':
        return (f"{child_indent}{PREFIX['removed']}{diff['key']}:"
                f" {convert_to_str(diff['new'], depth, indent_char, indent_size)}\n"
                f"{child_indent}{PREFIX['added']}{diff['key']}:"
                f" {convert_to_str(diff['old'], depth, indent_char, indent_size)}")
