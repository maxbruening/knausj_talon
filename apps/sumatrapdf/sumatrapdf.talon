app: sumatrapdf
-
# Set tags
tag(): user.pages
tag(): user.tabs

(tab | file) reload: key(r)

rotate right: key("shift-ctrl-keypad_plus")
rotate left: key("shift-ctrl-keypad_minus")

go back: key(alt-left)
go forward: key(alt-right)

hunt this: 
    edit.copy()
    edit.find("")
    sleep(25ms)
    edit.paste()
hunt [this] (pace | paste):
    edit.find("")
    sleep(25ms)
    edit.paste()
(hunt [here] | hunter) <user.text>: edit.find(text)
next one: edit.find_next()
(last | previous) one: 
    key(shift:down)   
    key(f3)
    key(shift:up)
# hunt next: user.find_next()
# hunt previous: user.find_previous()