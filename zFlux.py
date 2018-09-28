import json

from src.controller import Controller


if __name__ == "__main__":
    json_data = open("config.json").read()
    config = json.loads(json_data)

    Controller().main(config)
