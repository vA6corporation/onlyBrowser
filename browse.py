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
        self.scroll = gui.get_object('scrolled')

        #Dark theme
        settings = Gtk.Settings.get_default()
        settings.set_property("gtk-application-prefer-dark-theme", True)

        #self.win.connect("on_window_delete_event", self.on_window_delete_event)

        self.win.connect("destroy", Gtk.main_quit)
        self.win.maximize()
        self.win.show()
        gui.connect_signals(self)

        self.webview = WebKit.WebView()
        self.scroll.add(self.webview)
        self.webview.show()

        self.webview.open('http://www.google.com/')

    def on_home_button_clicked(self, widget, data=None):
        print("eres una puta")

    def on_refresh_button_clicked(self, widget, data=None):
        self.webview.reload()

    def on_close_button_clicked(self, widget, data=None):
        print ("hola")

    def on_window_delete_event(self, widget, event, data=None):
        print ("delete event occurred")
        #self.win2.show()
        return True

Browser()
Gtk.main()
