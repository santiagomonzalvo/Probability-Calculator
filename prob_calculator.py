import copy
import random
# Consider using the modules imported above.


class Hat:

  def __init__(self, **kwargs):
    self.contents = []
    for color, count in kwargs.items():
      self.contents.extend([color] * count)

  def draw(self, num_balls):
    drawn_balls = []
    if num_balls >= len(self.contents):
      drawn_balls = self.contents.copy()
      self.contents.clear()
    else:
      for _ in range(num_balls):
        ball_index = random.randint(0, len(self.contents) - 1)
        drawn_balls.append(self.contents.pop(ball_index))
    return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  quantity = 0
  #----------For each experiment...
  for _ in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    drawn_balls = hat_copy.draw(num_balls_drawn)
    drawn_balls_dict = {}
    for ball in drawn_balls:
      drawn_balls_dict[ball] = drawn_balls_dict.get(ball, 0) + 1
    #----------Verification
    match = True
    for color, count in expected_balls.items():
      if drawn_balls_dict.get(color, 0) < count:
        match = False
        break

    if match:
      quantity += 1

  return quantity / num_experiments
