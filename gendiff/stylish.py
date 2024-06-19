PREFIX = {
    "added": '+ ',
    "removed": '- ',
    "unchanged": '  ',
    "tree": '  '
}
DEFAULT_INDENT = 4


def stylish(diff, depth=0, indent_char=' ', indent_size=DEFAULT_INDENT):
    result = ["{"]

    child_indent = indent_char * (depth * indent_size - 2)
    # if len(diff) >= 1:
    #     result.append(f"{indent_char * depth}{{")
    # else:
    #     result.append(f"{indent_char * depth}")
    for element in diff:
        if element['value'] == 'tree':
            new_meta = stylish(element['children'], depth + 1)
            result.append(f"{child_indent}{element['key']}: {new_meta}")
        elif element['value'] == 'added':
            result.append(f"{child_indent}{PREFIX['added']}{element['key']}: {element['old']}")
        elif element['value'] == 'removed':
            result.append(f"{child_indent}{PREFIX['removed']}{element['key']}: {element['new']}")
        elif element['value'] == 'unchanged':
            result.append(f"{child_indent}{PREFIX['unchanged']}{element['key']}: {element['meta']}")
        elif element['value'] == 'changed':
            result.append(f"{child_indent}{PREFIX['removed']}{element['key']}: {element['new']}")
            result.append(f"{child_indent}{PREFIX['added']}{element['key']}: {element['old']}")

    result.append(f"{indent_char * depth}}}")

    return '\n'.join(result)


def output_stylish(diff):
    return stylish(diff)
