#!/usr/bin/env python
from sys import argv
from os import system

e = argv[1][:-3]
print e

system("pandoc -s " + e + ".md -o " + e + ".html")
system("pandoc -s " + e + ".md -o " + e + ".pdf")
