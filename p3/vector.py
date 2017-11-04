# -*- coding: utf-8 -*-

from math import acos, pi, sqrt
from decimal import Decimal, getcontext

getcontext().prec = 30

class Vector(object):
  def __init__(self, coordinates):
    try:
      if not coordinates:
          raise ValueError
      self.coordinates = tuple([Decimal(x) for x in coordinates])
      self.dimension = len(coordinates)

    except ValueError:
      raise ValueError('The coordinates must be nonempty')

    except TypeError:
      raise TypeError('The coordinates must be an iterable')

  def __str__(self):
    return 'Vector: {}'.format(self.coordinates)

  def __eq__(self, v):
    return self.coordinates == v.coordinates
  
  def iszero(self, tolerance=1e-10):
    return self.magnitude()<tolerance
      
  def plus(self, v):
    if isinstance(v, Vector):
      if self.dimension == v.dimension :
        return Vector([x+y for x, y in zip(self.coordinates, v.coordinates)])
      else:
        raise ValueError('dimension not match.')
    else:
      raise TypeError('not a Vector.')

  def minus(self, v):
    if isinstance(v, Vector):
      if self.dimension == v.dimension :
        return Vector([x-y for x, y in zip(self.coordinates, v.coordinates)])
      else:
        raise ValueError('dimension not match.')
    else:
      raise TypeError('not a Vector.')

  def time_scalar(self, scalar):
    try:
      return Vector([Decimal(scalar) * x for x in self.coordinates])
    except Exception:
      raise TypeError('{0} is not a number'.format(scalar))
      
  def magnitude(self):
      return Decimal(sqrt(sum([x**2 for x in self.coordinates])))
      
  def normalize(self):
    if self.iszero():
      raise ValueError("Can't normalize a zero vector.")
    else:
      return self.time_scalar(Decimal(1.0)/self.magnitude())
      
  def dot(self, v):
    if not isinstance(v, Vector):
      raise TypeError('not a Vector')
    else:
      if self.dimension != v.dimension:
        raise ValueError('dimension not match.')
      else:
        return sum([x*y for x,y in zip(self.coordinates,v.coordinates)])            
  
  def angle_with(self, v, in_degree=False, tolerance=1e-10):
    if not isinstance(v, Vector):
      raise TypeError('not a Vector')
    if self.dimension != v.dimension:
      raise ValueError('dimension not match.')
    d = self.normalize().dot(v.normalize())
    if abs(abs(d)-1) < tolerance:
      d = 1 if d>0 else -1
    if abs(d)<tolerance:
      d = 0
    if in_degree:
      return acos(d)/pi*180
    else:
      return acos(d)
      
  def is_parallel_to(self, v):
    if not isinstance(v, Vector):
      raise TypeError('not a Vector')
    if self.iszero() or v.iszero():
      return True
    v1 = self.normalize()
    v2 = v.normalize()
    return (v1.minus(v2).iszero() or 
            v1.plus(v2).iszero())
    
  def is_parallel_to2(self, v):
    if not isinstance(v, Vector):
      raise TypeError('not a Vector')
    if self.iszero() or v.iszero():
      return True
    return self.time_scalar(v.coordinates[0] / self.coordinates[0]).minus(v).iszero()
    
  def is_parallel_to3(self, v):
    if not isinstance(v, Vector):
      raise TypeError('not a Vector')
    return (self.iszero() or 
            v.iszero() or
            self.angle_with(v) == 0 or
            self.angle_with(v) == pi)
    
  def is_orthogonal_to(self, v, tolerance=1e-10):
    if not isinstance(v, Vector):
      raise TypeError('not a Vector')
    return abs(self.dot(v)) < tolerance

  def component_project_to(self, v):
    if not isinstance(v, Vector):
      raise TypeError('not a Vector')
    return v.normalize().time_scalar(self.dot(v.normalize()))

  def component_orthogonal_to(self, v):
    if not isinstance(v, Vector):
      raise TypeError('not a Vector')
    return self.minus(self.project(v))
    
  def cross(self, v):
    if not isinstance(v, Vector):
      raise TypeError('not a Vector')
    r = []
    if ((self.dimension != v.dimension) or
        (self.dimension == 1) or
        (v.dimension == 1)):
      raise ValueError('dimensions not match')
    if (self.dimension == v.dimension == 2):
      z1 = z2 = Decimal(0.0)
    if (self.dimension == v.dimension == 3):
      z1 = self.coordinates[2]
      z2 = v.coordinates[2]
    r.append(self.coordinates[1]*z2 - v.coordinates[1]*z1)
    r.append(v.coordinates[0]*z1 - self.coordinates[0]*z2)
    r.append(self.coordinates[0]*v.coordinates[1] - v.coordinates[0]*self.coordinates[1])
    return Vector(r)
    
    
  def parallelogram_area(self, v):
    if not isinstance(v, Vector):
      raise TypeError('not a Vector')
    return self.cross(v).magnitude()
      
