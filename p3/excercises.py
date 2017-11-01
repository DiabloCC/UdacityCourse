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
  # print Vector([7.887,4.138]).dot_product(Vector([-8.802,6.776]))
  # print Vector([-5.955,-4.904,-1.874]).dot_product(Vector([-4.496,-8.755,7.103]))
  # print Vector([3.183,-7.627]).inner_angle(Vector([-2.668,5.319]))
  # print Vector([7.350,0.221,5.188]).inner_angle(Vector([2.751,8.259,3.985]), True)

  # 10
  print "*"*10
  print Vector([-7.579,-7.880]).parallel(Vector([22.737,23.640]))
  print Vector([-7.579,-7.880]).parallel2(Vector([22.737,23.640]))
  print Vector([-7.579,-7.880]).parallel3(Vector([22.737,23.640]))
  print "-"*10
  print Vector([-7.579,-7.880]).orthogonal(Vector([22.737,23.640]))
  print "*"*10+"\n"
  print Vector([-2.029,9.970,4.172]).parallel(Vector([-9.231,-6.639,-7.245]))
  print Vector([-2.029,9.970,4.172]).parallel2(Vector([-9.231,-6.639,-7.245]))
  print Vector([-2.029,9.970,4.172]).parallel3(Vector([-9.231,-6.639,-7.245]))
  print "-"*10
  print Vector([-2.029,9.970,4.172]).orthogonal(Vector([-9.231,-6.639,-7.245]))
  print "*"*10+"\n"
  print Vector([-2.328,-7.284,-1.214]).parallel(Vector([-1.821,1.072,-2.940]))
  print Vector([-2.328,-7.284,-1.214]).parallel2(Vector([-1.821,1.072,-2.940]))
  print Vector([-2.328,-7.284,-1.214]).parallel3(Vector([-1.821,1.072,-2.940]))
  print "-"*10
  print Vector([-2.328,-7.284,-1.214]).orthogonal(Vector([-1.821,1.072,-2.940]))
  print "*"*10+"\n"
  print Vector([2.118,4.827]).parallel(Vector([0,0]))
  print Vector([2.118,4.827]).orthogonal(Vector([0,0]))
  print "-------------------"
  print Vector([3,4]).parallel(Vector([4.5,6.0]))
  print Vector([3,4]).parallel3(Vector([4.5,6.0]))
  
if __name__ == '__main__':
  vector_ex()