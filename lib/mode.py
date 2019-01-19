
class ModeError(Exception):
    def __init__(self, message):
        super(ModeError, self).__init__(message)

class Mode():
    modes = [
        'NORMAL',
        'COMMAND',
        'MESSAGE',
        'DIALOGS',
        'CHAT'
    ]

    def __init__(self, mode=None, on_toggle=None, on_init=None):
        if mode is None:
            mode = self.modes[0]
        mode = mode.upper()
        self.__check_mode(mode)
        self.current_mode = mode
        self.previous_mode = mode
        self.on_toggle = on_toggle
        self.on_init = on_init
        self.__init = False

    def init(self):
        self.__init = True
        if self.on_init is not None:
            self.on_init(self.current_mode)

    def toggle_mode(self, mode):
        self.__check_init()
        mode = mode.upper()
        self.__check_mode(mode)
        self.previous_mode = self.current_mode
        if self.on_toggle is not None:
            self.on_toggle(self.previous_mode, mode)
        self.current_mode = mode

    def __check_init(self):
        if self.__init is False:
            raise ModeError('mode is not initialized. Use mode.init()')

    def __check_mode(self, mode):
        if mode not in self.modes:
            raise ModeError('mode can not be \'{m}\''.format(m=mode))
