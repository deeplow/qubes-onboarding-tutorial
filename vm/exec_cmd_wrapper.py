#!/usr/bin/python3

import sys
import subprocess
import qubesidle.idle_watcher_window
from gi.repository import GLib

class ExecWrapper:
    """
    Wrapper for GUI program. Informs main tutorial component when the
    application's GUI opens and when it closes.

    Assumes this is the only GUI program being executed in the VM.
    """

    STATE_1 = "starting"
    STATE_2 = "waiting for window to open"
    STATE_3 = "waiting for window to close"
    STATE_4 = "exiting"

    def __init__(self, cmd):
        self.cmd = cmd
        self.state = self.STATE_1
        self.idle_watcher = qubesidle.idle_watcher_window.IdleWatcher();
        self.update_state()

    def update_state(self):
        any_window_opened = not self.idle_watcher.is_idle()
        if self.state == self.STATE_1:
            if not any_window_opened:
                subprocess.Popen(self.cmd, shell=True)
            else:
                raise Exception("there is already another GUI program open")
            self.state = self.STATE_2
        elif self.state == self.STATE_2 and any_window_opened:
            subprocess.Popen(
                "qrexec-client-vm dom0 tutorial.NextStep+opened_window",
                 shell=True)
            self.state = self.STATE_3
        elif self.state == self.STATE_3 and not any_window_opened:
            subprocess.Popen(
                "qrexec-client-vm dom0 tutorial.NextStep+closed_all_windows",
                shell=True)
            self.state = self.STATE_4
        elif self.state == self.STATE_4:
            # do not update state again
            return

        GLib.timeout_add(100, self.update_state)

if __name__ == '__main__':
    exec_cmd = " ".join(sys.argv[1:])
    ExecWrapper(exec_cmd)
    loop = GLib.MainLoop()
    loop.run()