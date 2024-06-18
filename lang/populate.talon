mode: command
code.language: /./
-
# At the ability to quickly add things to/edit the respective lists

customize {user.populate}:
    user.edit_code_list(populate)
    sleep(1500ms)
    edit.file_end()
    edit.line_insert_down()

add {user.populate} this:
    edit.copy()
    user.edit_code_list(populate)
    sleep(1500ms)
    edit.file_end()
    edit.line_insert_down()
    edit.paste()

abracadabra: insert("abracadabra")