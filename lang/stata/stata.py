import os
from talon import Module, Context, actions, settings, ui

mod = Module()
ctx = Context()

REPO_DIR = os.path.dirname(os.path.dirname(__file__))

mod.list("stata_variable_list", "List of stata variables")
mod.list(
    "stata_code_common_function_variable",
    "List of stata functions that take variables as input",
)


@mod.action_class
class Actions:
    def focus_stata_instance():
        """focus stata instance"""
        # I could include a check that only one stata instance is open.
        # I could also define what to do if no stata instance is open.
        active_windows = ui.windows()
        for w in active_windows:
            if w.title.startswith("Stata") and "Stata" in w.app.name:
                w.focus()
                break

    def stata_run_do_editor():
        """Run selected text in an open version of the Stata application via its do-file editor."""
        # Alternatively, I could print to a file and then run the file from stata's command window
        actions.user.focus_stata_instance()
        actions.sleep("300ms")
        actions.key("ctrl-9")
        actions.sleep("300ms")
        actions.edit.paste()
        actions.key("ctrl-d")
        actions.user.delete_all()
        actions.app.window_close()
        actions.sleep("200ms")
        actions.edit.right()
        actions.key("enter")
        # actions.sleep("300ms")
        actions.user.switcher_focus("Stata")

    def stata_help(arg: str):
        """Opens help for the command or <user.text>/ the stata viewer"""

    def stata_browse():
        """Opens the data editor"""

    def stata_do_file_editor():
        """Opens a new empty tab in the do-file editor"""

    def stata_print_variables():
        """Prints a talon-list with all current variables"""

    def code_insert_stata_variables(varlist: list):
        """Insert stata variables from the list"""

    # imperative_stata
    def code_state_place_cursor():
        """Places cursor in stata statements"""

    def code_state_for_each_local():
        """Inserts stata 'foreach m of local' statement"""

    def code_state_for_each_global():
        """Inserts stata 'foreach g of global' statement"""

    def code_state_for_each_varlist():
        """Inserts stata 'foreach var of varlist' statement"""

    def code_state_for_each_newlist():
        """Inserts stata 'foreach var of newlist' statement"""

    def code_state_for_each_numlist():
        """Inserts stata 'foreach num of numlist' statement"""


ctx.matches = r"""
code.language: stata
"""

@ctx.capture(
    "user.code_common_function",
    rule="{user.code_common_function} | {user.stata_code_common_function_variable}",
)
def code_common_function(m):
    return str(m)


@ctx.action_class("user")
class UserActions:
    # Navigate in stata
    def stata_help(arg: str):
        actions.user.focus_stata_instance()
        actions.key("ctrl-1")
        actions.auto_insert("help " + arg)
        actions.key("enter")

    def stata_browse():
        actions.user.focus_stata_instance()
        actions.key("ctrl-8")

    def stata_do_file_editor():
        actions.user.focus_stata_instance()
        actions.key("ctrl-9")

    def stata_print_variables():
        actions.user.focus_stata_instance()

        file_name = os.path.join(REPO_DIR, "stata", "stata_code_variables.talon-list")

        actions.sleep("300ms")
        actions.key("ctrl-9")
        actions.sleep("300ms")

        # Could modify the variable names before printing them.
        # For example separate words from numbers
        # remove leading underscores, swap middle underscores with spaces etc.
        # remove colons
        actions.user.paste(
            'file open f1 using "' + str(file_name) + '" ,write replace text\n\n'
            'file write f1 "list: user.stata_variable_list" _n ///\n'
            '"code.language: stata" _n "-" _n\n\n'
            "foreach var of varlist _all {\n"
            """\tlocal varlabel: variable label `var'\n"""
            """\tfile write f1 `"`var'"' _n\n"""
            """\tif "`varlabel'" != "" & "`varlabel'" != "`var'" {\n"""
            """\t\tfile write f1 `"`varlabel': `var'"' _n\n"""
            """\t}\n"""
            "}\n\n"
            "file close f1\n"
        )

        actions.key("ctrl-d")
        actions.user.delete_all()
        actions.app.window_close()
        actions.sleep("200ms")
        actions.edit.right()
        actions.sleep("200ms")
        actions.key("enter")
        actions.sleep("200ms")
        actions.user.switcher_focus_last()

    # code_run tag
    def code_run_selection():
        actions.edit.copy()
        actions.user.stata_run_do_editor()

    def code_run_line_start():
        actions.edit.extend_line_start()
        actions.edit.copy()
        actions.user.stata_run_do_editor()

    def code_run_line_end():
        actions.edit.extend_line_end()
        actions.edit.copy()
        actions.user.stata_run_do_editor()

    def code_run_line():
        actions.edit.select_line()
        actions.edit.copy()
        actions.user.stata_run_do_editor()

    def code_run_file():
        actions.edit.extend_file_start()
        actions.edit.copy()
        actions.user.stata_run_do_editor()

    def code_run_file_start():
        actions.edit.extend_file_start()
        actions.edit.copy()
        actions.user.stata_run_do_editor()

    def code_run_file_end():
        actions.edit.extend_file_end()
        actions.edit.copy()
        actions.user.stata_run_do_editor()

    # comment_line.py
    def code_comment_line_prefix():
        actions.auto_insert("* ")

    # functions.py
    def code_private_function(text: str):
        result = "program {} \n\nend".format(
            actions.user.formatted_text(
                text, settings.get("user.code_private_function_formatter")
            )
        )
        actions.user.paste(result)
        actions.edit.up()
        actions.key("tab")

    def code_default_function(text: str):
        actions.user.code_private_function(text)

    def code_insert_named_argument(parameter_name: str):
        actions.insert(f"{parameter_name} ")

    # functions_common.py
    def code_insert_function(text: str, selection: str):
        text += f" {selection or ''}"
        actions.user.paste(text)

    # imperative.py
    def code_block():
        actions.auto_insert("\n")

    def code_state_if():
        actions.insert("if  {\n\n}")
        actions.key("up tab up")
        actions.edit.line_end()
        actions.key("left:2")

    def code_state_else_if():
        actions.insert("else if  {\n\n}")
        actions.key("up tab up")
        actions.edit.line_end()
        actions.key("left:2")

    def code_state_else():
        actions.insert("else {\n\n}")
        actions.key("up tab")

    def code_state_for():
        actions.insert("forval  {\n\n}")
        actions.key("up tab up")
        actions.edit.line_end()
        actions.key("left:2")

    def code_state_for_each():
        actions.insert("foreach  in  {\n\n}")
        actions.key("up tab up")
        actions.edit.line_end()
        actions.key("left:2")

    def code_state_while():
        actions.insert("while  {\n\n}")
        actions.key("up tab up")
        actions.edit.line_end()
        actions.key("left:2")

    def code_break():
        actions.insert("break")

    def code_next():
        actions.insert("continue")

    # imperative_stata
    def code_state_place_cursor():
        actions.key("up tab up")
        actions.edit.line_end()
        actions.key("left:2")

    def code_state_for_each_local():
        actions.insert("foreach m of local  {\n\n}")
        actions.user.code_state_place_cursor()

    def code_state_for_each_global():
        actions.insert("foreach g of global  {\n\n}")
        actions.user.code_state_place_cursor()

    def code_state_for_each_varlist():
        actions.insert("foreach var of varlist  {\n\n}")
        actions.user.code_state_place_cursor()

    def code_state_for_each_newlist():
        actions.insert("foreach var of newlist  {\n\n}")
        actions.user.code_state_place_cursor()

    def code_state_for_each_numlist():
        actions.insert("foreach num of numlist  {\n\n}")
        actions.user.code_state_place_cursor()

    # libraries.py
    def code_import():
        actions.auto_insert("ssc install ")

    # libraries_gui.py
    def code_insert_library(text: str, selection: str):
        actions.auto_insert("ssc install ")
        actions.user.paste(text + selection)

    # operators_array.py
    def code_operator_subscript():
        actions.user.insert_between("[", "]")

    # operators_assignment.py
    def code_operator_assignment():
        actions.auto_insert(" = ")

    # operators_math.py
    def code_operator_subtraction():
        actions.auto_insert(" - ")

    def code_operator_addition():
        actions.auto_insert(" + ")

    def code_operator_multiplication():
        actions.auto_insert(" * ")

    def code_operator_division():
        actions.auto_insert(" / ")

    def code_operator_modulo():
        actions.user.insert_between("mod(", ")")

    def code_operator_exponent():
        actions.auto_insert(" ^ ")

    def code_operator_equal():
        actions.auto_insert(" == ")

    def code_operator_not_equal():
        actions.auto_insert(" != ")

    def code_operator_greater_than():
        actions.auto_insert(" > ")

    def code_operator_less_than():
        actions.auto_insert(" < ")

    def code_operator_greater_than_or_equal_to():
        actions.auto_insert(" >= ")

    def code_operator_less_than_or_equal_to():
        actions.auto_insert(" <= ")

    def code_operator_and():
        actions.auto_insert(" & ")

    def code_operator_or():
        actions.auto_insert(" | ")
