from pynput import keyboard
from time import sleep

class KeyInput():

    def __init__(self):
        self.status = True
        self.key_stroke = ''
        self.listener = keyboard.Listener(on_release=self.key_input)
        self.listener.start()


    def key_input(self,key):
        self.key_stroke = key.char
        self.status = False
        print(key.char)


    def grab_keystroke(self):
        while self.status:
            continue
        self.status = True
        return self.key_stroke

if __name__ == '__main__':

    foo = KeyInput()
    bar = foo.grab_keystroke()
    zed = foo.grab_keystroke()
    tau = foo.grab_keystroke()
