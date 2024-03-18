from talon import Module, Context, actions

mod = Module()
ctx = Context()

mod.apps.mendeley_desktop = r"""
os: windows
and app.name: MendeleyDesktop
os: windows
and app.exe: /^mendeleydesktop\.exe$/i
"""

ctx.matches = r"""
os: windows
app: mendeley_desktop
"""

# @mod.action_class
# class Actions:
