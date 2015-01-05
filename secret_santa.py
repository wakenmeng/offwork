#coding: utf-8
from random import choice
from deploy_mail import send_mail

#give = [1,2,3,4,5,6,7,8,9]
give = [u"大王",u'二师兄',u'志航',u'小豚子',u'于亮',u'建新',u'嘉兴',u'维康',u'小庄',u'小鱼',u'毛']
rec = give[:]
rst = {}

for i in give:
    while 1:
        r = choice(rec)
        if r != i:
            rec.remove(r)
            rst.update({i: r})
            break

for k, v in rst.items():
    print "%s -> %s" % (k, v)

