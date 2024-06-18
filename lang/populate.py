# for PR to community probably modify edit_text_file.py
import os

from talon import Context, Module, actions

# path to community/knausj root directory
REPO_DIR = os.path.dirname(os.path.dirname(__file__))

ctx = Context()
mod = Module()


mod.list("code_tag", desc="List of ")

@mod.action_class
class Actions:
    def edit_code_list(code_tag: str):
        """Open respective file for editing"""


ctx.matches = r"""
mode: command
code.language: /./
"""


ctx.lists["user.code_tag"] = {
    "functions": "stata_code_common_function.talon-list",
    "libraries": "libraries",
    "parameters": "parameter_names",
    "variables": "variables",
}


@mod.action_class
class Actions:
    def edit_code_list(code_tag: str):
        """Open respective file for editing"""
        lang = actions.code.language()
        path = os.path.join(REPO_DIR,lang,code_tag)
        print(path)
        os.startfile(path, "open")
