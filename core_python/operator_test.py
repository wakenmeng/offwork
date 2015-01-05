#-*- coding: utf-8 -*-
from random import choice, randint
from operator import add, sub

ops = {'+': add, '-': sub}
MAXTRIES = 2
def doprob():
    op = choice('+-')
    nums = [randint(1, 10) for i in range(2)]
    nums.sort(reverse=True)
    prompt = '%d %s %d=' % (nums[0], op, nums[1])
    ans = ops.get(op)(*nums)
    oops = 0
    while True:
        try:
            if int(raw_input(prompt)) == ans:
                print 'Correct!'
                break
            elif oops == MAXTRIES:
                print 'answer\n%s%d' % (prompt, ans)
            else:
                print 'try again'
                oops += 1
        except (KeyboardInterrupt, EOFError, ValueError):
            print 'invalid Input... try again.'

def main():
    while True:
        doprob()
        try:
            opt = raw_input('Wanna play again?[y]').lower()
            if opt and opt[0] == 'n':
                break
        except (KeyboardInterrupt, EOFError):
            break

if __name__ == '__main__':
    main()


