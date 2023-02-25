import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self,**kwargs):
    self.contents=[]
    for k,v in kwargs.items():
      for i in range(v):
        self.contents.append(k)
    print(self.contents)

  def draw(self,num):
    n=min(num,len(self.contents))
    return [self.contents.pop(random.randrange(len(self.contents))) for _ in range(n)]
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  count=0
  for i in range(num_experiments):
    expected_copy=copy.deepcopy(expected_balls)
    hat_copy=copy.deepcopy(hat)
    balls_drawn=hat_copy.draw(num_balls_drawn)
    for balls in balls_drawn:
      if balls in expected_copy:
        expected_copy[balls]-=1

    if(all(x<=0 for x in expected_copy.values())):
      count+=1
  return count/num_experiments
    
    
    
  
  
