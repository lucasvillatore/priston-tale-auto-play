import time
from src.infra.win32.keyboard_device import KeyboardDevice
from src.infra.win32.mouse_device import MouseDevice
from src.use_cases.use_case_base import UseCaseBase

class RebuffUseCase(UseCaseBase):
    """
    Use case for rebuffing in the game.
    This use case handles the logic for using buffs.
    """

    priority = 20

    def __init__(self, keyboard: KeyboardDevice, mouse: MouseDevice):
        self.keyboard = keyboard
        self.mouse = mouse

    def execute(self, buff):
        """
        Execute the rebuffing logic.
        :param buffs: List of buffs to use.
        """
        print(f"Using buff: {buff}")
        self.keyboard.press(buff)
        self.mouse.right_click()
        time.sleep(3)