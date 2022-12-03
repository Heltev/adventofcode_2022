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
  # Legger til en tom streng for å håndtere siste sekk
  sacks.append("")
  priority_sum = 0
  item_dict = {}
  item_set = set()
  for x in range(len(sacks)):
    if not (x % 3) and x > 0:
      ## Henter key basert på value fra dictionary
      security_item = [k for k, v in item_dict.items() if v == 3]
      ## Regn ut prioritetsverdien,
      priority_sum += calculate_priority(security_item[0])
      ## Tøm dictionary og set før neste trio 
      item_dict = {}
      item_set = set()
    item_set = set()
    for item in sacks[x]:
      item_set.add(item)
    for item in item_set:
      if item_dict.get(item):
        item_dict[item] += 1
      else:
        item_dict[item] = 1
  print(priority_sum)
  
main()