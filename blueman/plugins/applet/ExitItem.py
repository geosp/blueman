from gi.repository import Gtk
from blueman.plugins.AppletPlugin import AppletPlugin
from blueman.Functions import create_menuitem, get_icon


class ExitItem(AppletPlugin):
    __depends__ = ["Menu"]
    __autoload__ = False
    __description__ = _("Adds an exit menu item to quit the applet")
    __author__ = "Walmis"
    __icon__ = "application-exit"

    def on_load(self, applet):
        item = create_menuitem("_Exit", get_icon("application-exit", 16))
        item.connect("activate", lambda x: Gtk.main_quit())
        applet.Plugins.Menu.Register(self, item, 100)

    def on_unload(self):
        self.Applet.Plugins.Menu.Unregister(self)
