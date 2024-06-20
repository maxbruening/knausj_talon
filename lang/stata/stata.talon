# many of the things here could also be useful for working in R or python data science
code.language: stata
-
tag(): user.code_imperative

tag(): user.code_comment_block_c_like
tag(): user.code_comment_block
tag(): user.code_comment_line
tag(): user.code_functions
tag(): user.code_functions_common
tag(): user.code_libraries
tag(): user.code_libraries_gui
tag(): user.code_operators_array
tag(): user.code_operators_assignment
tag(): user.code_run

settings():
    user.code_private_function_formatter = "SNAKE_CASE"

(toggle | tog) imports: user.code_toggle_libraries()
(toggle | tog) packages: user.code_toggle_libraries()

### more stata imperatives
# alternative to saying ""state import""
s s c install: user.code_import()
s s c install <user.code_libraries>+:
    formatted = user.formatted_text(code_libraries_list, "NOOP")
    insert("ssc uninstall ")
    user.paste(formatted)

s s c uninstall <user.code_libraries>+:
    formatted = user.formatted_text(code_libraries_list, "NOOP")
    insert("ssc uninstall ")
    user.paste(formatted)

state for val: user.code_state_for()
[state] foreach local: user.code_state_for_each_local()
[state] foreach global: user.code_state_for_each_global()
[state] foreach (varlist | var [list]): user.code_state_for_each_varlist()
[state] foreach new [list]: user.code_state_for_each_newlist()
[state] foreach num [list]: user.code_state_for_each_numlist()

### Navigate in stata
help {user.code_common_function}:
    user.stata_help(user.code_common_function)

browse: user.stata_browse()
browse if [{user.stata_variable_list}]:
    user.focus_stata_instance()
    key(ctrl-1)
    user.delete_all()
    user.paste("browse if ")
    user.paste("{stata_variable_list}" or "")

do edit: user.stata_do_file_editor()

### more snippets
funk {user.stata_code_common_function_variable} {user.stata_variable_list}+:
    user.code_insert_function(stata_code_common_function_variable, "")
    formatted = user.formatted_text(stata_variable_list_list, "NOOP")
    user.paste(formatted)
    insert(" ")


# functions followed by other functions
capture {user.code_common_function}:
    user.paste("capture ")
    user.code_insert_function(code_common_function, "")

quietly {user.code_common_function}:
    user.paste("qui ")
    user.code_insert_function(code_common_function, "")

noisily {user.code_common_function}:
    user.paste("noisily ")
    user.code_insert_function(code_common_function, "")

arg {user.code_parameter_name}: user.code_insert_named_argument(code_parameter_name)

stata print variables: user.stata_print_variables()
var {user.stata_variable_list}+:
    formatted = user.formatted_text(stata_variable_list_list, "NOOP")
    user.paste(formatted)
    insert(" ")


(local | lock) quote: user.insert_between("`", "'")
(global | glow) quote:
    user.insert_between("${", "}")
stata quote:
    user.paste('`"')
    user.paste('"')
    user.paste("'")
    key(left:2)

(local | lock) string <user.text> [then]:
    formatted = user.formatted_text(text, "SNAKE_CASE")
    user.paste("`{formatted}' ")
    
# (lock | local) string <user.alphabet>:
#     user.paste("`{alphabet}' ")

(global | glow) string <user.text> [then]:
    formatted = user.formatted_text(text, "SNAKE_CASE")
    user.paste("${{{formatted}}} ")

stata string <user.text> [then]:
    formatted = user.formatted_text(text, "CAPITALIZE_FIRST_WORD")
    user.paste('`"')
    user.paste(formatted)
    user.paste('"')
    user.paste("'")


scalar: user.paste("sca_")
matrix: user.paste("mat_")

display <user.text> [then]:
    str = 'di "{text}"'
    user.paste(str)