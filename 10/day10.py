import sys
def readfile():
  with open(str(sys.argv[1])+'.txt') as f:
    lines = f.read().splitlines()
  return lines

def main():
  lines = readfile()
  clock_cycle = 0
  x_value = 1
  signal_strength = {}
  iterator = 0
  screen = ['.']*240
  while iterator < len(lines):
    if x_value - 1 <= clock_cycle - (40*(clock_cycle // 40)) <= x_value+1:
      screen[clock_cycle] = '#'
    clock_cycle += 1
    instruction = lines[iterator].split(' ')[0]
    if instruction == 'addx':
      step = int(lines[iterator].split(' ')[1])
    if clock_cycle == 20 or (clock_cycle + 20) % 40 == 0:
      signal_strength[clock_cycle] = x_value*clock_cycle
    if x_value - 1 <= clock_cycle - (40*(clock_cycle // 40)) <= x_value+1:
      screen[clock_cycle] = '#'
    if instruction == 'addx':
      clock_cycle += 1
    if clock_cycle == 20 or (clock_cycle + 20) % 40  == 0:
      signal_strength[clock_cycle] = x_value*clock_cycle
    if instruction == 'addx':
      x_value += step
    iterator += 1
  
  ## Part 1 
  signal_strength_sum = 0
  for signal in signal_strength.values():
    signal_strength_sum += signal
  print(signal_strength_sum)

  ## Part 2
  result = []
  for i in range(0,len(screen), 40):
    row = screen[i:i+40]
    result.append(row)
  for line in result:
    print(line)

main()