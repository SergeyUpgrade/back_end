def get_operations():
    return

def format_data(srt_data: str):
    my_data = srt_data.split("T")[0].split("-")
    return ".".join(my_data[::-1])


format_data("2019-07-03T18:35:29.512364")