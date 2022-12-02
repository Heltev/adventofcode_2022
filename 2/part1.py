import sys
def readfile():
  with open(str(sys.argv[1])+'.txt') as f:
    lines = f.read().splitlines()
  print(lines)
  return lines

def calculate_score(actions):
  if actions[0] == 'A':
    if actions[2] == 'X':
      return 4
    elif actions[2] == 'Y':
      return 8
    elif actions[2] == 'Z':
      return 3
  elif actions[0] == 'B':
    if actions[2] == 'X':
      return 1
    elif actions[2] == 'Y':
      return 5
    elif actions[2] == 'Z':
      return 9
  elif actions[0] == 'C':
    if actions[2] == 'X':
      return 7
    elif actions[2] == 'Y':
      return 2
    elif actions[2] == 'Z':
      return 6

def main():
  instructions = readfile()
  score = 0
  for line in instructions:
    score += calculate_score(line)
  print(score)

main()