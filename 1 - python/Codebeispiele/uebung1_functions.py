# define functions
def a():
    print("I am function a")


def b(text):
    return "I don‘t like " + text

# use the functions
a()
print(b("function a"))

# function with default parameters
def test(a=1, b=2, c=3):
    print(a + b + c)


test(1)
test(2, 2)
test(c=2)


