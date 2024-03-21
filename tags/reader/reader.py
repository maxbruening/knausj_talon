from talon import Context, Module, actions, app

mod = Module()
ctx = Context()
ctx.matches = r"""
tag: reader
"""


@ctx.action_class("user")
class UserActions:
    
    # find
    def find(text: str = None):
        # actions.edit.find("")
        # if text:
        #     actions.insert(text)
        actions.edit.find(text)

    



@ctx.action_class("reader")
class ReaderActions:
    def rotate_right():
        """Rotates the document 90 degrees to the right"""
        
    def rotate_left():
        """Rotates the document 90 degrees to the left"""

    def go_back():
        """Goes back"""

    def go_forward():
        """Goes forward"""
        