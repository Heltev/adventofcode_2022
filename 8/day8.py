import sys
def readfile():
  with open(str(sys.argv[1])+'.txt') as f:
    lines = f.read().split()
  return lines

def check_up(pos,value):
  for row in range(pos[0]-1,-1,-1):
    if value <= get_tree_height(row,pos[1]):
      return 0
  return 1

def check_down(pos,value):
  for row in range(pos[0]+1,SIZE):
    if value <= get_tree_height(row,pos[1]):
      return 0
  return 1

def check_right(pos,value):
  for col in range(pos[1]+1,SIZE):
    if value <= get_tree_height(pos[0],col):
      return 0
  return 1

def check_left(pos,value):
  for col in range(pos[1]-1,-1,-1):
    if value <= get_tree_height(pos[0],col):
      return 0
  return 1

def check_viewing_dist_up(pos,value):
  counter = 0
  for row in range(pos[0]-1,-1,-1):
    counter += 1
    if value <= get_tree_height(row,pos[1]):
      return counter
  return counter

def check_viewing_dist_down(pos,value):
  counter = 0
  for row in range(pos[0]+1,SIZE):
    counter += 1
    if value <= get_tree_height(row,pos[1]):
      return counter
  return counter

def check_viewing_dist_right(pos,value):
  counter = 0
  for col in range(pos[1]+1,SIZE):
    counter += 1
    if value <= get_tree_height(pos[0],col):
      return counter
  return counter

def check_viewing_dist_left(pos,value):
  counter = 0
  for col in range(pos[1]-1,-1,-1):
    counter += 1
    if value <= get_tree_height(pos[0],col):
      return counter
  return counter

def get_tree_height(row,col):
  return tree_matrix[row][col]

lines = readfile()
SIZE = len(lines)
tree_matrix = [[int(x) for x in line] for line in lines]

## Part 1
visible_trees = 0
for row in range(len(tree_matrix)):
  for col in range(len(tree_matrix)):
    visible = 0
    visible += check_up((row,col),tree_matrix[row][col])
    visible += check_down((row,col),tree_matrix[row][col])
    visible += check_right((row,col),tree_matrix[row][col])
    visible += check_left((row,col),tree_matrix[row][col])
    if visible > 0:
      visible_trees += 1
print(visible_trees)

## Part 2
top_scenic_score = 0
for row in range(1,len(tree_matrix)-1):
  for col in range(1,len(tree_matrix)-1):
    view_dist = []
    view_dist.append(check_viewing_dist_up((row,col),tree_matrix[row][col]))
    view_dist.append(check_viewing_dist_down((row,col),tree_matrix[row][col]))
    view_dist.append(check_viewing_dist_right((row,col),tree_matrix[row][col]))
    view_dist.append(check_viewing_dist_left((row,col),tree_matrix[row][col]))
    scenic_score = view_dist[0]*view_dist[1]*view_dist[2]*view_dist[3]
    if scenic_score > top_scenic_score:
      top_scenic_score = scenic_score
print(top_scenic_score)