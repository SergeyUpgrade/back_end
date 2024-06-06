import json


def get_operations():
    with open("operations.json", encoding="utf-8") as file:
        return json.load(file)


def format_data(srt_data: str):
    my_data = srt_data.split("T")[0].split("-")
    return ".".join(my_data[::-1])


print(get_operations())
