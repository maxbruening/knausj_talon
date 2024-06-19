mode: command
code.language: /./
-
# At the ability to quickly add things to/edit the respective lists

customize {user.code_tag}:
    user.edit_code_list(code_tag)
    sleep(1500ms)
    edit.file_end()
    edit.line_insert_down()

add {user.code_tag} this:
    edit.copy()
    user.edit_code_list(code_tag)
    sleep(1500ms)
    edit.file_end()
    edit.line_insert_down()
    edit.paste()

abracadabra: insert("abracadabra")