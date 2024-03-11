from talon import Module, Context, actions, settings

mod = Module()

@mod.action_class
class Actions:
    def stata_run_do_editor(): "Run stata code in the stata application via the do-file editor."

ctx = Context()

ctx.matches = r"""
code.language: stata
"""

@ctx.action_class("user")
class UserActions:
   def stata_run_do_editor():
      actions.user.switcher_focus("Stata")
      actions.sleep("500ms")
      # key(ctrl-1)
      # sleep(500ms)
      # insert("doedit")
      # key(enter)
      # sleep(500ms)
      # edit.paste()
      # edit.select_line()
      # sleep(500ms)
      # key(ctrl-d)
      # sleep(500ms)
      # user.delete_all()
      # app.window_close()
      # sleep(500ms)
      # edit.right()
      # key(enter)










      # actions.key(ctrl-1)
      # actions.sleep("500ms")
      # actions.insert("doedit")
      # actions.key("enter")
      # actions.sleep("500ms")
      # actions.edit.paste()
      # actions.key("ctrl-d")
      # user.delete_all()
      # actions.app.window_close()
   