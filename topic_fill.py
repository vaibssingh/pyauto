import pyautogui, time
import random
i = 0
nameField = (850, 434)
subtopic = (1120, 532)
saveButton = (1220, 295)
print("Entering info...")
time.sleep(5)
try:
    while i < 4:
        pyautogui.click(nameField)
        print('click!')
        # gh = random.choice(('u'))
        # pyautogui.press([gh])
        pyautogui.press('f')
        pyautogui.press('tab', presses= 2)
        print('tabbed')
        j = 0
        sub = ["Classification of hormones", "Mechanism of hormone action", "Structure and functions of pituitary gland", "Thyroid gland", "Parathyroid gland", "Adrenal gland", "Pancreas", "Pineal gland", "Thymus and their disorders"]
        for topic in sub:    
            pyautogui.typewrite(sub[j])
            pyautogui.press('tab')
            j += 1 
        time.sleep(1)
        pyautogui.scroll(-1)
        # time.sleep(1)
        i += 1
except KeyboardInterrupt:
    print('\nDone.')
