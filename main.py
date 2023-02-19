import pyautogui as ag
import time as t
import config as cfg
import json

cfg.check_config_exists()

cfg_file = open(cfg.file_path, "r")
json_code = json.loads(cfg_file.read())
cfg_file.close()

print("============")
print("Chat Spammer")
print("============")

messages = int(input("Number of Messages: "))
message_text = input("Message Text: ")

print("You have", json_code["fieldSelectionTimer"], "seconds to select the chat field!")
t.sleep(json_code["fieldSelectionTimer"])

for x in range(messages):
    ag.write(message_text)
    ag.press("enter")
