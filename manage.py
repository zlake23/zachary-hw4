import utils
import sys


command = sys.argv[1]

if command == "build":
    print("Build was specified")
    utils.main()
elif command == "new":
    print("New page was specified")
else:
    print("Please specify 'build' or 'new'")

# if __name__ == "__main__":
#     utils.main()