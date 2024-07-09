PREFIX = {
    "added": '+ ',
    "removed": '- ',
    "unchanged": '  ',
    "tree": '  '
}
DEFAULT_INDENT = 4


def convert_to_str(value, depth=0, indent_char=' ', indent_size=DEFAULT_INDENT):
    if isinstance(value, dict):
        child_indent = get_indent('  ', depth + 1)
        lines = ["{"]
        for key, val in value.items():
            if isinstance(val, dict):
                lines.append(f"{child_indent}{key}: "
                             f"{convert_to_str(val, depth + 1, indent_char, indent_size)}")
            else:
                lines.append(f'{child_indent}{key}: '
                             f'{convert_to_str(val, depth, indent_char, indent_size)}')
        lines.append(f"{get_indent('   ', depth)}}}")
        return "\n".join(lines)
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return str(value)


def get_indent(sign, depth, indent_char=' ', indent_size=DEFAULT_INDENT):
    indent_size = (depth * indent_size - 2)
    indent = indent_char * indent_size + PREFIX.get(sign, sign)
    return indent


def stylish(diff, depth=0, indent_char=' ', indent_size=DEFAULT_INDENT):
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
        return (f"{get_indent(PREFIX['tree'], depth)}{diff['key']}:"
                f" {{\n{result}\n{get_indent(PREFIX['tree'], depth)}}}")
    elif diff['type'] == 'added':
        return (f"{get_indent(PREFIX['added'], depth)}{diff['key']}:"
                f" {convert_to_str(diff['value'], depth, indent_char, indent_size)}")
    elif diff['type'] == 'removed':
        return (f"{get_indent(PREFIX['removed'], depth)}{diff['key']}:"
                f" {convert_to_str(diff['value'], depth, indent_char, indent_size)}")
    elif diff['type'] == 'unchanged':
        return (f"{get_indent(PREFIX['unchanged'], depth)}{diff['key']}:"
                f" {convert_to_str(diff['value'], depth, indent_char, indent_size)}")
    elif diff['type'] == 'changed':
        return (f"{get_indent(PREFIX['removed'], depth)}{diff['key']}:"
                f" {convert_to_str(diff['old'], depth, indent_char, indent_size)}\n"
                f"{get_indent(PREFIX['added'], depth)}{diff['key']}:"
                f" {convert_to_str(diff['new'], depth, indent_char, indent_size)}")
