import os

file_path = "C:/Users/" + os.getlogin() + "/AppData/Roaming/chatspammer.json"
default_json = "{\"fieldSelectionTimer\":5}"


def check_config_exists():
    if not os.path.exists(file_path):
        file = open(file_path, "w")
        file.write(default_json)
        file.close()
