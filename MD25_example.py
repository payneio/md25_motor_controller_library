#!/usr/bin/python

from MD25 import MD25
import time

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the MD25 and use STANDARD mode (default value)
controller = MD25(0x58,1,True)
controller.forward()
time.sleep(0.5)
controller.forward(1)
time.sleep(1.0)
controller.turn()
time.sleep(1.0)
controller.stop()
