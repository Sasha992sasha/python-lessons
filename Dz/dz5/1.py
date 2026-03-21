import colorama

colorama.init()

colorama.Fore.RED

print("Test")
print(colorama.Fore.GREEN + "Test")
print(colorama.Fore.BLUE +"Test")
print(colorama.Back.WHITE + "Test")
print(colorama.Style.RESET_ALL)
print(colorama.Style.BRIGHT + "Test")
print("5букв" +  colorama.Cursor.BACK(5) + "Test")