# Scripts to run Stata code from anywhere by copy-pasting into an open instance of the Stata do-file editor
os: windows
code.language: stata
not win.title: Do-file Editor
-
do this:
    edit.copy()
    user.stata_run_do_editor()

do line:
    edit.select_line()
    edit.copy()
    user.stata_run_do_editor()

do (all | file):
    edit.select_all()
    edit.copy()
    user.stata_run_do_editor()

do way up:
    edit.extend_file_start()
    edit.copy()
    user.stata_run_do_editor()

do way down:
    edit.extend_file_end()
    edit.copy()
    user.stata_run_do_editor()
