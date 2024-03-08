from talon import Context, actions, settings

ctx = Context()

ctx.matches = r"""
code.language: stata
"""

@ctx.action_class("user")
class UserActions:
    def code_block():
        actions.auto_insert("\n")

    def code_state_if():
        actions.insert("if  {")
        actions.key("enter tab enter left")
        actions.insert("}")
        actions.key("up:2 right:2")

    def code_comment_line_prefix():
       actions.auto_insert("* ") 
       # actions.auto_insert("// ") 



    




