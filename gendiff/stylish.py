PREF = {
    "added": '+ ',
    "removed": '- ',
    "unchanged": '  ',
    "tree": '  '
}
DEFAULT_INDENT = 4


def to_str(value, depth=0, indent_char=' ', indent_size=DEFAULT_INDENT):
    if isinstance(value, dict):
        current_indent = indent_char * depth
        child_indent = indent_char * (depth + indent_size)
        lines = ["{"]
        for key, val in value.items():
            lines.append(f"{child_indent}{key}: "
                         f"{to_str(val, indent_char, indent_size)}")
        lines.append(f"{current_indent}}}")
        return "\n".join(lines)
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return str(value)


def stylish_children(diff, depth, indent_char, indent_size):
    lines = list(
        map(
            lambda x: stylish(x, depth + 1, indent_char, indent_size),
            diff['children']
        )
    )
    result = '\n'.join(lines)
    return result


def stylish(diff, depth=0, indent_char=' ', indent_size=DEFAULT_INDENT):
    child_indent = indent_char * (depth * indent_size - 2)
    if diff['value'] in ('root', 'tree'):
        result = stylish_children(diff, depth, indent_char, indent_size)
        if diff['value'] == 'root':
            return f'{{\n{result}\n}}'
        elif diff['value'] == 'tree':
            return (f"{child_indent}{PREF['tree']}{diff['key']}:"
                    f" {{\n{result}\n{child_indent}}}")
    handlers = {
        'added': lambda: f"{child_indent}{PREF['added']}{diff['key']}: "
                         f"{to_str(diff['old'], depth)}",
        'removed': lambda: f"{child_indent}{PREF['removed']}{diff['key']}: "
                           f"{to_str(diff['new'], depth)}",
        'unchanged': lambda: f"{child_indent}{PREF['unchanged']}{diff['key']}: "
                             f"{to_str(diff['meta'], depth)}",
        'changed': lambda: (f"{child_indent}{PREF['removed']}{diff['key']}: "
                            f"{to_str(diff['new'], depth)}\n"
                            f"{child_indent}{PREF['added']}{diff['key']}: "
                            f"{to_str(diff['old'], depth)}"),
    }

    handler = handlers.get(diff['value'])
    if handler:
        return handler()
    else:
        raise ValueError(f"Unknown diff value: {diff['value']}")
