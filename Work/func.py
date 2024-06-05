def get_operations():
    with open("operations.json", "w", encoding="utf-8") as file:
        info = []
        for item,key in file:
            if item == "state" and key == "EXECUTED":
                info.append(file)
        return f"{info}"


def format_data(srt_data: str):
    my_data = srt_data.split("T")[0].split("-")
    return ".".join(my_data[::-1])


print(file = open("operations.json", "w", encoding="utf-8"))
