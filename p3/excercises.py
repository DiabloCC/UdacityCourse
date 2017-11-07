# -*- coding: utf-8 -*-

from vector import *
from line import *

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
  # print Vector([7.887,4.138]).dot(Vector([-8.802,6.776]))
  # print Vector([-5.955,-4.904,-1.874]).dot(Vector([-4.496,-8.755,7.103]))
  # print Vector([3.183,-7.627]).angle_with(Vector([-2.668,5.319]))
  # print Vector([7.350,0.221,5.188]).angle_with(Vector([2.751,8.259,3.985]), True)

  # 10
  # print "*"*10
  # print Vector([-7.579,-7.880]).is_parallel_to(Vector([22.737,23.640]))
  # print Vector([-7.579,-7.880]).is_parallel_to2(Vector([22.737,23.640]))
  # print Vector([-7.579,-7.880]).is_parallel_to3(Vector([22.737,23.640]))
  # print "-"*10
  # print Vector([-7.579,-7.880]).is_orthogonal_to(Vector([22.737,23.640]))
  # print "*"*10+"\n"
  # print Vector([-2.029,9.970,4.172]).is_parallel_to(Vector([-9.231,-6.639,-7.245]))
  # print Vector([-2.029,9.970,4.172]).is_parallel_to2(Vector([-9.231,-6.639,-7.245]))
  # print Vector([-2.029,9.970,4.172]).is_parallel_to3(Vector([-9.231,-6.639,-7.245]))
  # print "-"*10
  # print Vector([-2.029,9.970,4.172]).is_orthogonal_to(Vector([-9.231,-6.639,-7.245]))
  # print "*"*10+"\n"
  # print Vector([-2.328,-7.284,-1.214]).is_parallel_to(Vector([-1.821,1.072,-2.940]))
  # print Vector([-2.328,-7.284,-1.214]).is_parallel_to2(Vector([-1.821,1.072,-2.940]))
  # print Vector([-2.328,-7.284,-1.214]).is_parallel_to3(Vector([-1.821,1.072,-2.940]))
  # print "-"*10
  # print Vector([-2.328,-7.284,-1.214]).is_orthogonal_to(Vector([-1.821,1.072,-2.940]))
  # print "*"*10+"\n"
  # print Vector([2.118,4.827]).is_orthogonal_to(Vector([0,0]))
  # print "-------------------"
  # print Vector([3,4]).parallel(Vector([4.5,6.0]))
  # print Vector([3,4]).parallel3(Vector([4.5,6.0]))

  # 12
  # print Vector([3.039, 1.879]).componet_project_to(Vector([0.825, 2.036]))
  # print Vector([-9.880, -3.264, -8.159]).componet_project_to(Vector([-2.155, -9.353, -9.473]))
  # print Vector([-9.880, -3.264, -8.159]).component_orthogonal_to(Vector([-2.155,-9.353, -9.473]))
  # print Vector([3.009, -6.172, 3.692, -2.510]).componet_project_to(Vector([6.404, -9.144, 2.759, 8.718]))
  # print Vector([3.009, -6.172, 3.692, -2.510]).component_orthogonal_to(Vector([6.404, -9.144, 2.759, 8.718]))

  # 14
  # print Vector([8.462,7.893,-8.187]).cross(Vector([6.984,-5.975,4.778]))
  # print Vector([-8.987,-9.838,5.031]).parallelogram_area(Vector([-4.268,-1.861,-8.866]))
  # print Vector([1.500,9.547,3.691]).parallelogram_area(Vector([-6.007,0.124,5.772]))/2
  pass
  
def line_ex():
  # 4
  print Line(Vector([4.046,2.836]),1.210).is_parallel_to(Line(Vector([10.115,7.090]),3.025))
  # print Line(Vector([10.115,7.090]),3.025).direction_vector() 
  print Line(Vector([4.046,2.836]),1.210) == Line(Vector([10.115,7.090]),3.025)
  print Line(Vector([4.046,2.836]),1.210).intersection_point(Line(Vector([10.115,7.090]),3.025))
  print "-"*10
  print Line(Vector([7.204,3.182]),8.680).is_parallel_to(Line(Vector([8.172,4.114]),9.883))
  print Line(Vector([7.204,3.182]),8.680) == Line(Vector([8.172,4.114]),9.883)
  print Line(Vector([7.204,3.182]),8.680).intersection_point(Line(Vector([8.172,4.114]),9.883))
  print "-"*10
  print Line(Vector([1.182,5.562]),6.744).is_parallel_to(Line(Vector([1.773,8.343]),9.525))
  print Line(Vector([1.182,5.562]),6.744) == Line(Vector([1.773,8.343]),9.525)
  print Line(Vector([1.182,5.562]),6.744).intersection_point(Line(Vector([1.773,8.343]),9.525))
  print "-"*10
  
if __name__ == '__main__':
  # vector_ex()
  line_ex()
