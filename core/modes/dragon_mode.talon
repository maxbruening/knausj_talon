#defines modes specific to Dragon.
speech.engine: dragon
not mode: user.dragon_external
-
# wakes Dragon on Mac, deactivates talon speech commands
dragon mode: user.dragon_mode()
#sleep dragon on Mac, activates talon speech commands
talon mode: user.talon_mode()
