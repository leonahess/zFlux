import json

from src.controller import Controller


def main():
    json_data = open("config.json").read()
    config = json.loads(json_data)

    Controller().main(config)


if __name__ == "__main__":
        main()
