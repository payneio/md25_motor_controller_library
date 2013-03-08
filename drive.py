from MD25 import MD25
import tty, time, termios, fcntl, sys, os

controller = MD25(0x58,1,True)

class _GetchUnix:
  def __init__(self):
    import tty, sys

  def __call__(self):
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
      tty.setraw(sys.stdin.fileno())
      ch = sys.stdin.read(1)
    finally:
      termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

getch = _GetchUnix()
k = ''
while k != 'x':
  k = getch()
  if k == 's':
    controller.forward(1)
  elif k == 'w':
    controller.forward(255)
  elif k == 'd':
    controller.turn(255,1)
  elif k == 'a':
    controller.turn(1,255)
  else:
    controller.stop()
  time.sleep(0.1)
  controller.stop()

