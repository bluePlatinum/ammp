

class Rigidbody:
    """
        This class is used to handle basic rigidbody Physics. (No collisions
        though)
    """
    def __init__(self, position, rotation):
        """
            Constructor method
        """
        self.position = position
        self.rotation = rotation
