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
        self.message_dialog = gui.get_object('message_dialog')
        self.password_entry = gui.get_object('password_entry')
        self.scroll = gui.get_object('scrolled')

        self.password_dialog.connect('delete-event', lambda w, e: w.hide() or True)
        self.message_dialog.connect('delete-event', lambda w, e: w.hide() or True)

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

        self.webview.open('https://accounts.google.com/ServiceLogin?service=wise&passive=true&continue=http%3A%2F%2Fdrive.google.com%2F%3Futm_source%3Des%26utm_medium%3Dbutton%26utm_campaign%3Dweb%26utm_content%3Dgotodrive%26usp%3Dgtd%26ltmpl%3Ddrive&urp=https%3A%2F%2Fwww.google.com%2F')
        #self.webview.open('http://www.munisatipo.gob.pe/index.php/galerias')

        self.webview.connect("navigation-policy-decision-requested", self.check)
        self.webview.connect("download-requested", self.download)
        #self.webview.connect("webkit_download_set_destination_uri", self.destino)

    def on_aceptar_button_clicked(self, widget, data=None):
        if self.password_entry.get_text() == "123":
            self.win.destroy()

    def on_message_button_clicked(self, widget, data=None):
        self.message_dialog.hide()

    def on_cancelar_button_clicked(self, widget, data=None):
        self.password_entry.delete_text(0,-1)
        self.password_dialog.hide()

    def on_home_button_clicked(self, widget, data=None):
        self.webview.open('https://www.google.com/')

    def on_refresh_button_clicked(self, widget, data=None):
        self.webview.reload()

    def on_close_button_clicked(self, widget, data=None):
        self.password_dialog.show()

    def on_window_delete_event(self, widget, event, data=None):
        print ("delete event occurred")
        self.password_dialog.show()
        #self.win2.show()
        return True

    def check(self, widget, frame, req, nav, policy ,data=None):
        #self.message_dialog.show()
        print("Se abre un link")
        return False

    def download(self, widget, download, data=None):
        print("Hay una descarga")
        #dest = "/home/vampirodx/"
        print(dir(download))
        #down.set_destination_uri(download,dest)
        #download.start(download)
        #down.webkit_download_start()
        return True

Browser()
Gtk.main()
