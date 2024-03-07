mode: command
mode: dictation
-
customize {user.talon_settings_csv}:
    user.edit_text_file(talon_settings_csv)
    sleep(1500ms)
    edit.file_end()
    edit.line_insert_down()