from talon import Context, actions
ctx = Context()

# override snippets for stata 17 do-file editor
ctx.matches = r"""
code.language: stata
app.exe_path: /stata17/
win.title: /^Do-file Editor/
"""

@ctx.action_class("user")
class UserActions:

    # imperative.py
    def code_state_if():
        actions.insert("if  {\n")
        actions.key("up")
        actions.edit.line_end()
        actions.key("left:2")

    def code_state_else_if():
        actions.insert("else if  {\n")
        actions.key("up")
        actions.edit.line_end()
        actions.key("left:2")

    def code_state_else():
        actions.insert("else {\n")

    def code_state_for():
        actions.insert("forval  {\n")
        actions.key("up")
        actions.edit.line_end()
        actions.key("left:2")

    def code_state_for_each():
        actions.insert("foreach  in  {\n")
        actions.key("up")
        actions.edit.line_end()
        actions.key("left:2")

    def code_state_while():
        actions.insert("while  {\n")
        actions.key("up")
        actions.edit.line_end()
        actions.key("left:2")

    # imperative_stata
    def code_state_place_cursor():
        actions.key("up")
        actions.edit.line_end()
        actions.key("left:2")

    def code_state_for_each_local():
        actions.insert("foreach m of local  {\n")
        actions.user.code_state_place_cursor()

    def code_state_for_each_global():
        actions.insert("foreach g of global  {\n")
        actions.user.code_state_place_cursor()

    def code_state_for_each_varlist():
        actions.insert("foreach var of varlist  {\n")
        actions.user.code_state_place_cursor()

    def code_state_for_each_newlist():
        actions.insert("foreach var of newlist  {\n")
        actions.user.code_state_place_cursor()

    def code_state_for_each_numlist():
        actions.insert("foreach num of numlist  {\n")
        actions.user.code_state_place_cursor()

    