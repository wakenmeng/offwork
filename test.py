class InfoBoard():
    def __init__(self):
        self.func = 'show info'

    def show_info(self, name):
        def _get_short_name(name):
            print '-'*5
            print self.func
            if '-' in name:
                return name.split('-')[0]
            name = 'liubinbin'

        short_name = _get_short_name(name)
        if short_name is not None:
            print short_name
        else:
            print 'invalid name', name

def foo(name, age=23, gender='male'):
    print name, age, gender

def bar(gender):
    foo('weikang', gender)

if __name__ == "__main__":
    board = InfoBoard()
    board.show_info('waken-meng')
    board.show_info('mengweikang')
    bar(21)

