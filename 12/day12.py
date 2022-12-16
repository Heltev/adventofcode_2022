import sys
def readfile():
  with open(str(sys.argv[1])+'.txt') as f:
    lines = f.read().split()
  grid = []
  for line in lines:
    row = []
    for i in range(len(line)):
      row.append(line[i])
    row.insert(0,'~')
    row.append('~')
    grid.append(row)
  grid.insert(0,['~']*len(grid[0]))
  grid.append(['~']*len(grid[0]))
  return grid

def char_2_int(grid):
  int_grid = []
  for row in range(len(grid)):
    int_row = []
    for col in range(len(grid[row])):
      if grid[row][col] == 'S':
        int_row.append(ord('a')-96)
      elif grid[row][col] == 'E':
        int_row.append(ord('z')-96)
      else:
        int_row.append(ord(grid[row][col])-96)
    int_grid.append(int_row)
  return int_grid

def get_start_pos(grid):
  for row in range(len(grid)):
    for col in range(len(grid[row])):
      if grid[row][col] == 'S':
        return (row,col)

def get_target_pos(grid):
  for row in range(len(grid)):
    for col in range(len(grid[row])):
      if grid[row][col] == 'E':
        return (row,col)

def get_possible_next_nodes(pos,grid):
  current_height = grid[pos[0]][pos[1]]
  possible_next = []
  if grid[pos[0]][pos[1]+1] - current_height <= 1:
    possible_next.append((pos[0],pos[1]+1))
  if grid[pos[0]+1][pos[1]] - current_height <= 1:
    possible_next.append((pos[0]+1,pos[1]))
  if grid[pos[0]-1][pos[1]] - current_height <= 1:
    possible_next.append((pos[0]-1,pos[1]))
  if grid[pos[0]][pos[1]-1] - current_height <= 1:
    possible_next.append((pos[0],pos[1]-1))
  return possible_next

def get_multiple_start(grid):
  start_positions = []
  for row in range(len(grid)):
    for col in range(len(grid[row])):
      if grid[row][col] == 'a':
        start_positions.append((row,col))
  return start_positions

def bfs(integer_grid, start_pos, target_pos):
  queue = []
  temp_queue = []
  explored = [start_pos]
  queue.append(start_pos)
  a=1
  parents = {}
  parents[start_pos] = [(0,0)]
  while len(queue) >= 1:
    for element in queue:
      current_node = queue.pop(0)
      for possible_next in get_possible_next_nodes(current_node,integer_grid):
        if possible_next in parents:
          parents[possible_next].append(current_node)
        parents[possible_next] = [current_node]
        parents[possible_next]+= parents[current_node]
        if possible_next == target_pos:
          return len(parents[target_pos])-1
        if possible_next not in explored:
          temp_queue.append(possible_next)
          explored.append(possible_next)
    queue = temp_queue
    a+=1
      
  return 1000000000000
    
def main():
  grid = readfile()
  for row in grid:
    print(row)
  start_pos = get_start_pos(grid)
  target_pos = get_target_pos(grid)
  integer_grid = char_2_int(grid)
  ## Part 1
  print(bfs(integer_grid,start_pos,target_pos))

  ## Part 2
  starts = get_multiple_start(grid)
  shortest = 100000000000000
  for element in starts:
    path = bfs(integer_grid,element,target_pos)
    if int(path) < shortest:
      shortest = path
  print(shortest)
  

main()


