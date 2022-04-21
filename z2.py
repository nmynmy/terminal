import os
import sys
import argparse
import os
import configparser  # импортируем библиотеку
import pickle


class Data:
    def __init__(self, age="", name="", fav_food="", fav_drink=""):
        self.age = age
        self.name = name
        self.fav_food = fav_food
        self.fav_drink = fav_drink


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-f", "--file", default="default.ini", help="Input settings file name")
    parser.add_argument("-a", "--action", default="", help="Describe an action: read or write")
    args = parser.parse_args()

    data = Data()

    if os.path.isfile(args.file) == True:

        config = configparser.ConfigParser()  # создаём объекта парсера
        config.read(args.file, encoding="UTF-8")  # читаем конфиг
        data.name = config["Info"]["name"]
        data.age = config["Info"]["age"]
        data.fav_food = config["Info"]["fav_food"]
        data.fav_drink = config["Info"]["fav_drink"]
        pickled_data = pickle.dumps(data)
        # config.add_section("Data2")
        config["Data"]["data"] = str(pickled_data)

        with open(f"{args.file}", "w") as configfile:
            config.write(configfile)

        # print(config["Twitter"]["username"])  # обращаемся как к обычному словарю!
        print(config["Data"]["data"])
        new_data = pickle.loads(pickled_data)
        print("Age from settings:", new_data.age)
    else:
        print("File has not been found")

""" picklefile = open("data", "rb")
 data = pickle.load(picklefile)
 picklefile.close()
 print()"""

# new_data = pickle.loads(pickled_data)
# print(new_data)

# print(pickle.loads(bytes(config["Data2"]["data"], encoding="UTF-8")))
# 'johndoe'
