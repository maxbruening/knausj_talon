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

    def code_state_else_if():
        actions.insert("else if  {")
        actions.key("enter tab enter left")
        actions.insert("}")
        actions.key("up:2 right:7")

    def code_state_else():
        actions.insert("else  {")
        actions.key("enter tab enter left")
        actions.insert("}")
        actions.key("up:2 right:4")  

    def code_state_do():
        actions.insert("do {")
        actions.key("enter tab enter left")
        actions.insert("} while ()")
        actions.key("up tab")

    def code_state_for():    
        actions.insert("for () {")
        actions.key("enter tab enter left")
        actions.insert("}")
        actions.key("up:2 right:4")

    def code_state_for_each():
        actions.insert("foreach  in {")
        actions.key("enter tab enter left")
        actions.insert("}")
        actions.key("up:2 right:7")

    def code_break():
        actions.insert("break")

    def code_next():
        actions.insert("continue")        

    def code_comment_line_prefix():
       actions.auto_insert("* ") 
       # actions.auto_insert("// ") 



    




