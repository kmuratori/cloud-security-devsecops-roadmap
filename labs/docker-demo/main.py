import colorama, os

NAME=os.environ.get("NAME", "world2")
print("hello", colorama.Fore.RED + NAME + colorama.Style.RESET_ALL)
