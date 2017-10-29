# -*- coding: utf-8 -*-

from vector import *

# vector

def vector_ex():
  # 4
  print Vector([8.218,-9.341]).plus(Vector([-1.129,2.111]))
  print Vector([7.119,8.215]).minus(Vector([-8.223,0.878]))
  print Vector([1.671,-1.012,-0.318]).scalar_multiply(7.41)
  
if __name__ == '__main__':
  vector_ex()