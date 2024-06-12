from talon import Module, Context, actions

mod = Module()
ctx = Context()

mod.apps.microsoft_excel = r"""
os: windows
and app.exe: /^excel\.exe$/i
"""

ctx.matches = r"""
os: windows
app: microsoft_excel
"""

# @mod.action_class
# class Actions:
