import pyautogui, time
import random
i = 0
nameField = (850, 434)
subtopic = (1120, 532)
saveButton = (1220, 295)
print("Entering info...")
time.sleep(5)
while i < 70:
    pyautogui.click(nameField)
    print('click!')
    gh = random.choice(('u', 'f'))
    pyautogui.press([gh])
    # pyautogui.click(subtopic)
    # time.sleep(1)
    pyautogui.scroll(-1)
    time.sleep(1)
    i += 1
