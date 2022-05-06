import random
import math    
import copy 
import sys   
import numpy as np  

def error(position):
  err = 0.0
  for i in range(len(position)):
    xi = position[i]
    err += (xi * xi) - (10 * math.cos(2 * math.pi * xi)) + 10
  return err


class Particle:
  def __init__(self, dim, minx, maxx, seed):
    self.position = [0.0 for i in range(dim)]
    self.velocity = [0.0 for i in range(dim)]
    for i in range(dim):
      self.position[i] = ((maxx - minx) *
        np.random.standard_normal(size=1)[0] + minx)
      self.velocity[i] = ((maxx - minx) *
        np.random.standard_normal(size=1)[0] + minx)

    self.error = error(self.position)
    self.pbest_pos = copy.copy(self.position) 
    self.pbest_err = self.error 

def Solve(max_epochs, n, dim, minx, maxx):
  swarm = [Particle(dim, minx, maxx, i) for i in range(n)] 

  gbest_pos = [0.0 for i in range(dim)]
  gbest_err = sys.float_info.max 

  for i in range(n):
    if swarm[i].error < gbest_err:
      gbest_err = swarm[i].error
      gbest_pos = copy.copy(swarm[i].position) 

  epoch = 0
  w = 0.729 
  c1 = 2 
  c2 = 2 

  while epoch < max_epochs:
    
    if epoch % 10 == 0 and epoch > 1:
      print("Epoch = " + str(epoch) +
        ", Best error is= %.3f" % gbest_err)

    for i in range(n): 
      for k in range(dim): 
        r1 = random.random()   
        r2 = random.random()

        swarm[i].velocity[k] = ( (w * swarm[i].velocity[k]) +
          (c1 * r1 * (swarm[i].pbest_pos[k] -
          swarm[i].position[k])) +  
          (c2 * r2 * (gbest_pos[k] -
          swarm[i].position[k])))  

        if swarm[i].velocity[k] < minx:
          swarm[i].velocity[k] = minx
        elif swarm[i].velocity[k] > maxx:
          swarm[i].velocity[k] = maxx
        swarm[i].position[k] += swarm[i].velocity[k]
  
      swarm[i].error = error(swarm[i].position)

      if swarm[i].error < swarm[i].pbest_err:
        swarm[i].pbest_err = swarm[i].error
        swarm[i].pbest_pos = copy.copy(swarm[i].position)

      if swarm[i].error < gbest_err:
        gbest_err = swarm[i].error
        gbest_pos = copy.copy(swarm[i].position)
    
    epoch += 1
  return gbest_pos

dim = 3

num_particles = 50
max_epochs = 100
print("Particel Swarm Optimization for Rastrigin Function")
print("Total Number of particles = " + str(num_particles))
print("Total epochs = " + str(max_epochs))
print("")
best_position = Solve(max_epochs, num_particles,
 dim, -10.0, 10.0)

print("\nBest solution found:")
print(best_position)
err = error(best_position)
print("Error of best solution = %.6f" % err)
print("")