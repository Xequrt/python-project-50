from gendiff.cli import parse_arguments
from gendiff.generate_diff import generate_diff
import json

def main():
    args = parse_arguments()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(json.dumps(diff, indent=4))

    if __name__ == '__main__':
        main()