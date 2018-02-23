import pyautogui as pg
pg.PAUSE = 1
pg.FAILSAFE = True
print(pg.size())
width, height = pg.size()

# #Moving the mouse
# for i in range(5):
#     pg.moveRel(100, 0, duration=0.25)
#     pg.moveRel(0, 100, duration=0.25)
#     pg.moveRel(-100, 0, duration=0.25)
#     pg.moveRel(0, -100, duration=0.25)

print(pg.position())
pg.position()
