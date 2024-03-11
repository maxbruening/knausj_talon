code.language: stata
-
tag(): user.code_imperative

tag(): user.code_comment_block_c_like
tag(): user.code_comment_block
tag(): user.code_comment_line
tag(): user.code_functions

settings():
    user.code_private_function_formatter = "SNAKE_CASE"

arg {user.code_parameter_name}:
    user.code_insert_named_argument(code_parameter_name)




regress: insert("reg")