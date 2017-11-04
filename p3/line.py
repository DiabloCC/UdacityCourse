# -*- coding: utf-8 -*-

from vector import Vector
from decimal import Decimal, getcontext

getcontext().prec = 30

class Line(object):
  NO_NONEZERO_ELTS_FOUND_MSG = 'No nonezero elements found'
  
  def __init__(self, normal_vector=None, constant_term=None):
    self.dimension = 2
    
    if not normal_vector:
      all_zeros = ['0']*self.dimension
      normal_vector = Vector(all_zeros)
    self.normal_vector = normal_vector

