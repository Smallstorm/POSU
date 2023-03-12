FILENAME = 'key_records.txt'
import keyboard

def print_pressed_keys(e):
    global FILENAME
    f = open(FILENAME, 'a')
    f.write(f"Была {'нажата' if e.event_type == 'down' else 'отпущена'} кнопка {e.name}\n")
    f.close()

keyboard.hook(print_pressed_keys)
keyboard.wait()