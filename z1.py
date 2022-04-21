import os
import sys
import argparse
import os
import configparser  # импортируем библиотеку
import pickle

if __name__ == "__main__":
    print("Hello dear bunny!")
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-n", "--name", default="World!", help="Input name")
    parser.add_argument("-a", "--age", default=0, help="Input age")
    parser.add_argument("-p", "--path", default=r"C:\Users\nmy\PycharmProjects\terminal\text.txt", help="Input path")
    #path = os.getcwd()
    args = parser.parse_args()
    file = open(args.path, "a")
    try:
        file.write(args.name + "\n")
        file.write(str(args.age) + "\n")
        file.write(args.path + "\n")
    finally:
        file.close()

    ans = input("Delete or not? Please answer 'yes' or 'no'\n")

    if ans[0] == "y" or ans[0] == "Y":
        os.remove(file.name)
    elif ans[0] != "n":
        print("Please answer 'yes' or 'no'")

    print(f'Hello {args.name}')
    print(args)
