#!/usr/bin/env python3.5

import gi
gi.require_version('WebKit', '3.0')
gi.require_version('Gtk', '3.0')
from gi.repository import WebKit, Gtk

class Browser():
    def __init__(self):
        gui= Gtk.Builder()
        gui.add_from_file('gui.glade')
        self.win = gui.get_object('window')
        self.password_dialog = gui.get_object('password_dialog')
        self.password_entry = gui.get_object('password_entry')
        self.scroll = gui.get_object('scrolled')

        self.password_dialog.connect('delete-event', lambda w, e: w.hide() or True)

        #Dark theme
        settings = Gtk.Settings.get_default()
        settings.set_property("gtk-application-prefer-dark-theme", True)
        self.win.set_default_size(500, 500)

        self.win.connect("destroy", Gtk.main_quit)
        #self.win.maximize()
        self.win.show()
        gui.connect_signals(self)

        self.webview = WebKit.WebView()
        self.scroll.add(self.webview)
        self.webview.show()

        self.webview.open('http://www.munisatipo.gob.pe/index.php/galerias')

    def on_aceptar_button_clicked(self, widget, data=None):
        if self.password_entry.get_text() == "123":
            self.win.destroy()

    def on_cancelar_button_clicked(self, widget, data=None):
        self.password_entry.delete_text(0,-1)
        self.password_dialog.hide()

    def on_home_button_clicked(self, widget, data=None):
        self.webview.open('http://www.munisatipo.gob.pe/index.php/galerias')

    def on_refresh_button_clicked(self, widget, data=None):
        self.webview.reload()

    def on_close_button_clicked(self, widget, data=None):
        self.password_dialog.show()

    def on_window_delete_event(self, widget, event, data=None):
        print ("delete event occurred")
        self.password_dialog.show()
        #self.win2.show()
        return True

Browser()
Gtk.main()
