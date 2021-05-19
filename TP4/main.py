import json
from types import SimpleNamespace as Obj
from ex1.ex1_a import ex1_a
from ex1.ex1_b import ex1_b
from ex2.ex_2 import *


def main():
    with open('config.json') as config_file:
        config = json.load(config_file, object_hook=lambda d: Obj(**d))

    print("Exercise 1a:")
    ex1_a(config.ex1)
    print("Exercise 1b:")
    ex1_b(config.ex1)
    print("Exercise 2:")
    ex2_a()


if __name__ == "__main__":
    main()