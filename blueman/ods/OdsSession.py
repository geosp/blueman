from gi.repository import GObject
from blueman.ods.OdsBase import OdsBase


class OdsSession(OdsBase):
    __gsignals__ = {
        'connected': (GObject.SignalFlags.RUN_FIRST, None, ()),
        'cancelled': (GObject.SignalFlags.NO_HOOKS, None, ()),
        'disconnected': (GObject.SignalFlags.NO_HOOKS, None, ()),
        'transfer-started': (GObject.SignalFlags.NO_HOOKS, None, (GObject.TYPE_PYOBJECT, GObject.TYPE_PYOBJECT, GObject.TYPE_PYOBJECT,)),
        'transfer-progress': (GObject.SignalFlags.NO_HOOKS, None, (GObject.TYPE_PYOBJECT,)),
        'transfer-completed': (GObject.SignalFlags.NO_HOOKS, None, ()),
        'error-occurred': (GObject.SignalFlags.NO_HOOKS, None, (GObject.TYPE_PYOBJECT, GObject.TYPE_PYOBJECT,)),
    }

    def __init__(self, obj_path):
        OdsBase.__init__(self, "org.openobex.Session", obj_path)
        self.Connected = False
        self.Handle("Cancelled", self.on_cancelled)
        self.Handle("Disconnected", self.on_disconnected)
        self.Handle("TransferStarted", self.on_trans_started)
        self.Handle("TransferProgress", self.on_trans_progress)
        self.Handle("TransferCompleted", self.on_trans_complete)
        self.Handle("ErrorOccurred", self.on_error)

    def __del__(self):
        dprint("deleting session")

    # this is executed by gobject, before the connected signal is emitted
    def do_connected(self):
        self.Connected = True

    def on_cancelled(self):
        self.emit("cancelled")

    #self.DisconnectAll()

    def on_disconnected(self):
        dprint("disconnected")
        self.Connected = False
        self.emit("disconnected")

    #self.DisconnectAll()

    def on_trans_started(self, filename, path, size):
        self.emit("transfer-started", filename, path, size)

    def on_trans_progress(self, bytes):
        self.emit("transfer-progress", bytes)

    def on_trans_complete(self):
        self.emit("transfer-completed")

    def on_error(self, name, msg):
        self.emit("error-occurred", name, msg)

    #self.DisconnectAll()
