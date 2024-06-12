from talon import Module

mod = Module()
mod.tag("code_run", desc="Tag to run/execute code")


@mod.action_class
class Actions:
    def code_run_selection():
        """Executes the selected code"""

    def code_run_line_start():
        """Executes the code to the left of the caret/cursor on the current line"""

    def code_run_line_end():
        """Executes the code to the right of the caret/cursor on the current line"""

    def code_run_line():
        """Executes the code on the current line"""

    def code_run_file():
        """Executes the code in the current file"""

    def code_run_file_start():
        """Executes the code from the cursor position to the top of the current file"""

    def code_run_file_end():
        """Executes the code from the cursor position to the bottom of the current file"""