import pyautogui

# waifu variable is going to be waifu count plus 1

my_screen = pyautogui.size()
waifu = 340
leftovers = [
    310, 285, 215, 213, 201, 195, 191, 182, 168, 151, 144, 140, 118,
    115, 95, 92, 75, 70, 60, 59, 46, 40, 34, 21, 19, 16, 10, 4
]
body_count = 0


pyautogui.moveTo(450, 1025, duration=0.50)
pyautogui.click()

# for i in range(waifu):
#     waifu -= 1
#     pyautogui.typewrite(f'w!interact {waifu}', 0.30)
#     pyautogui.typewrite(['enter'])
#     if waifu == 0:
#         break

for i in leftovers:
    pyautogui.typewrite(f'w!interact {leftovers[body_count]}', 0.30)
    pyautogui.typewrite(['enter'])
    body_count += 1
    if leftovers[body_count] == leftovers[27]:
        break

