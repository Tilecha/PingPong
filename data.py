import json

history = dict()

with open('history.json', 'r', encoding= "utf-8") as file:
    history = json.load(file)

setting_win = {
    "WIDTH": 500,
    "HEIGHT": 500
}

setting_board = {
    "WIDTH": 20,
    "HEIGHT": 100
}

setting_ball = {
    "RADIUS": 15,
}
restart = {
    "RESTART_BALL": (setting_win["WIDTH"] // 2 - setting_ball["RADIUS"],
                     setting_win["HEIGHT"] // 2 - setting_ball["RADIUS"]),
    "RESTART_BOARD_LEFT": (15,
                           setting_win["HEIGHT"] // 2 - setting_board["HEIGHT"] // 2),
}