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
    
    def iszero(self):
      return self.coordinates == tuple([Decimal(0.0)] * self.dimension)
        
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
      if self.iszero():
        return 0
      else:
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
    
    def inner_angle(self, v, in_degree=False):
      if not isinstance(v, Vector):
        raise TypeError('not a Vector')
      if self.dimension != v.dimension:
        raise ValueError('dimension not match.')
      ret = acos(self.normalize().dot_product(v.normalize()))
      if in_degree:
        return ret/pi*180
      else:
        return ret