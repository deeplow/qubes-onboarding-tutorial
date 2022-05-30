#!/usr/bin/python3
# open file manager and notify of next step
# otherwise it's hard to know when the file manager actually opens

import subprocess

from dbus.mainloop.glib import DBusGMainLoop
from gi.repository import GLib
import dbus

def setup_handler():
    DBusGMainLoop(set_as_default=True)
    bus = dbus.SessionBus()
    bus.add_signal_receiver(handler_function=notify_dom0,
                            dbus_interface='org.gtk.Actions',
                            path='/org/gnome/Nautilus')

def notify_dom0(*args):
    # notify dom0
    subprocess.Popen("qrexec-client-vm dom0 tutorial.NextStep+opened_nautilus",
                     shell=True)

def main():
    subprocess.Popen("nautilus ~/", shell=True)
    setup_handler()
    loop = GLib.MainLoop()
    loop.run()
