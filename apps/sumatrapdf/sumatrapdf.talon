app: sumatrapdf
-
# Set tags
tag(): user.pages
tag(): user.tabs
tag(): user.find

(tab | file) reload: key(r)
tab close all: key(ctrl-shift-w)

# These commands depend on manually specifying these shortcuts in the Sumatra pdf application
# the chosen shortcuts are based on the firefox extension https://addons.mozilla.org/en-US/firefox/addon/close-tabs-shortcuts/
tab close other: key(alt-w)
tab close left: key(alt-shift-f1)
tab close right: key(alt-shift-f2)