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