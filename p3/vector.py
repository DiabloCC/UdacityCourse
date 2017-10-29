class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates
        
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
      if not (isinstance(scalar, int) or isinstance(scalar, float)):
        raise TypeError('{0} is not a number'.format(scalar))
      else:
        return Vector([scalar * x for x in self.coordinates])
