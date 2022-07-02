import random


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


class SystemDisplay(System):
    """
    Creates a System intended for displaying static and semistatic
    constellations.

    :param bodies: The bodies which are part of the system. Passed as a list
        of body objects.
    :type bodies: list
    """
    def __init__(self, bodies):
        super().__init__()
        self.bodies = bodies

    def draw_sv(self, sv_graphic):
        """
        Draws the system for the SystemViewerGraphic widget by plotting every
        body with its position and size.

        :param sv_graphic: the SystemViewerGraphic widget
        :type sv_graphic: SystemViewerGraphic
        :return: None
        """
        for body in self.bodies:
            # there is no scaling between physical size and display size
            # implemented so this will definitely change, but for now it is
            # a placeholder
            try:
                size = body.size
            except AttributeError:
                size = 1

            color = (random.random(), random.random(), random.random())
            sv_graphic.axes.plot(*body.position, marker='o', markersize=size,
                                 color=color)
