from talon import Context, actions

ctx = Context()

ctx.matches = r"""
os: windows
app: stata
win.title: /^Stata/
"""

@ctx.action_class("user")
class UserActions:
    def stata_help(arg: str):
        actions.key("ctrl-1")
        actions.auto_insert("help "+arg)
        actions.key("enter")

    def stata_browse():
        actions.key("ctrl-8")

    def stata_do_file_editor():
        actions.key("ctrl-9")