from talon import Module, Context, actions, ui

mod = Module()


@mod.action_class
class Actions:
    def focus_stata_instance():
        "focus stata instance"

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
    def focus_stata_instance():
        active_windows = ui.windows()
        for w in active_windows:
            if w.title.startswith("Stata") and "Stata" in w.app.name:
                w.focus()
                break

    def stata_run_do_editor():
        actions.user.focus_stata_instance()
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
