class Constraint(object):

  def __init__(self, constraint_list=[]):
    self.constraint_list=constraint_list

  def add_constraint(self, constraint):
    '''
    param
    constraint: list
    '''
    self.constraint_list+constraint
  

