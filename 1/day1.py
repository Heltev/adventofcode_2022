import sys

def main():
  tot_cals = 0
  max_cals = 0
  all_cals = []
  for line in open(str(sys.argv[1])+'.txt'):
    if line == '\n':
        if tot_cals > max_cals:
            max_cals = tot_cals
        all_cals.append(tot_cals)
        tot_cals = 0
    else:
      tot_cals += int(line)
  if tot_cals > max_cals:
    max_cals = tot_cals
  all_cals.append(tot_cals)
  all_cals.sort()
  print (max_cals)
  print(all_cals[-1]+all_cals[-2]+all_cals[-3])

main()