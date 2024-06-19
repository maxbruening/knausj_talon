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
s s c install: user.code_import() # alternative to saying ""state import""
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
# opens the help for the function/command

browse: user.stata_browse()
# starts the data editor

do edit: user.stata_do_file_editor()
# starts the do-file editor

### more snippets
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

(sta | stata) quote: user.insert_between("`", "'")
local var: user.paste("`var' ")
local <user.text> [then]:
    formatted = user.formatted_text(text, "SNAKE_CASE")
    user.paste("`{formatted}' ")

global <user.text> [then]:
    formatted = user.formatted_text(text, "SNAKE_CASE")
    user.paste("${{{formatted}}} ")
