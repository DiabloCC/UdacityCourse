# -*- coding: utf-8 -*-

from decimal import Decimal, getcontext

from vector import Vector

getcontext().prec = 30


class Plane(object):

  NO_NONZERO_ELTS_FOUND_MSG = 'No nonzero elements found'

  def __init__(self, normal_vector=None, constant_term=None):
    self.dimension = 3

    if not normal_vector:
      all_zeros = ['0']*self.dimension
      normal_vector = Vector(all_zeros)
    self.normal_vector = normal_vector

    if not constant_term:
      constant_term = Decimal('0')
    self.constant_term = Decimal(constant_term)

    self.set_basepoint()


  def set_basepoint(self):
    try:
      n = self.normal_vector.coordinates
      c = self.constant_term
      basepoint_coords = ['0']*self.dimension

      initial_index = Plane.first_nonzero_index(n)
      initial_coefficient = n[initial_index]

      basepoint_coords[initial_index] = c/initial_coefficient
      self.basepoint = Vector(basepoint_coords)

    except Exception as e:
      if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
        self.basepoint = None
      else:
        raise e


  def __str__(self):

    num_decimal_places = 3

    def write_coefficient(coefficient, is_initial_term=False):
      coefficient = round(coefficient, num_decimal_places)
      if coefficient % 1 == 0:
        coefficient = int(coefficient)

      output = ''

      if coefficient < 0:
        output += '-'
      if coefficient > 0 and not is_initial_term:
        output += '+'

      if not is_initial_term:
        output += ' '

      if abs(coefficient) != 1:
        output += '{}'.format(abs(coefficient))

      return output

    n = self.normal_vector

    try:
      initial_index = Plane.first_nonzero_index(n)
      terms = [write_coefficient(n[i], is_initial_term=(i==initial_index)) + 'x_{}'.format(i+1)
           for i in range(self.dimension) if round(n[i], num_decimal_places) != 0]
      output = ' '.join(terms)

    except Exception as e:
      if str(e) == self.NO_NONZERO_ELTS_FOUND_MSG:
        output = '0'
      else:
        raise e

    constant = round(self.constant_term, num_decimal_places)
    if constant % 1 == 0:
      constant = int(constant)
    output += ' = {}'.format(constant)

    return output


  @staticmethod
  def first_nonzero_index(iterable):
    for k, item in enumerate(iterable):
      if not MyDecimal(item).is_near_zero():
        return k
    raise Exception(Plane.NO_NONZERO_ELTS_FOUND_MSG)

  def is_parallel_to(self, p):
    return self.normal_vector.is_parallel_to(p.normal_vector)
    
  def __eq__(self, p):
    if self.normal_vector.iszero():
      if not p.normal_vector.iszero():
        return False
      else:
        diff = self.constant_term - p.constant_term
        return MyDecimal(diff).is_near_zero()
    elif p.normal_vector.iszero():
      return False
      
    return (self.is_parallel_to(p) and 
            self.basepoint.minus(p.basepoint).is_orthogonal_to(self.normal_vector))
  
  def gaussian(self, p1, p2):
    n = [self.normal_vector, p1.normal_vector, p2.normal_vector]
    t = [self.constant_term, p1.constant_term, p2.constant_term]
    z = sorted([[first_nonzero_index(x[0])+list(x)] for x in zip(n,t)])
    for x in xrange(len(z)-1):
      i_1, n_1, k_1 = z[x]
      i_2, n_2, k_2 = z[x+1]
      if v_1.coordinates[i_2] != Decimal(0):
        c = n_1.coordinates[i_2] / n_2.coordinates[i_2]
        z[x+1] = [i_1 if i_1<i_2 else i_2+1,
                  n_1.minus(n_2.time_scalar(c)),
                  k_1-k_2*c]
      #z = sorted(z)

    
    
class MyDecimal(Decimal):
  def is_near_zero(self, eps=1e-10):
    return abs(self) < eps
