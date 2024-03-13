# Commands for the Stata Do-File Editor
os: windows
app: stata
win.title: Do-file Editor
-
do this: key(ctrl-d)

do line: 
    edit.select_line()
    key(ctrl-d)

do (all | file): 
    edit.select_all()
    key(ctrl-d)

do way up: 
    edit.extend_file_start()
    key(ctrl-d)

do way down: 
    edit.extend_file_end()
    key(ctrl-d)
