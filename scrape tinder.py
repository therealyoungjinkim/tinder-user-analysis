import time
import pyautogui as auto
xpos = [111, 988, 1011, 355, 249, 217, 195, 526]
ypos = [16, 703, 967, 1058, 477, 558, 1058, 1060]

i = 0
n = 400

#click on tinder to focus - pos 0
auto.click(xpos[0], ypos[0])
time.sleep(.3)

while i < n:
    # up arrow
    auto.hotkey('up')
    time.sleep(.3)
    # right click name - pos 1
    auto.click(xpos[1], ypos[1], button='right')
    time.sleep(.3)
    # inspect element - pos 2
    auto.click(xpos[2], ypos[2])
    time.sleep(.3)
    # copy
    auto.hotkey('ctrl', 'c')
    time.sleep(.3)
    # open excel - pos 3
    auto.click(xpos[3], ypos[3])
    time.sleep(.3)
    # paste
    auto.hotkey('ctrl', 'v')
    time.sleep(.3)
    # hit tab
    auto.hotkey('tab')
    time.sleep(.3)
    # open inspection - pos 7
    auto.click(xpos[7], ypos[7])
    time.sleep(.3)
    # click the age element - pos 4
    auto.click(xpos[4], ypos[4])
    time.sleep(.3)
    # copy
    auto.hotkey('ctrl', 'c')
    time.sleep(.3)
    # open excel - pos 3
    auto.click(xpos[3], ypos[3])
    time.sleep(.3)
    # paste
    auto.hotkey('ctrl', 'v')
    time.sleep(.3)
    # hit tab
    auto.hotkey('tab')
    time.sleep(.3)
    # open inspection - pos 7
    auto.click(xpos[7], ypos[7])
    time.sleep(.3)
    # click the description element - pos 5
    auto.click(xpos[5], ypos[5])
    time.sleep(.3)
    # copy
    auto.hotkey('ctrl', 'c')
    time.sleep(.3)
    # open excel - pos 3
    auto.click(xpos[3], ypos[3])
    time.sleep(.3)
    # f2 to paste formula
    auto.hotkey('F2')
    time.sleep(.3)
    # paste
    auto.hotkey('ctrl', 'v')
    time.sleep(.3)
    # hit enter
    auto.hotkey('enter')
    time.sleep(.3)
    #go to leftmost cell
    auto.hotkey('ctrl', 'left')
    time.sleep(.3)    
    # open tinder - pos 6
    auto.click(xpos[6], ypos[6])
    time.sleep(.3)
    # right arrow
    auto.hotkey('right')
    time.sleep(.3)
    # wait 3 sec
    time.sleep(3)
    i = i + 1
    print(str(i) + " / " + str(n))
