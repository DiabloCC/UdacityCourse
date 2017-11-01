from math import acos, pi, sqrt
from decimal import Decimal, getcontext

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

  def scalar_multiply(self, scalar):
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
      return self.scalar_multiply(Decimal(1.0)/self.magnitude())
      
  def dot_product(self, v):
    if not isinstance(v, Vector):
      raise TypeError('not a Vector')
    else:
      if self.dimension != v.dimension:
        raise ValueError('dimension not match.')
      else:
        return sum([x*y for x,y in zip(self.coordinates,v.coordinates)])            
  
  def inner_angle(self, v, in_degree=False, tolerance=1e-10):
    if not isinstance(v, Vector):
      raise TypeError('not a Vector')
    if self.dimension != v.dimension:
      raise ValueError('dimension not match.')
    d = self.normalize().dot_product(v.normalize())
    if abs(abs(d)-1) < tolerance:
      d = 1 if d>0 else -1
    if abs(d)<tolerance:
      d = 0
    if in_degree:
      return acos(d)/pi*180
    else:
      return acos(d)
      
  def parallel(self, v):
    if not isinstance(v, Vector):
      raise TypeError('not a Vector')
    if self.iszero() or v.iszero():
      return True
    v1 = self.normalize()
    v2 = v.normalize()
    return (v1.minus(v2).iszero() or 
            v1.plus(v2).iszero())
    
  def parallel2(self, v):
    if not isinstance(v, Vector):
      raise TypeError('not a Vector')
    if self.iszero() or v.iszero():
      return True
    return self.scalar_multiply(v.coordinates[0] / self.coordinates[0]).minus(v).iszero()
    
  def parallel3(self, v):
    if not isinstance(v, Vector):
      raise TypeError('not a Vector')
    return (self.iszero() or 
            v.iszero() or
            self.inner_angle(v) == 0 or
            self.inner_angle(v) == pi)
    
  def orthogonal(self, v, tolerance=1e-10):
    if not isinstance(v, Vector):
      raise TypeError('not a Vector')
    return abs(self.dot_product(v)) < tolerance