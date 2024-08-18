def main():
    hello()
    name = input("what is your name?\n")
    hello(name)



def hello(to="world"):
    print("Hello, ",to)


main()    