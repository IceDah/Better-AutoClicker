import pyautogui
from pynput.keyboard import *

#Settings
delay = 0.2
resume = Key.f1
pause_key = Key.f2
exit_key = Key.f3
pdelay = Key.f4
mdelay = Key.f5

running = True
paused = True

click_type = 'left' #default clickoption

def on_press(key):
    global running, paused, delay, click_type

#Option Keys
    if key == resume:
        delay = float(input('Enter the delay in seconds: ')) #Delay input
        print("New Delay = " + str(delay))
        click_type = input('Enter the button u want to click with(left , right or write the button. Example : space , capslock): ') #Click_type input
        print("Click type set to " + click_type)
        paused = False
        print("Resumed")

    elif key == pause_key:
        paused = True
        print("Paused")

    elif key == exit_key:
        running = False

    elif key == pdelay:
        delay += 0.1
        print("Delay increased \n New Delay =" + str(delay))

    elif key == mdelay:
        delay -= 0.1
        print("Delay decreased \n New Delay =" + str(delay))

#Displayed things if the app opened
def display_controls():
    print(" --- Better Autoclicker by IceDah ---\n")
    print("-----------------------------------------------------")
    print(" - Settings: ")
    print("\t delay = " + str(delay) + ' sec' + '\n')
    print("\t click type = " + click_type + '\n')
    print("-----------------------------------------------------")
    print(" - Controls:")
    print("\t F1 = Resume")
    print("\t F2 = Pause")
    print("\t F3 = Exit")
    print("\t F4 = Plus 0.1 Delay")
    print("\t F5 = Minus 0.1 Delay")
    print("-----------------------------------------------------")
    print('Press F1 to start')

#Listen key press and loops autoclicker
def main():
    lis = Listener(on_press=on_press)
    lis.start()

#Click_type options
    display_controls()
    while running:
        if not paused:
            if click_type == 'left':
                pyautogui.click(button='left')
            elif click_type == 'right':
                pyautogui.click(button='right')
            else:
                pyautogui.press(click_type)

            pyautogui.PAUSE = delay      

    lis.stop()


if __name__ == "__main__":
    main()
