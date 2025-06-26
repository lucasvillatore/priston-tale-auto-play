import math
import win32api
import win32con
import time
import random

class MouseDevice():
    def __init__(self, min_delay:float=0.005, max_delay:float=0.015, speed:int=10):
        self.min_delay = min_delay
        self.max_delay = max_delay
        self.speed = speed

    def right_click(self):
        """Realiza um clique com o botão direito do mouse."""
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0) # type: ignore
        time.sleep(self.min_delay)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0) # type: ignore

    def left_click(self):
        """Realiza um clique com o botão esquerdo do mouse."""
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0) # type: ignore
        time.sleep(self.min_delay)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0) # type: ignore

    def go_to_area(self, area_x: tuple[int, int], area_y: tuple[int, int]):
        """Move para um ponto aleatório dentro da área definida."""
        x = random.randint(area_x[0], area_x[1])
        y = random.randint(area_y[1], area_y[1])

        self.go_to(x, y)

    def go_to(self, x: int, y: int):
        """Move o cursor do mouse para a posição (x, y) com movimento suave."""
        start_x, start_y = win32api.GetCursorPos()

        delta_x = x - start_x
        delta_y = y - start_y

        distance = math.hypot(delta_x, delta_y)
        steps = int(distance / self.speed)
        if steps == 0:
            win32api.SetCursorPos((x, y))
            return

        def generate_bezier_curve(start_x: int, start_y: int, end_x: int, end_y: int):
            """Gera pontos de uma curva Bézier aleatória."""
            cp1_x = start_x + (end_x - start_x) * random.uniform(0.3, 0.7) + random.uniform(-100, 100)
            cp1_y = start_y + (end_y - start_y) * random.uniform(0.3, 0.7) + random.uniform(-100, 100)

            def bezier(t: float) -> tuple[int, int]:
                x = (1 - t) ** 2 * start_x + 2 * (1 - t) * t * cp1_x + t ** 2 * end_x
                y = (1 - t) ** 2 * start_y + 2 * (1 - t) * t * cp1_y + t ** 2 * end_y
                return int(x), int(y)

            return bezier

        bezier = generate_bezier_curve(start_x, start_y, x, y)

        def ease(t: float) -> float:
            """Função de easing para suavizar o movimento do mouse."""
            return t * t * (3 - 2 * t)

        for i in range(steps + 1):
            t = i / steps
            t_eased = ease(t)
            new_x, new_y = bezier(t_eased)

            win32api.SetCursorPos((new_x, new_y))
            time.sleep(random.uniform(self.min_delay, self.max_delay))

        win32api.SetCursorPos((x, y))
