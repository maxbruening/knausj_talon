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


# alternative to saying ""state import""
s s c install: user.code_import()

s s c install <user.code_libraries>: user.code_insert_library(code_libraries, "")

(toggle | tog) imports: user.code_toggle_libraries()
(toggle | tog) packages: user.code_toggle_libraries()

state for val: user.code_state_for()

# more stata imperatives
[state] foreach local: user.code_state_for_each_local()
[state] foreach global: user.code_state_for_each_global()
[state] foreach (varlist | var [list]): user.code_state_for_each_varlist()
[state] foreach new [list]: user.code_state_for_each_newlist()
[state] foreach num [list]: user.code_state_for_each_numlist()


# Navigate in stata
help {user.code_common_function}: user.stata_help(user.code_common_function)
browse: user.stata_browse()
do edit: user.stata_do_file_editor()

# more snippets
arg {user.code_parameter_name}: user.code_insert_named_argument(code_parameter_name)

stata print variables: user.stata_print_variables()
var {user.stata_variable_list}+: user.code_insert_stata_variables(stata_variable_list_list)

(sta | stata) quote: user.insert_between("`","'")
local var: insert("`var' ")
local <user.text>: 
    formatted = user.formatted_text(text,"SNAKE_CASE,NO_SPACES")
    insert("`{formatted}' ")
    
global <user.text>: 
    formatted = user.formatted_text(text,"SNAKE_CASE,NO_SPACES")
    key("$")
    start = "{"+formatted
    user.paste(start)
    insert("} ")

# funk [capture


