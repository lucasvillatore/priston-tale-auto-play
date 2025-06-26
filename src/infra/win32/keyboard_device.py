import win32api
import win32con
import time

class KeyboardDevice:
    def __init__(self, delay_between_keys:float=0.05):
        self.delay = delay_between_keys

    def press(self, hex_code_key: int):
        """Pressiona e solta a tecla rapidamente."""
        win32api.keybd_event(hex_code_key, 0, 0, 0)  # type: ignore # Key down
        time.sleep(self.delay)
        win32api.keybd_event(hex_code_key, 0, win32con.KEYEVENTF_KEYUP, 0)  # type: ignore # Key up
        time.sleep(self.delay)

    def hold(self, hex_code_key: int):
        """Segura a tecla (key down)."""
        win32api.keybd_event(hex_code_key, 0, 0, 0) # type: ignore
        time.sleep(self.delay)

    def release(self, hex_code_key: int):
        """Solta a tecla (key up)."""
        win32api.keybd_event(hex_code_key, 0, win32con.KEYEVENTF_KEYUP, 0) # type: ignore
        time.sleep(self.delay)

    def hold_with_sequence(self, hold_key: int, sequence: list[int]):
        """
        Segura uma tecla enquanto executa uma sequência de teclas.
        :param hold_key: tecla a ser segurada
        :param sequence: lista de teclas a serem pressionadas
        """
        self.hold(hold_key)
        for key in sequence:
            self.press(key)
        self.release(hold_key)