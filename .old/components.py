from datetime import datetime
import asyncio
from urwid import Text, SimpleListWalker as ListWalker, Pile, SolidFill, Frame, MainLoop, AsyncioEventLoop, ExitMainLoop, Edit, ListBox, AttrMap, Divider, Filler, Columns
import styles as style

class Container(Pile):
    def __init__(self, widget_list=[], focus_item=None):
        super(Container, self).__init__(widget_list, focus_item)

    def append_child(self, element):
        super(Container, self).contents.append((element, self.options()))

class Window:
    def __init__(self, body=SolidFill(), header=None, footer=None, focus_part=None, unhandled_input=None, palette=None):
        self.document = Frame(body, header, footer, focus_part)
        self.loop = MainLoop(
            self.document,
            palette,
            event_loop=AsyncioEventLoop(loop=asyncio.get_event_loop()),
            unhandled_input=unhandled_input
        )
        self.loop.screen.set_terminal_properties(colors=256)
        self.body = body
        self.footer = footer
        self.header = header

    def run(self):
        self.loop.run()

    def exit(self):
        raise ExitMainLoop()

    def set_state(self, key, value):
        self.state[key] = value

    def get_state(self, key):
        try:
            return self.state[key]
        except KeyError:
            return None

class TextInput(Edit):
    def __init__(self, caption='', edit_text='', multiline=False, align='left', wrap='space', allow_tab=False, edit_pos=None, layout=None, mask=None, on_change=None, on_enter=None, on_key_press=None, on_esc=None):
        super(TextInput, self).__init__(caption, edit_text, multiline, align, wrap, allow_tab, edit_pos, layout, mask)
        self.on_change = on_change
        self.on_enter = on_enter
        self.on_key_press = on_key_press
        self.on_esc = on_esc

    def keypress(self, size, key):
        if self.on_key_press != None:
            key = self.on_key_press(size, key)
        if key != None:
            super(TextInput, self).keypress(size, key)
        if self.on_change != None:
            result = self.on_change(self.edit_text, key)
            if result != None: self.edit_text = result
        if self.on_enter != None and key == 'enter' and self.on_enter(self.edit_text) != None:
            self.edit_text = ''
        if self.on_esc != None and key == 'esc' and self.on_esc(self.edit_text) != None:
            self.edit_text = ''

class Error(Text):
    def __init__(self, markup, align='left', wrap='space', layout=None):
        super(Error, self).__init__('error: ' + markup, align, wrap, layout)

class Warn(Text):
    def __init__(self, markup, align='left', wrap='space', layout=None):
        super(Warn, self).__init__('warning: ' + markup, align, wrap, layout)

class Info(Text):
    def __init__(self, markup, align='left', wrap='space', layout=None):
        super(Info, self).__init__('info: ' + markup, align, wrap, layout)

class List(ListBox):
    def __init__(self, body=ListWalker([]), auto_scroll=None):
        super(List, self).__init__(body)
        self.auto_scroll = auto_scroll

    def append_child(self, element):
        self.body.append(element)
        if self.auto_scroll != None:
            super(List, self).keypress((119, 11), self.auto_scroll)

    def scroll_down(self):
        super(List, self).keypress((119, 11), 'end')

class Message(Columns):
    def __init__(self, message, text=None):
        date = datetime.fromtimestamp(message['date']).strftime('%H:%M')
        text = message['text'] or '' if text is None else text

        if message['outgoing'] or message['from_user']['is_self'] is True:
            super(Message, self).__init__([
                ('weight', 10, Divider()),
                ('pack', Text(text, 'right')),
                ('pack', Text('  ' + str(date), 'right')) ])
        else:
            super(Message, self).__init__([
                ('pack', Text(str(date) + '  ', 'left')),
                ('pack', AttrMap(Text(text), 'message')),
                ('weight', 10, Divider()) ])
        

class StatusLine(AttrMap):
    def __init__(self, attr_map=style.STATUS_LINE, focus_map=style.STATUS_LINE_FOCUSED):
        self.left_column = Text('')
        self.center_column = Text('')
        self.right_column = Text('')
        self.body = Columns([ self.left_column, self.center_column, self.right_column ], min_width=0)
        super(StatusLine, self).__init__(self.body, attr_map, focus_map)

