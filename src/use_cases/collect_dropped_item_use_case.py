from src.infra.win32 import keys
from src.infra.win32.keyboard_device import KeyboardDevice
from src.infra.win32.mouse_device import MouseDevice
from src.use_cases.use_case_base import UseCaseBase


class CollectDroppedItemUseCase(UseCaseBase):
    """
    Use case for collecting dropped items in the game.
    This class handles the sequence of actions related to collecting dropped items.
    """

    priority = 1000

    def __init__(self, keyboard: KeyboardDevice, mouse: MouseDevice):
        self.keyboard = keyboard
        self.mouse = mouse

    def execute(self, item_position: tuple[int, int]) -> None:
        """
        Execute the collect dropped item action.
        :param item_position: The position of the item to be collected.
        """
        print(f"Collecting item at position: {item_position}")
        self.keyboard.hold(keys.VK_A)
        self.mouse.go_to(item_position[0], item_position[1])
        self.mouse.left_click()
        self.keyboard.release(keys.VK_A)