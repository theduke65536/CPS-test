from tkinter import *
import threading
from time import sleep

window_size = '1000x600'
clicks = 0
seconds = int(input('Seconds: >'))

def click():
    global clicks

    if clicks == 0:
        start_time_thread(timer)
    clicks += 1


def timer():
    sleep(seconds)
    print('Times up!\n')
    window.destroy()

def start_time_thread(timer):
    timer = threading.Thread(target=timer, args=())
    timer.start()


def cps_calculator(clicks, seconds):
    return clicks / seconds


window = Tk()
window.geometry(window_size)
window.title('Clicks Per Second Test')
window.config(background='black')

button = Button(window,
                command=click,
                text='Click me to start the test',
                font=('Arial',50,'bold'),
                bg='Grey',
                height='600',
                width='1000',
                activeforeground='Grey'
)
button.pack()
window.mainloop()

cps = cps_calculator(clicks, seconds)
print(f'You clicked {clicks} times\nYou had a cps of {cps}')