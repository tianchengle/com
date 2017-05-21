#coding:utf-8

import numpy as np
import sys
reload(sys)
sys.setdefaultencoding('utf8')

data=np.loadtxt('aa.csv',dtype=str,delimiter=',')

a=data[0][0]
print data[0][0].decode('gbk').encode('utf8')