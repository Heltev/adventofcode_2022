import sys

def readfile():
  with open(str(sys.argv[1])+'.txt') as f:
    lines = f.read().splitlines()
  stacks = {}
  instructions = []
  move_instructions = 0
  for line in lines:
    if move_instructions:
      instructions.append(line)
    else:
      stack_counter = 0
      for element in line:
        if (stack_counter == 1 or (stack_counter-1) % 4 == 0) and element.isalpha():
          if (stack_counter+3)/4 in stacks.keys():
            stacks[(stack_counter+3)//4].insert(0,element)
          else:
            stacks[(stack_counter+3)//4] = [element]
        stack_counter += 1
    if line == '':
      move_instructions = 1
  return stacks, instructions

def cratemover_9000(stacks,instructions):
  for line in instructions:
    n_crates,from_stack,to_stack = int(line.split(' ')[1]),int(line.split(' ')[3]),int(line.split(' ')[5])
    for x in range(n_crates):
      stacks[to_stack].append(stacks[from_stack].pop())
  return stacks

def cratemover_9001(stacks,instructions):
  for line in instructions:
    n_crates,from_stack,to_stack = int(line.split(' ')[1]),int(line.split(' ')[3]),int(line.split(' ')[5])
    for x in range(len(stacks[from_stack])-n_crates,len(stacks[from_stack])):
      stacks[to_stack].append(stacks[from_stack][x])
    del stacks[from_stack][len(stacks[from_stack])-n_crates:]
  return stacks


stacks_init,instructions = readfile()
stacks_9000 = cratemover_9000(stacks_init,instructions)

stacks_init,instructions = readfile()
stacks_9001 = cratemover_9001(stacks_init,instructions)


message_9000=''
message_9001=''
for x in range(len(stacks_init)):
  message_9000 += stacks_9000[x+1][-1]
  message_9001 += stacks_9001[x+1][-1]
print(message_9000)
print(message_9001)