import json
from types import SimpleNamespace as Obj
from ex1.ex1_a import ex1_a
from ex2.ex_2 import ex2_a

def main():
    with open('config.json') as config_file:
        config = json.load(config_file, object_hook=lambda d: Obj(**d))

    # print("Exercise 1:")
    # ex1_a(config.ex1)

    print("Exercise 2:")
    print()
    ex2_a()



if __name__ == "__main__":
    main()
