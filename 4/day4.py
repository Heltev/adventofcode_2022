import sys

def readfile():
  with open(str(sys.argv[1])+'.txt') as f:
    lines = f.read().splitlines()
  lines_splitted = []
  for element in lines:
    lines_splitted.append(element.split(','))
  return lines_splitted

def check_overlap(pair):
  lower_limit_first, upper_limit_first = pair[0].split('-')
  lower_limit_second, upper_limit_second = pair[1].split('-')
  if int(lower_limit_first) <= int(lower_limit_second) and int(upper_limit_first) >= int(upper_limit_second):
    return 1
  elif int(lower_limit_second) <= int(lower_limit_first) and int(upper_limit_second) >= int(upper_limit_first):
    return 1
  else:
    return 0

def check_partial_overlap(pair):
  lower_limit_first, upper_limit_first = pair[0].split('-')
  lower_limit_second, upper_limit_second = pair[1].split('-')
  if int(upper_limit_first) >= int(lower_limit_second) and (int(lower_limit_first) <= int(upper_limit_second)):
    return 1
  else:
    return 0

def main():
  instructions = readfile()
  total_overlaps = 0
  total_partial_overlaps = 0
  for pair in instructions:
    total_overlaps += check_overlap(pair)
    total_partial_overlaps += check_partial_overlap(pair)
  print(total_overlaps)
  print(total_partial_overlaps)

main()