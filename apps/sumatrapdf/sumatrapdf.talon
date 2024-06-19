app: sumatrapdf
-
# Set tags
tag(): user.pages
tag(): user.tabs
tag(): user.find


please [<user.text>]:
    key(ctrl-k)
    insert(user.text or "")

file rename: key(f2)

(toggle | tog) [book] marks: key(shift-f12)
(toggle | tog) menu: key(f9)
(toggle | tog) (tools | tool [bar]): key(f8)

(tab | file) reload: key(r)

# These commands depend on manually specifying these shortcuts in the Sumatra pdf application
# the chosen shortcuts are based on the firefox extension https://addons.mozilla.org/en-US/firefox/addon/close-tabs-shortcuts/
tab close all: key(ctrl-shift-w)
tab close other: key(alt-w)
tab close left: key(alt-shift-f1)
tab close right: key(alt-shift-f2)