from src.infra.win32.mouse_device import MouseDevice
from src.infra.win32.keyboard_device import KeyboardDevice
from src.use_cases.attack_use_case import AttackUseCase
from src.use_cases.collect_dropped_item_use_case import CollectDroppedItemUseCase
from src.use_cases.fill_potions_use_case import FillPotionsUseCase
from src.use_cases.rebuff_use_case import RebuffUseCase
from src.infra.queue.actions_queue import ActionsQueue
from typing import cast

from src.use_cases.use_potion_use_case import UsePotionUseCase

class DependencyProvider:
    """
    A class to provide dependencies for the application.
    This class is a singleton, ensuring that only one instance exists throughout the application.
    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DependencyProvider, cls).__new__(cls)
            cls._instance._initialize_dependencies()
        return cls._instance

    def _initialize_dependencies(self):
        self.dependencies: dict[str, object] = {}

    def _get_dependency(self, name: str) -> object | None:
        return self.dependencies.get(name)

    def _set_dependency(self, name: str, dependency: object):
        self.dependencies[name] = dependency

    def get_keyboard_device(self) -> KeyboardDevice:
        """
        Set the keyboard device dependency.
        This method should be implemented to set the keyboard device.
        """
        dep = self._get_dependency('keyboard_device')
        if dep is not None:
            return cast(KeyboardDevice, dep)
        
        keyboard_device = KeyboardDevice()

        self._set_dependency('keyboard_device', keyboard_device)

        return keyboard_device

    def get_mouse_device(self) -> MouseDevice:
        """
        Get the mouse device dependency.
        This method should be implemented to get the mouse device.
        """

        dep = self._get_dependency('mouse_device')
        if dep is not None:
            return cast(MouseDevice, dep)
        
        mouse_device = MouseDevice(speed=15) 
    
        self._set_dependency('mouse_device', mouse_device)

        return mouse_device

    def get_rebuff_use_case(self) -> RebuffUseCase:
        """
        Get the rebuff use case dependency.
        :param rebuff_use_case: The rebuff use case instance to get.
        """

        dep = self._get_dependency('rebuff_use_case')
        if dep is not None:
            return cast(RebuffUseCase, dep)
        
        use_case = RebuffUseCase(self.get_keyboard_device(),
                                 self.get_mouse_device())
    
        self._set_dependency('rebuff_use_case', use_case)

        return use_case 
    
    def get_fill_potions_use_case(self) -> FillPotionsUseCase:
        """
        Get the fill potions use case dependency.
        :param fill_potions_use_case: The fill potions use case instance to get.
        """

        dep = self._get_dependency('fill_potions_use_case')
        if dep is not None:
            return cast(FillPotionsUseCase, dep)

        use_case = FillPotionsUseCase(self.get_keyboard_device(),
                                      self.get_mouse_device())

        self._set_dependency('fill_potions_use_case', use_case)

        return use_case

    def get_attack_use_case(self) -> AttackUseCase:
        """
        Get the attack use case dependency.
        :param attack_use_case: The attack use case instance to get.
        """

        dep = self._get_dependency('attack_use_case')
        if dep is not None:
            return cast(AttackUseCase, dep)

        use_case = AttackUseCase(self.get_keyboard_device(),
                                 self.get_mouse_device())

        self._set_dependency('attack_use_case', use_case)

        return use_case
    
    def get_use_potion_use_case(self) -> UsePotionUseCase:
        """
        Get the use potion use case dependency.
        :param use_potion_use_case: The use potion use case instance to get.
        """

        dep = self._get_dependency('use_potion_use_case')
        if dep is not None:
            return cast(UsePotionUseCase, dep)

        use_case = UsePotionUseCase(self.get_keyboard_device())

        self._set_dependency('use_potion_use_case', use_case)

        return use_case
    
    def get_collect_dropped_item_use_case(self) -> CollectDroppedItemUseCase:
        """
        Get the collect dropped item use case dependency.
        :param collect_dropped_item_use_case: The collect dropped item use case instance to get.
        """

        dep = self._get_dependency('collect_dropped_item_use_case')
        if dep is not None:
            return cast(CollectDroppedItemUseCase, dep)

        use_case = CollectDroppedItemUseCase(self.get_keyboard_device(),
                                             self.get_mouse_device())

        self._set_dependency('collect_dropped_item_use_case', use_case)

        return use_case

    def get_actions_queue(self) -> ActionsQueue:
        """
        Get the actions queue dependency.
        This method should be implemented to get the actions queue.
        """
        dep = self._get_dependency('priority_queue')
        if dep is not None:
            return cast(ActionsQueue, dep)

        actions_queue = ActionsQueue()

        self._set_dependency('priority_queue', actions_queue)

        return actions_queue