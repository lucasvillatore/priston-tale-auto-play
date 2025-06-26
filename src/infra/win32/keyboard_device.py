import win32api
import win32con
import time

class KeyboardDevice:
    def __init__(self, delay_between_keys=0.05):
        self.delay = delay_between_keys

    def press(self, hexKeyCode):
        """Pressiona e solta a tecla rapidamente."""
        win32api.keybd_event(hexKeyCode, 0, 0, 0)  # Key down
        time.sleep(self.delay)
        win32api.keybd_event(hexKeyCode, 0, win32con.KEYEVENTF_KEYUP, 0)  # Key up
        time.sleep(self.delay)

    def hold(self, hexKeyCode):
        """Segura a tecla (key down)."""
        win32api.keybd_event(hexKeyCode, 0, 0, 0)
        time.sleep(self.delay)

    def release(self, hexKeyCode):
        """Solta a tecla (key up)."""
        win32api.keybd_event(hexKeyCode, 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(self.delay)

    def hold_with_sequence(self, hold_key, sequence):
        """
        Segura uma tecla enquanto executa uma sequência de teclas.
        :param hold_key: tecla a ser segurada
        :param sequence: lista de teclas a serem pressionadas
        """
        self.hold(hold_key)
        for key in sequence:
            self.press(key)
        self.release(hold_key)