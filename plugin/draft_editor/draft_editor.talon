user.draft_editor_running: True
not tag: user.draft_editor_app_focused
-

draft [here]: 
    user.draft_editor_open()
    mode.enable("command")
    mode.enable("dictation")
    user.code_clear_language_mode()
    mode.disable("user.gdb")

draft all:
    edit.select_all()
    user.draft_editor_open()
    mode.enable("command")
    mode.enable("dictation")
    user.code_clear_language_mode()
    mode.disable("user.gdb")

draft line:
    edit.select_line()
    user.draft_editor_open()
    mode.enable("command")
    mode.enable("dictation")
    user.code_clear_language_mode()
    mode.disable("user.gdb")

draft top:
    edit.extend_file_start()
    user.draft_editor_open()
    mode.enable("command")
    mode.enable("dictation")
    user.code_clear_language_mode()
    mode.disable("user.gdb")

draft bottom:
    edit.extend_file_end()
    user.draft_editor_open()
    mode.enable("command")
    mode.enable("dictation")
    user.code_clear_language_mode()
    mode.disable("user.gdb")

# draft submit: user.draft_editor_paste_last()
