from talon import Module, Context, actions

mod = Module()


@mod.action_class
class Actions:
    def stata_run_do_editor():
        "Run selected text in an open version of the Stata application via its do-file editor."


ctx = Context()

ctx.matches = r"""
os: windows
code.language: stata
not win.title: Do-file Editor
"""


@ctx.action_class("user")
class UserActions:
    def stata_run_do_editor():
        actions.user.switcher_focus("Stata")
        actions.sleep("300ms")
        actions.key("ctrl-1")
        actions.sleep("100ms")
        actions.edit.select_all()
        actions.insert("doedit")
        actions.key("enter")
        actions.sleep("300ms")
        actions.edit.select_all()
        actions.edit.paste()
        actions.key("ctrl-d")
        actions.user.delete_all()
        actions.app.window_close()
        actions.sleep("100ms")
        actions.edit.right()
        actions.key("enter")
        # actions.sleep("300ms")
        actions.user.switcher_focus("Stata")
