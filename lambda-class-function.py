#!/usr/bin/env python3
class cursed : pass

cursed.test = lambda self, *args, **kargs : (
    print(args[0])
)

a = cursed()
a.test(12)
