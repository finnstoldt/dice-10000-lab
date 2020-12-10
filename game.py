import random

def roll_dice(n_dice):
  dice_rolls = { 1:0, 2:0, 3:0, 4:0, 5:0, 6:0 }
  for _ in range(n_dice):
    dice_rolls[random.randint(1,6)] += 1
  return dice_rolls

def evaluate(dice_rolls, score):
  paths = []
  
  # straight
  if dice_rolls == { 1:1, 2:1, 3:1, 4:1, 5:1, 6:1 }:
    rec_turn = play_turn()
    paths.append((0,1500 + rec_turn if rec_turn != 0 else 0))
  # 3 pairs
  if sum([1 if dice_rolls[k] == 2 else 0 for k in dice_rolls]) == 3:
    rec_turn = play_turn()
    paths.append((0,1500 + rec_turn if rec_turn != 0 else 0))
  # x*y's
  for i in range(1,6):
    f = 10 if i == 1 else 1
    if dice_rolls[i] >= 1 and (i == 1 or i == 5):
      paths.append((5,1*i*10*f))
    if dice_rolls[i] >= 2 and (i == 1 or i == 5):
      paths.append((4,2*i*10*f))
    if dice_rolls[i] >= 3:
      paths.append((3,1*i*100*f))
    if dice_rolls[i] >= 4:
      paths.append((2,2*i*100*f))
    if dice_rolls[i] >= 5:
      paths.append((1,3*i*100*f))
    if dice_rolls[i] == 6:
      rec_turn = play_turn()
      paths.append((0,4*i*100*f + rec_turn if rec_turn != 0 else 0))

  random_path = random.sample(paths,1)[0] if paths else [0,0]

  return random_path[0], random_path[1]

def play_turn():
  score = 0
  n_dice = 6
  while n_dice > 0:
    dice_rolls = roll_dice(n_dice)
    n_dice, score_d = evaluate(dice_rolls, score)
    score += score_d
    if score_d == 0: return 0

  # return score if score >= 400 else 0
  return score

for _ in range(100):
  print(play_turn())