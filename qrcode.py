# -*- coding: utf-8 -*-

import math

class SimpleQRCode(object):

    def __init__(self):
        self.__qrcode = ''
        self.__input()

    def __input(self):
        words = raw_input('QR Code->>')
        self.__words = words.encode('utf-8') if isinstance(words, unicode) else words
        self.__bin = self.str2bin()

    def __str__(self):
        self.gen_simple_qrcode()
        return '-'*5

    def __repr__(self):
        return self.__words

    def qrappend(self, char):
        self.__qrcode = ''.join((self.__qrcode, char))

    def qrspace(self):
        self.__qrcode = ''.join((self.__qrcode, ' '))

    def str2bin(self):
        hex_s = self.__words.encode('hex')
        int_s = int(hex_s, base=16)
        bin_s = str(bin(int_s))
        if bin_s.startswith('0b'):
            bin_s = bin_s[2:]
        return bin_s

    @staticmethod
    def get_square_edge_size(total):
        print int(math.sqrt(total))
        return int(math.sqrt(total))

    def gen_simple_qrcode(self):
        line = SimpleQRCode.get_square_edge_size(len(self.__bin))
        cnt = 0
        row = 0
        for b in self.__bin:
            if b == '1':
                self.qrappend('#'),
            else:
                print ' ',
            cnt += 1
            if cnt == line:
                print
                row += 1
                cnt = 0
        while cnt < line:
            print ' ',
            cnt += 1
        print
        print 'col', line
        print 'row', row
        print 'last_line', cnt

    def read_qrcode(self):



if __name__ == '__main__':
    qr = SimpleQRCode()
    print qr
