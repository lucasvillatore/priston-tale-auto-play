from src.infra.win32.mouse_device import MouseDevice
from src.infra.win32.keyboard_device import KeyboardDevice
from src.use_cases.fill_potions_use_case import FillPotionsUseCase
from src.use_cases.rebuff_use_case import RebuffUseCase
from src.infra.queue.actions_queue import ActionsQueue

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
        self.dependencies = {}

    def _get_dependency(self, name):
        return self.dependencies.get(name)

    def _set_dependency(self, name, dependency):
        self.dependencies[name] = dependency

    def get_keyboard_device(self):
        """
        Set the keyboard device dependency.
        This method should be implemented to set the keyboard device.
        """
        if (self._get_dependency('keyboard_device') is not None):
            return self._get_dependency('keyboard_device')
        
        keyboard_device = KeyboardDevice()

        self._set_dependency('keyboard_device', keyboard_device)

        return keyboard_device

    def get_mouse_device(self):
        """
        Get the mouse device dependency.
        This method should be implemented to get the mouse device.
        """

        if (self._get_dependency('mouse_device') is not None):
         return self._get_dependency('mouse_device')
        
        mouse_device = MouseDevice(speed=15) 
    
        self._set_dependency('mouse_device', mouse_device)

        return mouse_device

    def get_rebuff_use_case(self):
        """
        Get the rebuff use case dependency.
        :param rebuff_use_case: The rebuff use case instance to get.
        """

        if (self._get_dependency('rebuff_use_case') is not None):
            return self._get_dependency('rebuff_use_case')
        
        use_case = RebuffUseCase(self.get_keyboard_device(),
                                 self.get_mouse_device())
    
        self._set_dependency('rebuff_use_case', use_case)

        return use_case 
    
    def get_fill_potions_use_case(self):
        """
        Get the fill potions use case dependency.
        :param fill_potions_use_case: The fill potions use case instance to get.
        """

        if (self._get_dependency('fill_potions_use_case') is not None):
            return self._get_dependency('fill_potions_use_case')

        use_case = FillPotionsUseCase(self.get_keyboard_device(),
                                      self.get_mouse_device())

        self._set_dependency('fill_potions_use_case', use_case)

        return use_case
    
    def get_actions_queue(self):
        """
        Get the actions queue dependency.
        This method should be implemented to get the actions queue.
        """
        if (self._get_dependency('priority_queue') is not None):
            return self._get_dependency('priority_queue')

        actions_queue = ActionsQueue()

        self._set_dependency('priority_queue', actions_queue)

        return actions_queue