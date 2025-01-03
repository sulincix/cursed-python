#!/usr/bin/env python3
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

def create(type, signals=[], *args, **kwargs):
    obj = type(*args, **kwargs)
    def create_wrapper(sig, function):
        def wrapper(*args, **kwargs):
            return function(sig, *args, **kwargs)
        obj.connect(sig, wrapper)
    def decorator(function):
        for sig in signals:
            create_wrapper(sig, function)
        return obj
    return decorator

w = Gtk.Window()

@create(Gtk.Button, ["clicked", "pressed", "released"], label="test")
def test(signal, widget):
    print(signal, widget, 123)

w.add(test)
w.show_all()
Gtk.main()
