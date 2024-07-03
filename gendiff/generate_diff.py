from gendiff.data import extensions_data
from gendiff.parser import parse
from gendiff.stylish import stylish


def build_diff(parsed_data1, parsed_data2):
    return {
        "type": "root",
        "children": make_diff(parsed_data1, parsed_data2)
    }


def make_diff_tree(child, key):
    return {
        "key": key,
        "type": "tree",
        "children": child
    }


def make_diff_unchanged(data1, key):
    return {
        "key": key,
        "type": "unchanged",
        "value": data1[key]
    }


def make_diff_changed(data1, data2, key):
    return {
        "key": key,
        "type": "changed",
        "new": data1[key],
        "old": data2[key]
    }


def make_diff_added(data2, key):
    return {
        "key": key,
        "type": "added",
        "old": data2[key]
    }


def make_diff_removed(data1, key):
    return {
        "key": key,
        "type": "removed",
        "new": data1[key]
    }


def make_diff(data1, data2):
    diff = []
    for key in sorted(set(data1.keys()) | set(data2.keys())):
        if key not in data1:
            diff.append(make_diff_added(data2, key))
        elif key not in data2:
            diff.append(make_diff_removed(data1, key))
        elif data1[key] == data2[key]:
            diff.append(make_diff_unchanged(data1, key))
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            child = make_diff(data1[key], data2[key])
            diff.append(make_diff_tree(child, key))
        elif data1[key] != data2[key]:
            diff.append(make_diff_changed(data1, data2, key))
    return diff


def generate_diff(file1_path, file2_path, output_format):
    data1, extension1 = extensions_data(file1_path)
    data2, extension2 = extensions_data(file2_path)

    parsed_data1 = parse(data1, extension1)
    parsed_data2 = parse(data2, extension2)

    diff = build_diff(parsed_data1, parsed_data2)
    if output_format == "stylish":
        return stylish(diff)

    raise ValueError(f"Unrecognized output format: {output_format}")
