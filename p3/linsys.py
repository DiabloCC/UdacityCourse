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
    for i in xrange(m):
      while j<n:
        c = system[i].normal_vector.coordinates[j]
        if c==Decimal(0):
          flag = False
          for k in xrange(i+1,m):
            if system[k].normal_vector.coordinates[j] != Decimal(0):
              system.swap_rows(i,k)
              flag = True
              break
          if not flag:
            j += 1
        else:
          for k in xrange(i+1,m):
            system.add_multiple_times_row_to_row(-system[k].normal_vector.coordinates[j]/c,i,k)
          j += 1
          break
         
    return system
    
  def compute_rref(self):
    tf = self.compute_triangular_form()
    indices = tf.indices_of_first_nonzero_terms_in_each_row()
    
    for i in reversed(range(len(self))):
      if indices[i] < 0:
        continue
      c = tf[i].normal_vector[indices[i]]
      if not MyDecimal(abs(c) - 1).is_near_zero():
        c = Decimal(1)/c
        tf.multiply_coefficient_and_row(c,i)
      for k in range(i-1,-1, -1):
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






# print MyDecimal('1e-9').is_near_zero()
# print MyDecimal('1e-11').is_near_zero()

def test_row_func():
  p0 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
  p1 = Plane(normal_vector=Vector(['0','1','0']), constant_term='2')
  p2 = Plane(normal_vector=Vector(['1','1','-1']), constant_term='3')
  p3 = Plane(normal_vector=Vector(['1','0','-2']), constant_term='2')

  s = LinearSystem([p0,p1,p2,p3])
  print s.indices_of_first_nonzero_terms_in_each_row()
  print '{},{},{},{}'.format(s[0],s[1],s[2],s[3])
  print len(s)
  print s
  print "-"*20
 
  s.swap_rows(0,1)
  if not (s[0]==p1 and s[1]==p0 and s[2]==p2 and s[3]==p3):
    print 'test case 1 failed'
  else:
    print 'test case 1 success'
    
  s.swap_rows(1,3)
  if not (s[0] == p1 and s[1] == p3 and s[2] == p2 and s[3] == p0):
    print 'test case 2 failed'
  else:
    print 'test case 2 success'

  s.swap_rows(3,1)
  if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
    print 'test case 3 failed'
  else:
    print 'test case 3 success'

  s.multiply_coefficient_and_row(1,0)
  if not (s[0] == p1 and s[1] == p0 and s[2] == p2 and s[3] == p3):
    print 'test case 4 failed'
  else:
    print 'test case 4 success'

  s.multiply_coefficient_and_row(-1,2)
  if not (s[0] == p1 and
          s[1] == p0 and
          s[2] == Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3') and
          s[3] == p3):
    print 'test case 5 failed'
  else:
    print 'test case 5 success'

  s.multiply_coefficient_and_row(10,1)
  if not (s[0] == p1 and
          s[1] == Plane(normal_vector=Vector(['10','10','10']), constant_term='10') and
          s[2] == Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3') and
          s[3] == p3):
    print 'test case 6 failed'
  else:
    print 'test case 6 success'

  s.add_multiple_times_row_to_row(0,0,1)
  if not (s[0] == p1 and
          s[1] == Plane(normal_vector=Vector(['10','10','10']), constant_term='10') and
          s[2] == Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3') and
          s[3] == p3):
    print 'test case 7 failed'
  else:
    print 'test case 7 success'

  s.add_multiple_times_row_to_row(1,0,1)
  if not (s[0] == p1 and
          s[1] == Plane(normal_vector=Vector(['10','11','10']), constant_term='12') and
          s[2] == Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3') and
          s[3] == p3):
    print 'test case 8 failed'
  else:
    print 'test case 8 success'

  s.add_multiple_times_row_to_row(-1,1,0)
  if not (s[0] == Plane(normal_vector=Vector(['-10','-10','-10']), constant_term='-10') and
          s[1] == Plane(normal_vector=Vector(['10','11','10']), constant_term='12') and
          s[2] == Plane(normal_vector=Vector(['-1','-1','1']), constant_term='-3') and
          s[3] == p3):
    print 'test case 9 failed'
  else:
    print 'test case 9 success'
    
def test_compute_triangle():
  # p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
  # p2 = Plane(normal_vector=Vector(['0','1','1']), constant_term='2')
  # s = LinearSystem([p1,p2])
  # print s
  # print "-"*20
  # 
  # t = s.compute_triangular_form()
  # print t
  # if not (t[0] == p1 and
  #   t[1] == p2):
  #   print 'test case 1 failed'

  # p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
  # p2 = Plane(normal_vector=Vector(['1','1','1']), constant_term='2')
  # s = LinearSystem([p1,p2])
  # t = s.compute_triangular_form()
  # print t
  # if not (t[0] == p1 and
  #   t[1] == Plane(constant_term='1')):
  #   print 'test case 2 failed'
  # 
  # p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
  # p2 = Plane(normal_vector=Vector(['0','1','0']), constant_term='2')
  # p3 = Plane(normal_vector=Vector(['1','1','-1']), constant_term='3')
  # p4 = Plane(normal_vector=Vector(['1','0','-2']), constant_term='2')
  # s = LinearSystem([p1,p2,p3,p4])
  # t = s.compute_triangular_form()
  # print t
  # if not (t[0] == p1 and
  #   t[1] == p2 and
  #   t[2] == Plane(normal_vector=Vector(['0','0','-2']), constant_term='2') and
  #   t[3] == Plane()):
  #   print 'test case 3 failed'
  # 
  p1 = Plane(normal_vector=Vector(['0','1','1']), constant_term='1')
  p2 = Plane(normal_vector=Vector(['1','-1','1']), constant_term='2')
  p3 = Plane(normal_vector=Vector(['1','2','-5']), constant_term='3')
  s = LinearSystem([p1,p2,p3])
  t = s.compute_triangular_form()
  print t
  if not (t[0] == Plane(normal_vector=Vector(['1','-1','1']), constant_term='2') and
    t[1] == Plane(normal_vector=Vector(['0','1','1']), constant_term='1') and
    t[2] == Plane(normal_vector=Vector(['0','0','-9']), constant_term='-2')):
    print 'test case 4 failed'
  
def test_reef():
  # p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
  # p2 = Plane(normal_vector=Vector(['0','1','1']), constant_term='2')
  # s = LinearSystem([p1,p2])
  # r = s.compute_rref()
  # if not (r[0] == Plane(normal_vector=Vector(['1','0','0']), constant_term='-1') and
  #     r[1] == p2):
  #   print 'test case 1 failed'

  # p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
  # p2 = Plane(normal_vector=Vector(['1','1','1']), constant_term='2')
  # s = LinearSystem([p1,p2])
  # r = s.compute_rref()
  # if not (r[0] == p1 and
  #     r[1] == Plane(constant_term='1')):
  #   print 'test case 2 failed'
  # 
  # p1 = Plane(normal_vector=Vector(['1','1','1']), constant_term='1')
  # p2 = Plane(normal_vector=Vector(['0','1','0']), constant_term='2')
  # p3 = Plane(normal_vector=Vector(['1','1','-1']), constant_term='3')
  # p4 = Plane(normal_vector=Vector(['1','0','-2']), constant_term='2')
  # s = LinearSystem([p1,p2,p3,p4])
  # r = s.compute_rref()
  # if not (r[0] == Plane(normal_vector=Vector(['1','0','0']), constant_term='0') and
  #     r[1] == p2 and
  #     r[2] == Plane(normal_vector=Vector(['0','0','-2']), constant_term='2') and
  #     r[3] == Plane()):
  #   print 'test case 3 failed'
  # 
  p1 = Plane(normal_vector=Vector(['0','1','1']), constant_term='1')
  p2 = Plane(normal_vector=Vector(['1','-1','1']), constant_term='2')
  p3 = Plane(normal_vector=Vector(['1','2','-5']), constant_term='3')
  s = LinearSystem([p1,p2,p3])
  r = s.compute_rref()
  if not (r[0] == Plane(normal_vector=Vector(['1','0','0']), constant_term=Decimal('23')/Decimal('9')) and
      r[1] == Plane(normal_vector=Vector(['0','1','0']), constant_term=Decimal('7')/Decimal('9')) and
      r[2] == Plane(normal_vector=Vector(['0','0','1']), constant_term=Decimal('2')/Decimal('9'))):
    print 'test case 4 failed'
    
if __name__=="__main__":
  # test_row_func()
  # test_compute_triangle()
  test_reef()


