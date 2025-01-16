#!/usr/bin/env python3
test = [lambda *args : (
    lambda *args : (
        print(args)
    )
)][0]()

test("Hello World")
