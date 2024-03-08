code.language: stata
-
settings():
   key_wait = 4
   insert_wait = 7


due this: 
   edit.copy()
   # user.stata_run_do_editor()
   sleep(500ms)
   user.switcher_focus("Stata")
   sleep(500ms)
   key(ctrl-1)
   sleep(500ms)
   insert("doedit")
   key(enter)
   sleep(500ms)
   edit.paste()
   edit.select_line()
   sleep(500ms)
   key(ctrl-d)
   sleep(500ms)
   user.delete_all()
   app.window_close()
   sleep(500ms)
   edit.right()
   key(enter)