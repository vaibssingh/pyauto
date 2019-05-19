import pyautogui, time
import random
i = 0
nameField = (850, 434)
subtopic = (1120, 532)
saveButton = (1220, 295)
print("Entering info...")
time.sleep(5)

pyautogui.click(nameField)
print('Click!')
try:
    while i < 18:
        # gh = random.choice(('u'))
        # pyautogui.press([gh])
        pyautogui.press('u')
        pyautogui.press('tab', presses= 2)
        print('tabbed')
        time.sleep(1)
        # j = 0
        # sub = ["Classification of hormones", "Mechanism of hormone action", "Structure and functions of pituitary gland", "Thyroid gland", "Parathyroid gland", "Adrenal gland", "Pancreas", "Pineal gland", "Thymus and their disorders"]
        # for topic in sub:    
        #     pyautogui.typewrite(sub[j])
        #     pyautogui.press('tab')
        #     j += 1 
        # time.sleep(1)
        # pyautogui.scroll(-1)
        # time.sleep(1)
        i += 1
except KeyboardInterrupt:
    print('\nDone.')
