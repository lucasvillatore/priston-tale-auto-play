import time
from src.infra.win32 import keys
from src.infra.win32.keyboard_device import KeyboardDevice
from src.infra.win32.mouse_device import MouseDevice
from src.use_cases.use_case_base import UseCaseBase


class FillPotionsUseCase(UseCaseBase):
    """= managing the potions actions in the game.
    This class handles the sequence of actions related to fill potions.
    """

    priority = 1

    def __init__(self, keyboard: KeyboardDevice, mouse: MouseDevice):
        self.keyboard = keyboard
        self.mouse = mouse

    from typing import Any

    def execute(self, *args: Any, **kwargs: Any) -> None:
        """
        Execute the fill potions action.
        """
        print("Executing fill potion use case")
        self._open_inventory() \
            ._fill_first_potion() \
            ._fill_second_potion() \
            ._fill_third_potion() \
            ._close_inventory()
        
    def _open_inventory(self):
        print("Opening inventory")
        
        self.keyboard.press(keys.VK_V)
        time.sleep(0.5)

        return self
    
    def _close_inventory(self):
        print("Closing inventory")
        
        self.keyboard.press(keys.VK_V)
        time.sleep(0.5)

        return self

    def _fill_first_potion(self):
        print("Filling first potion")
        area_x = (25, 41)
        area_y = (877, 896)

        self.mouse.go_to_area(area_x, area_y)
        self.keyboard.hold_with_sequence(keys.VK_SHIFT, [keys.VK_1])
        time.sleep(0.5)
        
        return self
    
    def _fill_second_potion(self):
        print("Filling second potion")
        area_x = (47, 64)
        area_y = (877, 896)

        self.mouse.go_to_area(area_x, area_y)
        self.keyboard.hold_with_sequence(keys.VK_SHIFT, [keys.VK_2])
        time.sleep(0.5)

        return self

    def _fill_third_potion(self):
        print("Filling third potion")
        area_x = (69, 86)
        area_y = (877, 896)

        self.mouse.go_to_area(area_x, area_y)
        self.keyboard.hold_with_sequence(keys.VK_SHIFT, [keys.VK_3])
        time.sleep(0.5)

        return self
    
