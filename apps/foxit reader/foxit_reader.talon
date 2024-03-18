app: foxit_reader
-
tag(): user.tabs
tag(): user.pages

tab close all: key(ctrl-shift-w)

[page] rotate right: key("shift-ctrl-keypad_equals")
[page] rotate left: key("shift-ctrl-keypad_minus")

go back: key(alt-left)

hunt this: 
    edit.copy()
    sleep(25ms)
    edit.find("")
    sleep(25ms)
    edit.paste()
hunt [this] (pace | paste):
    edit.find("")
    sleep(25ms)
    edit.paste()
(hunt [here] | hunter) <user.text>: 
    edit.find(text)
    key(enter)
next one: edit.find_next()
(last | previous) one: 
    key(shift:down)   
    key(f3)
    key(shift:up)
# hunt next: user.find_next()
# hunt previous: user.find_previous()