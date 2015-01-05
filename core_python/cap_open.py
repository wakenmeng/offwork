# -*- coding: utf-8 -*-

class CapOpen(object):

    def __init__(self, fn, mode='r', buf=-1):
        self.file = open(fn, mode, buf)

    def write(self, line):
        self.file.write(line.upper())

    def __repr__(self):
        return 'self.file'

    def __str__(self):
        return str(self.file)

    def __getattr__(self, attr):
        return getattr(self.file, attr)

