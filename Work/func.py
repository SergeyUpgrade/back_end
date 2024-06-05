def get_operations():
    with open("operations.json", "r", encoding="utf-8") as file:
        print(file.read())

def format_data(srt_data: str):
    my_data = srt_data.split("T")[0].split("-")
    return ".".join(my_data[::-1])


get_operations()
