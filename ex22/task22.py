from pynput.mouse import Controller, Listener, Button
from pynput import mouse, keyboard
import time
import json
import pprint

device = input()

m = list()

def on_move(x, y):
    print("x and y", (x,y))
    m.append({"Type": "EV_REL", "value": (x,y)}) 
    with open('C:\dev\Python\POSU\ex22\\task22.json', 'w') as f:
        json.dump(m,f)             

def on_click(x, y, button, pressed):
    print('{0} at {1} lalala {2}'.format('Pressed' if pressed else 'Released',(x, y),button))
    if not pressed:
        # Stop listener
        return False

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format(
        'down' if dy < 0 else 'up',
        (x, y)))

if device == "m":
    # Collect events until released
    with mouse.Listener(
        on_move = on_move,
        on_click = on_click,
        on_scroll=on_scroll) as listener:
        listener.join()
        

def on_press(key):
    try:        
        m.append({"Type": 'EV_KEY', "code": 'KEY_{0}'.format(key),"state": 1}) 
        with open('C:\dev\Python\POSU\ex22\\task22.json', 'w') as f:
            json.dump(m,f)             
        print('alphanumeric key {0} pressed'.format(key))
    except AttributeError:
        print('special key {0} pressed'.format(key))

def on_release(key):    
    # m.append({"Type": "EV_KEY", "code": format(key), "state": 0}) 
    m.append({"Type": "EV_KEY", "code": 'KEY_{0}'.format(key),"state": 0}) 
    with open('C:\dev\Python\POSU\ex22\\task22.json', 'w') as f:
            json.dump(m,f)
    print(key)                     
    print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        # Stop listener 
        return False    

if device == "k":
    # Collect events until released
    with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
        listener.join()


with open('C:\dev\Python\POSU\ex22\\task22.json') as json_file:
    data = json.load(json_file)

pprint.pprint(data)    