############################################################################################################################################################################################################
  # complete graph, K_4, not appropriate for deconvolve?

  # A= K_4
  n = 4
  A=((0,1),(0,2),(0,3),(1,2),(1,3),(2,3),)

  # A1 = cycle 
  A1=((0,1),(1,2),(2,3),(3,0),)

  # A2 = cross joining all nodes
  A2=((0,2),(1,3),)


############################################################################################################################################################################################################
  # Clebsch graph with noise 

 # labelling of nodes from, http://www.ioirp.com/Doc/IJIRTSE/v1_i3/JMS105.pdf 
  n=16
  #  check size(A) = size(A1)+ size(A2)
  A = ((0,1),(0,4),(0,7),(0,9),(0,10),(1,2),(1,5),(1,8),(1,11),(2,3),(2,6),(2,9),(2,12),(3,4),(3,5),(3,7),(3,13),(4,6),(4,8),(4,14),(5,10),(5,14),(5,15),(6,10),(6,11),(6,15),(7,11),(7,12),(7,15),(8,12),(8,13),(8,15),(9,13),(9,14),(9,15),(10,12),(10,13),(11,13),(11,14),(12,14),(0,5),(5,13),(13,14),(14,6),(6,1),(1,7),(7,2),(2,8),(8,11),(11,15),(15,10),(10,9),(9,4),(4,12),(12,3),(3,0),)
  
  #16 cycle
  A1 = ((0,5),(5,13),(13,14),(14,6),(6,1),(1,7),(7,2),(2,8),(8,11),(11,15),(15,10),(10,9),(9,4),(4,12),(12,3),(3,0),)

  #clebsch graph
  A2=((0,1),(0,4),(0,7),(0,9),(0,10),(1,2),(1,5),(1,8),(1,11),(2,3),(2,6),(2,9),(2,12),(3,4),(3,5),(3,7),(3,13),(4,6),(4,8),(4,14),(5,10),(5,14),(5,15),(6,10),(6,11),(6,15),(7,11),(7,12),(7,15),(8,12),(8,13),(8,15),(9,13),(9,14),(9,15),(10,12),(10,13),(11,13),(11,14),(12,14),)

  #clebsch graph, in visual order
  #A2=((0,1),(0,4),(0,7),(0,9),(0,10),
     # (1,2),(1,5),(1,8),(1,11),
     # (2,3),(2,6),(2,9),(2,12),
     # (3,4),(3,5),(3,7),(3,13),
     # (4,6),(4,8),(4,14),
     # (5,10),(5,14),(5,15),
     # (6,10),(6,11),(6,15),
     # (7,11),(7,12),(7,15),
     # (8,12),(8,13),(8,15),
     # (9,13),(9,14),(9,15),
     # (10,12),(10,13),
     # (11,13),(11,14),(12,14),)

############################################################################################################################################################################################################
  # Shrikande graph with noise

  n=16
  # convolved graphs
  A=((7,1),(1,3),(3,5),(5,0),(0,2),(2,4),(4,6),(6,14),(14,13),(13,12),(12,11),(11,10),(10,9),(9,8),(8,15),(0,1),(0,2),(0,6),(0,7),(0,9),(0,15),(1,2),(1,3),(1,7),(1,8),(1,10),(2,3),(2,4),(2,9),(2,11),(3,4),(3,5),(3,10),(3,12),(4,5),(4,6),(4,11),(4,13),(5,6),(5,7),(5,12),(5,14),(6,7),(6,13),(6,15),(7,8),(7,14),(8,10),(8,11),(8,13),(8,14),(9,11),(9,12),(9,14),(9,15),(10,12),(10,13),(10,15),(11,13),(11,14),(12,14),(12,15),(13,15),)

  # 16 cycle
  A1=((7,1),(1,3),(3,5),(5,0),(0,2),(2,4),(4,6),(6,14),(14,13),(13,12),(12,11),(11,10),(10,9),(9,8),(8,15),(15,7),)

  # shrikande graph
  A2=((0,1),(0,2),(0,6),(0,7),(0,9),(0,15),(1,2),(1,3),(1,7),(1,8),(1,10),(2,3),(2,4),(2,9),(2,11),(3,4),(3,5),(3,10),(3,12),(4,5),(4,6),(4,11),(4,13),(5,6),(5,7),(5,12),(5,14),(6,7),(6,13),(6,15),(7,8),(7,14),(8,10),(8,11),(8,13),(8,14),(9,11),(9,12),(9,14),(9,15),(10,12),(10,13),(10,15),(11,13),(11,14),(12,14),(12,15),(13,15),)

