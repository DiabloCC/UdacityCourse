# -*- coding: utf-8 -*-

from vector import *
from line import *
from plane import *
from linsys import LinearSystem, Parametrization

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
  
def plane_ex():
  # 7
  a = Plane(Vector([-0.412,3.806,0.728]),-3.460) 
  b = Plane(Vector([1.030,-9.515,-1.820]),8.650)
  print a == b
  print a.is_parallel_to(b) and not (a == b)
  print not a.is_parallel_to(b)
  print "-"*10
  a = Plane(Vector([2.611,5.528,0.283]),4.600) 
  b = Plane(Vector([7.715,8.306,5.342]),3.760)
  print a == b
  print a.is_parallel_to(b) and not (a == b)
  print not a.is_parallel_to(b)
  print "-"*10
  a = Plane(Vector([-7.926,8.625,-7.212]),-7.952) 
  b = Plane(Vector([-2.642,2.875,-2.404]),-2.443)
  print a == b
  print a.is_parallel_to(b) and not (a == b)
  print not a.is_parallel_to(b)
  print "-"*10
  
def parametrization_ex():
  # p1 = Plane(Vector([0.786,0.786,0.588]),-0.714)
  # p2 = Plane(Vector([-0.138,-0.138,0.244]),0.319)
  # s = LinearSystem([p1,p2])
  # print s
  # try:
  #   print s.compute_solution()
  # except Exception as e:
  #   print str(e)
  
  p1 = Plane(Vector([8.631,5.112,-1.816]),-5.113)
  p2 = Plane(Vector([4.315,11.132,-5.270]),-6.775) 
  p3 = Plane(Vector([-2.158,3.010,-1.727]),-0.831)
  s = LinearSystem([p1,p2,p3])
  print s
  try:
    print s.compute_solution()
  except Exception as e:
    print str(e)
  # 
  # p1 = Plane(Vector([-0.935,1.760,-9.365]),-9.955)
  # p2 = Plane(Vector([0.187,0.352,-1.873]),-1.991) 
  # p3 = Plane(Vector([0.374,0.704,-3.746]),-3.982)
  # p4 = Plane(Vector([-0.561,-1.056,5.619]),5.973)
  # s = LinearSystem([p1,p2,p3,p4])
  # print s
  # try:
  #   print s.compute_solution()
  # except Exception as e:
  #   print str(e)
  
  
if __name__ == '__main__':
  # vector_ex()
  # line_ex()
  # plane_ex()
  parametrization_ex()
