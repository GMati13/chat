from urwid import *
import src.templates.message as msg_template
import src.formatter as formatter

class EditText(Edit):
    def __init__(self, caption='', edit_text='', multiline=False, align='left', wrap='space', allow_tab=False, edit_pos=None, layout=None, mask=None, on_change=None, on_enter=None, on_key_press=None, on_esc=None, on_click=None):
        super(EditText, self).__init__(caption, edit_text, multiline, align, wrap, allow_tab, edit_pos, layout, mask)
        self.on_change = on_change
        self.on_enter = on_enter
        self.on_key_press = on_key_press
        self.on_esc = on_esc
        self.on_click = on_click

    def keypress(self, size, key):
        if self.on_key_press is not None:
            key = self.on_key_press(key, self)
        if self.on_enter is not None and key == 'enter':
            self.on_enter(self.edit_text, self)
        if self.on_esc is not None and key == 'esc':
            self.on_esc(self.edit_text, self)
        if key is not None:
            super(EditText, self).keypress(size, key)
            if self.on_change is not None:
                result = self.on_change(key, self)
                if result is not None:
                    self.edit_text = result

    def mouse_event(self, size, event, button, x, y, focus):
        if self.on_click is not None:
            if self.on_click(event, button, x, y, focus) is False:
                return
        super(EditText, self).mouse_event(size, event, button, x, y, focus)

    def clear(self):
        self.edit_text = ''

class List(ListBox):
    def __init__(self, body=[], on_enter=None, on_key_press=None, on_after_key_press=None, on_esc=None):
        super(List, self).__init__(body)
        self.on_enter = on_enter
        self.on_key_press = on_key_press
        self.on_after_key_press = on_after_key_press
        self.on_esc = on_esc

    def keypress(self, size, key):
        if self.on_key_press is not None:
            key = self.on_key_press(key, self)
        if self.on_enter is not None and key == 'enter':
            self.on_enter(self.focus_position, self)
        if self.on_esc is not None and key == 'esc':
            self.on_esc(self.edit_text, self)
        if key is not None:
            super(List, self).keypress(size, key)
        if self.on_after_key_press is not None:
            key = self.on_after_key_press(key, self)

    def append_child(self, element):
        self.body.append(element)

    def append_childs(self, elements):
        self.body.extend(elements)

    def clear(self):
        self.body = []

    def scroll_down(self):
        super(List, self).keypress((1, 9999), 'end')

    def scroll_up(self):
        super(List, self).keypress((1, 9999), 'home')

    def scroll_page_down(self):
        super(List, self).keypress((1, 11), 'page down')

    def scroll_page_up(self):
        super(List, self).keypress((1, 11), 'page up')

    def scroll_next(self):
        super(List, self).keypress((1, 1), 'down')

    def scroll_prev(self):
        super(List, self).keypress((1, 1), 'up')

class StatusLine(Columns):
    def __init__(self, widget_list=None, dividechars=0, focus_column=None, min_width=1, box_columns=None):
        if widget_list is None:
            self.left_column = Text('')
            self.right_column = Text('', align='right')
            widget_list=[
                self.left_column,
                self.right_column
            ]
        super(StatusLine, self).__init__(widget_list, dividechars, focus_column, min_width, box_columns)

class Message(Text):
    def __init__(self, message, short=False):
        text = ''
        if message['media']:
            text = msg_template.short_media
        else:
            text = str(message['text']).split('\n')[0]
        super(Message, self).__init__(text, align='left', wrap='clip', layout=None)

class Dialog(Columns):
    def __init__(self, dialog):
        widget_list = []
        date = formatter.formate_date(dialog['top_message']['date'])
        if dialog['chat']['type'] == 'private':
            fullname = formatter.formate_name(dialog['chat']['first_name'], dialog['chat']['last_name'])
            widget_list = [
                (24, Text(fullname)),
                (Message(dialog['top_message'])),
                (12, Text(date, align='right'))
            ]
        if dialog['chat']['type'] in ['group', 'channel']:
            widget_list = [
                (24, Text(str(dialog['chat']['title']))),
                (Message(dialog['top_message'])),
                (12, Text(date, align='right'))
            ]
        super(Dialog, self).__init__(widget_list, dividechars=0, focus_column=None, min_width=1, box_columns=None)
