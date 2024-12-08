SHELL=/usr/bin/env python3

SRCS = $(wildcard *.c)
OBJS = $(SRCS:.c=.o)

build: main

main: $(OBJS)
  import subprocess ; subprocess.run(["gcc", "-o", "main"] + "$(OBJS)".split(" "))

clean:
  import os; [os.remove(file) for file in "$(OBJS)".split(" ")]

%.o: %.c
  import subprocess ; subprocess.run(["gcc", "-c", "$<", "-o", "$@"])
