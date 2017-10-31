# -*- coding: utf-8 -*-

from vector import *

# vector

def vector_ex():
  # 4
  # print Vector([8.218,-9.341]).plus(Vector([-1.129,2.111]))
  # print Vector([7.119,8.215]).minus(Vector([-8.223,0.878]))
  # print Vector([1.671,-1.012,-0.318]).scalar_multiply(7.41)
  
  # 6
  # print Vector([-0.221,7.437]).magnitude()
  # print Vector([8.813,-1.331,-6.247]).magnitude()
  # print Vector([5.581,-2.136]).normalize()
  # print Vector([1.996,3.108,-4.554]).normalize()
  
  # 8
  print Vector([7.887,4.138]).dot_product(Vector([-8.802,6.776]))
  print Vector([-5.955,-4.904,-1.874]).dot_product(Vector([-4.496,-8.755,7.103]))
  print Vector([3.183,-7.627]).inner_angle(Vector([-2.668,5.319]))
  print Vector([7.350,0.221,5.188]).inner_angle(Vector([2.751,8.259,3.985]), True)

if __name__ == '__main__':
  vector_ex()