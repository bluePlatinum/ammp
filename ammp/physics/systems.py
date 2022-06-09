

class SystemDisplay:
    """
    Creates a System intended for displaying static and semistatic
    constellations.

    :param bodies: The bodies which are part of the system. Passed as a list
        of body objects.
    :type bodies: list
    """
    def __init__(self, bodies):
        self.bodies = bodies
