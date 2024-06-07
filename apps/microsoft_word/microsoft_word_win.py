from typing import Optional
from talon import Module, Context, actions

mod = Module()
ctx = Context()

mod.apps.microsoft_word = r"""
os: windows
and app.exe: /^winword\.exe$/i
"""

ctx.matches = r"""
os: windows
app: microsoft_word
"""

# # edit redefinitions
# @ctx.action_class("edit")
# class EditActions:



@mod.action_class
class Actions:
    def dictation_peek_unselect_before():
        """test"""
        actions.edit.right()

    def dictation_peek_unselect_after():
        """test"""
        actions.edit.left()

    def test():
        """hello"""
        before = None
        actions.edit.extend_word_left()
        actions.edit.extend_word_left()
        before = actions.edit.selected_text()
        print("this is"+before+'continues')


@ctx.action_class("user")
class UserActions:
    def dictation_peek(left: bool, right: bool) -> tuple[Optional[str], Optional[str]]:

        if not (left or right):
            return None, None
        before, after = None, None
        
        # go right first
        actions.edit.extend_word_right()
        actions.edit.extend_word_right()
        after = actions.edit.selected_text()
        actions.edit.left() #deselect
        
        # go left
        if left:
            actions.edit.extend_word_left()
            actions.edit.extend_word_left()
            before = actions.edit.selected_text()
            actions.edit.right()  # deselect
            # if there is a newline to the right, we need to go left again
            if after.startswith("\r\n"):
                actions.edit.left()
        
        print('after.'+after+".end")
        print("before."+str(before)+".end")
        if after.startswith("\r\n"):
            print("If there is a newline, I detect it.")
        return before, after