from gendiff.data import extensions_data
from gendiff.parser import parse
from gendiff.stylish import stylish


def build_diff(parsed_data1, parsed_data2):
    return {
        "value": "root",
        "children": make_diff(parsed_data1, parsed_data2)
    }


def make_diff_unchanged(data1, key):
    return {
        "key": key,
        "value": "unchanged",
        "meta": data1[key]
    }


def make_diff_changed(data1, data2, key):
    return {
        "key": key,
        "value": "changed",
        "new": data1[key],
        "old": data2[key]
    }


def make_diff_added(data2, key):
    return {
        "key": key,
        "value": "added",
        "old": data2[key]
    }


def make_diff_removed(data1, key):
    return {
        "key": key,
        "value": "removed",
        "new": data1[key]
    }


def make_diff(data1, data2):
    diff = []
    for key in sorted(set(data1.keys()) | set(data2.keys())):
        if key in data1 and key in data2:
            if isinstance(data1[key], dict) and isinstance(data2[key], dict):
                child = make_diff(data1[key], data2[key])
                if child:
                    diff.append({
                        "key": key,
                        "value": "tree",
                        "children": child
                    })
                else:
                    diff.append(make_diff_unchanged(data1, key))
            elif data1[key] == data2[key]:
                diff.append(make_diff_unchanged(data1, key))
            else:
                diff.append(make_diff_changed(data1, data2, key))
        elif key not in data2:
            if isinstance(data1[key], dict):
                diff.append({
                    "key": key,
                    "value": "tree",
                    "children": make_diff(data1[key], {})
                })
            else:
                diff.append(make_diff_removed(data1, key))
        elif key not in data1:
            if isinstance(data2[key], dict):
                diff.append({
                    "key": key,
                    "value": "tree",
                    "children": make_diff({}, data2[key])
                })
            else:
                diff.append(make_diff_added(data2, key))
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
