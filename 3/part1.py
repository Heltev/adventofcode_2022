import sys
def readfile():
  with open(str(sys.argv[1])+'.txt') as f:
    lines = f.read().splitlines()
  return lines

def calculate_priority(item):
  ## Regner ut ascii verdi og trekker fra for å matche
  ## dagens oppgave
  if item.isupper():
    return ord(item)-38
  elif item.islower():
    return ord(item)-96
  else:
    print("Error!!!!")

def main():
  sacks = readfile()
  priority_sum = 0
  for sack in sacks:
    first_compartment = {}
    second_compartment = []
    for x in range(len(sack)):
      if x >= len(sack)/2:
        if first_compartment.get(sack[x]) == 0:
          priority_sum += calculate_priority(sack[x])
          first_compartment[sack[x]] = 1
        second_compartment.append(sack[x])
      else:
        first_compartment[sack[x]] = 0
    
  print(priority_sum)

main()
