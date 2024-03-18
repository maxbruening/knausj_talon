from talon import Module, Context, actions

mod = Module()
ctx = Context()

mod.apps.jabref = r"""
os: windows
and app.name: JabRef.exe
os: windows
and app.exe: /^jabref\.exe$/i
"""

ctx.matches = r"""
app: jabref
"""

# @mod.action_class
# class Actions:
