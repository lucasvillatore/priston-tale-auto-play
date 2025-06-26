from src.infra.win32.keyboard_device import KeyboardDevice
from src.use_cases.use_case_base import UseCaseBase


class UsePotionUseCase(UseCaseBase):
    priority = 1

    def __init__(self, keyboard: KeyboardDevice):
        self.keyboard = keyboard

    def execute(self, potion_key: int):
        """
        Execute the use potion logic.
        :param potion_key: The key to be used for using the potion.
        """
        print(f"Using potion with key: {potion_key}")
        self.keyboard.press(potion_key)
