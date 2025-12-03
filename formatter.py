from maps import code_to_description_map, code_to_emoji_map_day, code_to_emoji_map_night, week_days
import datetime

sunrise: float = 5
sunset: float = 17

# test the emoji suite uwu
def test_emojis() -> None:
    for k in code_to_emoji_map_day:
        print(f"{code_to_description_map[k]}: {code_to_emoji_map_day[k]}")
    print()
    for k in code_to_emoji_map_night:
        print(f"{code_to_description_map[k]}: {code_to_emoji_map_night[k]}")

# returns a brief, few-word description of the weather encoded by code
def weather_code_to_description(code: str) -> str:
    code = code.lower()
    time_modifier: str = ""
    if code.endswith("am") or code.endswith("pm"):
        time_modifier = code[-2:].upper() + " " if len(code) == 2 else ""
        code = code[:-2]
    if not code in code_to_description_map.keys():
        raise Exception(f"Invalid code entered! Valid codes are {code_to_description_map.keys()}")
    return f"{time_modifier}{code_to_description_map[code]}"

# returns an emoji that visually describes the weather encoded by code
def weather_code_to_emoji(code: str, hour: int) -> str:
    code = code.lower()
    if code.endswith("am") or code.endswith("pm"):
        code = code[:-2]
    if not code in code_to_description_map.keys():
        raise Exception(f"Invalid code entered! Valid codes are {code_to_description_map.keys()}")
    map = code_to_emoji_map_day if is_day(hour) else code_to_emoji_map_night
    return map[code]

# returns a string in the format XX:00 {A/P}M representing hour as a twelve-hour time
def hour_to_12_hour_time(hour: int)  -> str:
    pm: bool = False
    if hour > 12:
        hour %= 12
    if hour >= 12:
        pm = True
    return f"{hour:2}:00 {"PM" if pm else "AM"}"

# checks whether a given time is during daylight hours
def is_day(hour: int) -> bool:
    return hour > sunrise and hour < sunset

# prompts the user for input and displays the formatted output to standard output
def format_hourly(start_time: int, end_time: int, increment: int) -> None:
    times:         list[int] = []
    temps:         list[int] = []
    weather_codes: list[str] = []
    for hour in range(start_time, end_time, increment):
        times.append(hour)
        line: list[str] = input(f"{hour:2}:00 - ").split()
        try:
            temps.append(int(line[0]))
            weather_codes.append(line[1])
        except:
            print("Expected format <temp: int> <weather code: string>")
            continue
    print("\n**Tomorrow**")
    for hour, temp, code in zip(times, temps, weather_codes):
        print(f"`{hour_to_12_hour_time(hour)} - `{weather_code_to_emoji(code, hour)}` {temp} {weather_code_to_description(code)}`\n")

def format_multiday(num_days: int, today: int = datetime.datetime.today().weekday()) -> None:
    days:          list[str] = []
    highs:         list[int] = []
    lows:          list[int] = []
    weather_codes: list[str] = []
    for day in range(today + 1, today + 1 + num_days):
        days.append(week_days[day % 7])
        line: list[str] = input(f"{week_days[day % 7]}: ").split()
        try:
            lows.append(int(line[0]))
            highs.append(int(line[1]))
            weather_codes.append(line[2])
        except:
            print("Expected format <low temp: int> <high temp: int> <weather code: str>")
            continue
    print(f"\n**{num_days} Day Forecast**\n")
    for day, low, high, code in zip(days, lows, highs, weather_codes):
        print(f"`{day}...`{weather_code_to_emoji(code, 12)}` {low:>3} | {high:>3} {weather_code_to_description(code)}`\n")


def run() -> int:
    mode = input("Hourly (h) or multiday (m)? ").lower().strip()
    if mode == "h":
        format_hourly(7, 20, 3)
        return 0
    elif mode == "m":
        format_multiday(5)
        return 0
    else:
        print("Unknown mode {mode}. Please try again.")
        return 1
