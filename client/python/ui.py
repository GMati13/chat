import asyncio
import urwid

class Container(urwid.Pile):
    def __init__(self, widget_list=[], focus_item=None):
        super(Container, self).__init__(widget_list, focus_item)

    def append_child(self, element):
        super(Container, self).contents.append((element, self.options()))

class Window:
    def __init__(self, vertical_align='top', unhandled_input=None, palette=None):
        placeholder = urwid.SolidFill()
        loop = urwid.MainLoop(
                placeholder,
                palette,
                event_loop=urwid.AsyncioEventLoop(loop=asyncio.get_event_loop()),
                unhandled_input=unhandled_input)
        loop.screen.set_terminal_properties(colors=256)
        loop.widget = urwid.AttrMap(placeholder, 'body')
        loop.widget.original_widget = urwid.Filler(Container(), vertical_align)
        body = loop.widget.base_widget

        self.loop = loop
        self.body = body

    def run(self):
        self.loop.run()

    def exit(self):
        raise urwid.ExitMainLoop()

    def set_state(self, key, value):
        self.state[key] = value

    def get_state(self, key):
        try:
            return self.state[key]
        except KeyError:
            return None

class TextInput(urwid.Edit):
    def __init__(self, caption='', edit_text='', multiline=False, align='left', wrap='space', allow_tab=False, edit_pos=None, layout=None, mask=None, on_change=None, on_enter=None, on_key_press=None, on_esc=None):
        super(TextInput, self).__init__(caption, edit_text, multiline, align, wrap, allow_tab, edit_pos, layout, mask)
        self.on_change = on_change
        self.on_enter = on_enter
        self.on_key_press = on_key_press
        self.on_esc = on_esc

    def keypress(self, size, key):
        if self.on_key_press != None:
            super(TextInput, self).keypress(size, self.on_key_press(size, key))
        else:
            super(TextInput, self).keypress(size, key)
        if self.on_change != None:
            result = self.on_change(self.edit_text, key)
            if result != None: self.edit_text = result
        if self.on_enter != None and key == 'enter' and self.on_enter(self.edit_text) != None:
            self.edit_text = ''
        if self.on_esc != None and key == 'esc' and self.on_esc(self.edit_text) != None:
            self.edit_text = ''

class Error(urwid.Text):
    def __init__(self, markup, align='left', wrap='space', layout=None):
        super(Error, self).__init__('error: ' + markup, align, wrap, layout)

class Warn(urwid.Text):
    def __init__(self, markup, align='left', wrap='space', layout=None):
        super(Warn, self).__init__('warning: ' + markup, align, wrap, layout)

class Info(urwid.Text):
    def __init__(self, markup, align='left', wrap='space', layout=None):
        super(Info, self).__init__('info: ' + markup, align, wrap, layout)
