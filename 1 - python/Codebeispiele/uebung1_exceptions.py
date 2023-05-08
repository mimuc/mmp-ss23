try:
    test = open("test.txt", "r")
except IOError:
    print("file doesn‘t exist")


