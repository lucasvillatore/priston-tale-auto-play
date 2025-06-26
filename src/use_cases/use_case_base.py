class UseCaseBase:
    """
    Base class for use cases.
    """

    priority = 0
    def execute(self, *args, **kwargs):
        """
        Execute the use case logic.
        This method should be overridden by subclasses.
        """
        raise NotImplementedError("Subclasses must implement this method.")