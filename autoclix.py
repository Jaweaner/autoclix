import os

x = input('Install modules? Y/N > ')

if x == 'y' or x == 'Y':
    try:

        
        os.system("pip install pynput")
        os.system("pip install colorama")
    except:
        pass
else:
    pass

import time 
import threading 
from pynput.mouse import Button, Controller 
from pynput.keyboard import Listener, KeyCode 
from colorama import Fore
import os

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

r = Fore.RED
rs = Fore.RESET
g = Fore.GREEN
cls()
print(f'''{r}
 $$$$$$\              $$\                $$$$$$\  $$\ $$\           
$$  __$$\             $$ |              $$  __$$\ $$ |\__|          
$$ /  $$ |$$\   $$\ $$$$$$\    $$$$$$\  $$ /  \__|$$ |$$\ $$\   $$\ 
$$$$$$$$ |$$ |  $$ |\_$$  _|  $$  __$$\ $$ |      $$ |$$ |\$$\ $$  |
$$  __$$ |$$ |  $$ |  $$ |    $$ /  $$ |$$ |      $$ |$$ | \$$$$  / 
$$ |  $$ |$$ |  $$ |  $$ |$$\ $$ |  $$ |$$ |  $$\ $$ |$$ | $$  $$<  
$$ |  $$ |\$$$$$$  |  \$$$$  |\$$$$$$  |\$$$$$$  |$$ |$$ |$$  /\$$\ 
\__|  \__| \______/    \____/  \______/  \______/ \__|\__|\__/  \__|
[github.com/Jawiner/autoclix]

      {g}[-] Press "-" to start/stop{r}
      [+] Press "+" to exit
                                                                    {rs}''')

delay = 0.000000001  
button = Button.left
start_stop_key = KeyCode(char='-') 
stop_key = KeyCode(char='+') 

class ClickMouse(threading.Thread): 
	
    def __init__(self, delay, button): 
        super(ClickMouse, self).__init__() 
        self.delay = delay 
        self.button = button 
        self.running = False
        self.program_running = True

    def start_clicking(self): 
        self.running = True

    def stop_clicking(self): 
        self.running = False

    def exit(self): 
        self.stop_clicking() 
        self.program_running = False

    def run(self): 
        while self.program_running: 
            while self.running: 
                mouse.click(self.button) 
                end_time = time.time() + self.delay
                while time.time() < end_time:
                    pass
            time.sleep(0.1) 

mouse = Controller() 
click_thread = ClickMouse(delay, button) 
click_thread.start() 

def on_press(key): 
    if key == start_stop_key: 
        if click_thread.running: 
            click_thread.stop_clicking() 
        else: 
            click_thread.start_clicking() 
    elif key == stop_key: 
        click_thread.exit() 
        listener.stop() 

with Listener(on_press=on_press) as listener: 
    listener.join()
