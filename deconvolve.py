#!/usr/bin/env python3
import cvxpy as cvx
import numpy as np
from constraints.spectral_hull_constraint import SpectralHullConstraint
from constraints.node_limit_constraint import NodeLimitConstraint
from graphs.graph import Graph

def deconvolve(n,A,A1,A2):
  '''
  n, number of mades/dimension of adjacency matrix
  A: Composition of A1 and A2, don't know labelling
  A1: Component of A
  A2: component of A
  '''
  A_matrix = Graph.create_adjacency_matrix(n,A)
  A1_matrix = Graph.create_adjacency_matrix(n,A1)
  A2_matrix = Graph.create_adjacency_matrix(n,A2)

  # Realisations of the precise labelling of A1 and A2
  A1_labelled = cvx.Symmetric(n)  
  A2_labelled = cvx.Symmetric(n)

  #A1_labelled = cvx.Int(n,n) 
  #A2_labelled = cvx.Int(n,n) 
  #ugly way to  make a variable be both symmetric and mixed integer, move to variable class SymmetricInt(n)
  #A1_symmetric = cvx.Symmetric(n)
  #A2_symmetric = cvx.Symmetric(n)
  #A1_labelled = A1_symmetric
  #A2_labelled = A2_symmetric  

  # objective function
  objective = cvx.Minimize(cvx.norm(A_matrix - A1_labelled - A2_labelled))

  # Constraint sets
  A1_hull = SpectralHullConstraint(A1_matrix, A1_labelled)
  A2_hull = SpectralHullConstraint(A2_matrix, A2_labelled)

  # all values between 0 and 1
  A1_limits = NodeLimitConstraint(A1_labelled,lower_limit=0, upper_limit=1)
  A2_limits = NodeLimitConstraint(A2_labelled,lower_limit=0, upper_limit=1)


  constraints = A1_hull.constraint_list + A2_hull.constraint_list + A1_limits.constraint_list + A2_limits.constraint_list 

  problem = cvx.Problem(objective,constraints)

  problem.solve(kktsolver='robust') #problem.solve(solver=cvx.CBC) or problem.solve(solver=cvx.GUROBI)


  # check correctness by looking at intersection of tangent cones for A1_labelled and A2_labelled
  # correct if and only if

  #  Tc(A1_labelled) ∩ - Tc(A2_labelled) ={0}

  if problem.status=='optimal':
    return problem.status,problem.value,A1_labelled.value,A2_labelled.value
  else:
    return problem.status,np.nan,np.nan,np.nan


if __name__ == '__main__':
  # A= K_4
  n = 4
  A=((0,1),(0,2),(0,3),(1,2),(1,3),(2,3),)

  # A1 = cycle 
  A1=((0,1),(1,2),(2,3),(3,0),)

  # A2 = cross joining all nodes
  A2=((0,2),(1,3),)

  status,problem_value,A1_star,A2_star= deconvolve(n,A,A1,A2)

  A_matrix = Graph.create_adjacency_matrix(n,A)

  print('Problem status: ',status)
  print('Norm value: ',problem_value)
  print('A:  \n', A_matrix)
  print('A1: \n', np.round(A1_star,5))
  print('A2: \n', np.round(A2_star,5))
  print('A1+A2: \n ', np.round(np.add(A1_star,A2_star),5))

