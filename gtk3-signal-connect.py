#!/usr/bin/env python3
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

def connect(obj, sig):
    def decorator(function):
        obj.connect(sig, function)
        def wrapper(*args, **kwargs):
            return  function(*args, **kwargs)
        return wrapper
    return decorator

w = Gtk.Window()
b = Gtk.Button(label="button")

@connect(b, "clicked")
def test(widget):
    print(123)

w.add(b)
w.show_all()
Gtk.main()
