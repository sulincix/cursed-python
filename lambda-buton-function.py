#!/usr/bin/env python3
import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

b = Gtk.Button(label="test")
b.connect("clicked", lambda *args :(
    print(args[1])
), "Hello World")

w = Gtk.Window()
w.add(b)
w.show_all()
Gtk.main()
