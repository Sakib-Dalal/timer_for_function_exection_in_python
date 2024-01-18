from main import timer


@timer
def display():
    print("Hello World")


@timer
def printing():
    print("How is this")


display()
printing()
