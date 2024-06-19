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
    "libraries": "stata_code_libraries.talon-list",
    "parameters": "stata_code_parameter_names.talon-list",
    "variables": "stata_code_variables.talon-list",
}


@mod.action_class
class Actions:
    def edit_code_list(code_tag: str):
        """Open respective file for editing"""
        active_lang = actions.code.language()
        path = os.path.join(REPO_DIR,"lang",active_lang,code_tag)
        print(path)
        os.startfile(path, "open")
