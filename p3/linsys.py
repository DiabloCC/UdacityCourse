from decimal import Decimal, getcontext
from copy import deepcopy

from vector import Vector
from plane import Plane

getcontext().prec = 30


class LinearSystem(object):

  ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG = 'All planes in the system should live in the same dimension'
  NO_SOLUTIONS_MSG = 'No solutions'
  INF_SOLUTIONS_MSG = 'Infinitely many solutions'

  def __init__(self, planes):
    try:
      d = planes[0].dimension
      for p in planes:
        assert p.dimension == d

      self.planes = planes
      self.dimension = d

    except AssertionError:
      raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)


  def swap_rows(self, row1, row2):
    # pass # add your code here
    self[row1], self[row2] = self[row2], self[row1]

  def multiply_coefficient_and_row(self, coefficient, row):
    # pass # add your code here
    self[row] = Plane(normal_vector=self[row].normal_vector.time_scalar(coefficient),
                constant_term=self[row].constant_term*coefficient)

  def add_multiple_times_row_to_row(self, coefficient, row_to_add, row_to_be_added_to):
    # pass # add your code here
    n1 = self[row_to_add].normal_vector
    n2 = self[row_to_be_added_to].normal_vector
    k1 = self[row_to_add].constant_term
    k2 = self[row_to_be_added_to].constant_term
    
    new_normal_vector = n1.time_scalar(coefficient).plus(n2)
    new_constant_term = coefficient * k1 + k2
    
    self[row_to_be_added_to] = Plane(normal_vector=new_normal_vector,
                                     constant_term=new_constant_term)
                                     
  def compute_triangular_form(self):
    system = deepcopy(self)
    m = len(system)
    n = system.dimension
    j=0
    for i in range(m):
      while j<n:
        c = system[i].normal_vector[j]
        if c==Decimal(0):
          flag = False
          for k in range(i+1,m):
            if system[k].normal_vector[j] != Decimal(0):
              system.swap_rows(i,k)
              flag = True
              break
          if not flag:
            j += 1
        else:
          for k in range(i+1,m):
            system.add_multiple_times_row_to_row(-system[k].normal_vector[j]/c,i,k)
          j += 1
          break
    return system
    
  def compute_rref(self):
    tf = self.compute_triangular_form()
    indices = tf.indices_of_first_nonzero_terms_in_each_row()
    
    for i in reversed(range(len(self))):
      if indices[i] < 0:
        continue
      c = Decimal(1.0)/tf[i].normal_vector[indices[i]]
      tf.multiply_coefficient_and_row(c,i)
      for k in reversed(range(i)):
        c = tf[k].normal_vector[indices[i]]
        if MyDecimal(c).is_near_zero():
          continue
        tf.add_multiple_times_row_to_row(-c,i,k) 
        
    return tf
    
  def indices_of_first_nonzero_terms_in_each_row(self):
    num_equations = len(self)
    num_variables = self.dimension

    indices = [-1] * num_equations

    for i,p in enumerate(self.planes):
      try:
        indices[i] = p.first_nonzero_index(p.normal_vector.coordinates)
      except Exception as e:
        if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
          continue
        else:
          raise e

    return indices

  def compute_solution(self):
    try:
      # return self.do_gaussian_elimination()
      return self.do_gaussian_elimination_and_parametrize_solution()
    except Exception as e:
      # if (str(e) == self.NO_SOLUTIONS_MSG or
      #    str(e) == self.INF_SOLUTIONS_MSG):
      if str(e) == self.NO_SOLUTIONS_MSG:
          return str(e)
      else:
        raise e
  
  def do_gaussian_elimination_and_parametrize_solution(self):
    rref = self.compute_rref()
    # print rref
    rref.raise_exception_if_contradictory_equation()
    
    direction_vectors = rref.extract_direction_vectors_for_parametrization()
    basepoint = rref.extract_basepoint_for_parametrization()
    
    return Parametrization(basepoint, direction_vectors)
    
    # num_variables = rref.dimension
    # solution_coordinates = [x.constant_term for x in rref.planes]
    # return Vector(solution_coordinates)
    
  def extract_direction_vectors_for_parametrization(self):
    num_variables = self.dimension
    pivot_indices = self.indices_of_first_nonzero_terms_in_each_row()
    free_variable_indices = set(range(num_variables)) - set(pivot_indices)
    
    direction_vectors = []
    
    for free_var in free_variable_indices:
      vector_coords = [0] * num_variables
      vector_coords[free_var] = 1
      for i, p in enumerate(self.planes):
        pivot_var = pivot_indices[i]
        if pivot_var < 0:
          break
        vector_coords[pivot_var] = -p.normal_vector[free_var]
      direction_vectors.append(Vector(vector_coords))
      
    return direction_vectors
    
  def extract_basepoint_for_parametrization(self):
    num_variables = self.dimension
    pivot_indices = self.indices_of_first_nonzero_terms_in_each_row()
    
    basepoint = [0] * num_variables
    
    for i, p in enumerate(self.planes):
      pivot_var = pivot_indices[i]
      if pivot_var < 0:
        break
      basepoint[pivot_var] = p.constant_term
    return Vector(basepoint)
  
  def raise_exception_if_contradictory_equation(self):
    for p in self.planes:
      try:
        p.first_nonzero_index(p.normal_vector)
      except Exception as e:
        if str(e) == 'No nonezero elements found':
          constant_term = MyDecimal(p.constant_term)
          if not constant_term.is_near_zero():
            raise Exception(self.NO_SOLUTIONS_MSG)
        else:
          raise e

  def __len__(self):
    return len(self.planes)

  def __getitem__(self, i):
    return self.planes[i]

  def __setitem__(self, i, x):
    try:
      assert x.dimension == self.dimension
      self.planes[i] = x

    except AssertionError:
      raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)

  def __str__(self):
    ret = 'Linear System:\n'
    temp = ['Equation {}: {}'.format(i+1,p) for i,p in enumerate(self.planes)]
    ret += '\n'.join(temp)
    return ret

class MyDecimal(Decimal):
  def is_near_zero(self, eps=1e-10):
    return abs(self) < eps

class Parametrization(object):
  BASEPT_AND_DIR_VECTORS_MUST_BE_IN_SAME_DIM_MSG = (
    'The basepoint and direction vectors should all live in the same dimensionion')
    
  def __init__(self, basepoint, direction_vectors):
    self.basepoint = basepoint
    self.direction_vectors = direction_vectors
    self.dimension = self.basepoint.dimension
    
    try:
      for v in direction_vectors:
        assert v.dimension == self.dimension
    except AssertionError:
      raise Exception(BASEPT_AND_DIR_VECTORS_MUST_BE_IN_SAME_DIM_MSG)

  def __str__(self):
    num_decimal_places = 3
    
    ret = 'Parametrization Form:\n'
    for i in range(self.dimension):
      temp = 'X_{} = {}'.format(i+1, round(self.basepoint[i],num_decimal_places))
      for j in range(len(self.direction_vectors)):
        if not MyDecimal(self.direction_vectors[j][i]).is_near_zero():
          temp = (temp + '+ {} t_{}').format(round(self.direction_vectors[j][i],num_decimal_places), j+1)
      ret = ret + temp + '\n'
     
    return ret
       

