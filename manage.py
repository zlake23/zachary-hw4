import utils
import sys



if len(sys.argv) > 1:
    command = sys.argv[1]
    if command == "build":
        print("[Build was specified]")
        if __name__ == "__main__":
            utils.main()
    elif command == "new":
        print("New page was specified")
        utils.new_page()
    else:
        print('Please specify "build" or "new"')
else:
    print('''Usage:
        Rebuild site: python manage.py build
        Create new page: python manage.py new''')
