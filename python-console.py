#!/usr/bin/env python3
import ctypes
libreadline = ctypes.CDLL("libreadline.so")
libreadline.readline.argtypes = [ctypes.c_char_p]
libreadline.readline.restype = ctypes.c_char_p
print("Cursed python console:")
while True:
    exec(libreadline.readline(b'>>> ').decode("utf-8").strip())
