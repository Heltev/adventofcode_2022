import sys
def readfile():
  with open(str(sys.argv[1])+'.txt') as f:
    lines = f.read()
  return lines

signal = readfile()
unique_list = []
for x in range(len(signal)):
  unique_set = set()
  unique_list.append(signal[x])
  if x > 13:
    unique_list.pop(0)
  for element in unique_list:
    unique_set.add(element)
  if len(unique_set) > 13:
    break
  
print(x+1)
