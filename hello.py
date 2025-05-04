import argparse
import os


def create_file(filename, content=""):
    """Create a new file with optional content."""
    if os.path.exists(filename):
        print(f"Error: File '{filename}' already exists.")
        return
    with open(filename, "w") as file:
        file.write(content)
    print(f"File '{filename}' created successfully.")


def read_file(filename):
    """Read and print the content of a file."""
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' does not exist.")
        return
    with open(filename, "r") as file:
        content = file.read()
    print(f"Content of '{filename}':\n{content}")


def append_to_file(filename, content):
    """Append content to an existing file."""
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' does not exist.")
        return
    with open(filename, "a") as file:
        file.write(content)
    print(f"Content appended to '{filename}'.")


def main():
    parser = argparse.ArgumentParser(description="A simple notepad program.")
    parser.add_argument("action", choices=["create", "read", "append"], help="Action to perform on the file.")
    parser.add_argument("filename", help="The name of the file.")
    parser.add_argument("--content", help="Content to add to the file (for create and append actions).", default="")

    args = parser.parse_args()

    if args.action == "create":
        create_file(args.filename, args.content)
    elif args.action == "read":
        read_file(args.filename)
    elif args.action == "append":
        append_to_file(args.filename, args.content)


if __name__ == "__main__":
    main()
