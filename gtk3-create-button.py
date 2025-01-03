#!/usr/bin/env python3
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

def create(type, signals=[], *args, **kwargs):
    if callable(type):
        obj = type(*args, **kwargs)
    else:
	    obj = type
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

but = Gtk.Button(label="test2")

@create(but, ["clicked", "pressed", "released"])
def test2(signal, widget):
    print(signal, widget, 456)

b = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
print(test2)
b.pack_start(test, False, False, 0)
b.pack_start(but, False, False, 0)
w.add(b)
w.show_all()
Gtk.main()
