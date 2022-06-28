class System:
    """
    The parent class for all systems.
    """
    def __init__(self):
        """
        Constructor method
        """
        pass

    def draw_sv(self, sv_graphic):
        """
        This method draws the system for the SystemViewerGraphic QWidget.
        It needs to be specifically implemented by the child classes.


        :param sv_graphic: the SystemViewerGrapic QWidget
        :type sv_graphic: SystemViewerGraphic
        :return: None
        """
        msg = 'The draw_sv method was not implemented by the child class.'
        raise NotImplementedError(msg)


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
