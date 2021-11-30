import datetime
import pathlib
import getpass
import json
import os


def get_path() -> pathlib.Path:
    with open("config.json") as file:
        config: dict = json.load(file)
        custom_path = config.get("custom_path")
        if custom_path.get("use_custom_path"):
            return pathlib.Path(custom_path.get("path"))
        else:
            sys_disk = config.get('sys_disk')
            username = getpass.getuser()
            return pathlib.Path(f"{sys_disk}:/Users/{username}/AppData/Roaming/Zoom/bin/Zoom.exe")


def set_offset(hours: list[list[int, int], list[int, int]]):
    def format_time(time):
        time[0] = (time[0] + time[1] // 60) % 24
        time[1] %= 60
        if time[1] < 0:
            time[0] -= 1
            time[1] += 60
        return time
    with open("config.json") as file:
        config: dict = json.load(file)
        offsets: dict = config.get("offsets", {})
        hours[0][1] += offsets.get("start", 0)
        hours[1][1] += offsets.get("end", 0)
    hours = format_time(hours[0]), format_time(hours[1])
    return [int(''.join(str(n) for n in hour)) for hour in hours]


def load_schedule() -> dict:
    with open("schedule.json") as file:
        return json.load(file)


def join(class_number):
    if type(class_number) is list and len(class_number) == 1:
        class_number = class_number[0]
    if type(class_number) is int:
        cmd = f'start /B {PATH} --url="zoommtg://zoom.us/join?action=join&confno={class_number}"'
    elif type(class_number) is list and len(class_number) == 2:
        cmd = f'start /B {PATH} --url="zoommtg://zoom.us/join?action=join&confno={class_number[0]}&pwd={class_number[1]}"'
    else:
        print(f"Unexpected error, parsed key: {class_number}")
        return
    os.system(cmd)


def check_for_class(schedule: dict):
    now = datetime.datetime.now()
    day = now.strftime("%A")
    time = now.strftime("%X")[:-3]

    classes: dict = schedule.get(day)
    if classes:
        for hour_set in classes.keys():
            hours = [[int(num) for num in hour.split(":")] for hour in hour_set.split("-")]
            hours = set_offset(hours)
            split_time = int(time.replace(":", ''))
            if hours[0] <= split_time <= hours[1]:
                join(classes.get(hour_set))
                return
    print(f"There are no meetings configured for {day}s at {time}!")
    input("Press any key to close this window...")


if __name__ == "__main__":
    PATH = get_path()
    data = load_schedule()
    check_for_class(data)
