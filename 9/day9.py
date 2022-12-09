import sys
def readfile():
  with open(str(sys.argv[1])+'.txt') as f:
    lines = f.read().splitlines()
  return lines

def move_head(direction):
  if direction == 'U':
    return 1j
  elif direction == 'D':
    return -1j
  elif direction == 'R':
    return 1
  elif direction == 'L':
    return -1

def move_body(distance, body_part,prev_body_part):
  if distance == 2.0:
    if prev_body_part.real > body_part.real:
      return 1
    elif prev_body_part.real < body_part.real:
      return -1
    elif prev_body_part.imag > body_part.imag:
      return 1j
    elif prev_body_part.imag < body_part.imag:
      return -1j
  elif distance > 2.0:
    if prev_body_part.real > body_part.real and prev_body_part.imag > body_part.imag:
      return 1+1j
    elif prev_body_part.real > body_part.real and prev_body_part.imag < body_part.imag:
      return 1-1j
    elif prev_body_part.real < body_part.real and prev_body_part.imag > body_part.imag:
      return -1+1j
    elif prev_body_part.real < body_part.real and prev_body_part.imag < body_part.imag:
      return -1-1j
  else:
    return 0+0j

def main(snake_length):
  lines=readfile()
  tail_visited = set()
  snake = [0+0j]*snake_length
  for line in lines:
    direction = line.split(' ')[0]
    step_size = int(line.split(' ')[1])
    for step in range(step_size):
      tail_visited.add(snake[-1])
      snake[0] += move_head(direction)
      for body_part in range(len(snake)-1):
        dist_between = abs(snake[body_part]-snake[body_part+1])
        snake[body_part+1] += move_body(dist_between,snake[body_part+1],snake[body_part])

    tail_visited.add(snake[-1])

  print(len(tail_visited))

## Part 1
main(2)
## Part 2
main(10)