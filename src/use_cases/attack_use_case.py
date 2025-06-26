from src.infra.win32.keyboard_device import KeyboardDevice
from src.infra.win32.mouse_device import MouseDevice
from src.use_cases.use_case_base import UseCaseBase


class AttackUseCase(UseCaseBase):

    priority = 100
    def __init__(self, keyboard: KeyboardDevice, mouse: MouseDevice):
        self.keyboard = keyboard
        self.mouse = mouse

    def execute(self, attack_key: int, position: tuple[int, int]):
        """
        Execute the attack logic.
        :param attack_key: The key to be used for attacking.
        """
        print(f"Executing attack with key: {attack_key}")
        self.keyboard.press(attack_key)
        self.mouse.go_to(position[0], position[1])
        self.mouse.right_click()
        