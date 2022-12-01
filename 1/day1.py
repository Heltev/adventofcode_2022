def main():
  tot_cals = 0
  max_cals = 0
  all_cals = []
  for line in open('input.txt'):
    if line == '\n':
        if tot_cals > max_cals:
            max_cals = tot_cals
        all_cals.append(tot_cals)
        all_cals.sort()
        tot_cals = 0
    else:
      tot_cals += int(line)
  print (max_cals)
  print(all_cals[-1]+all_cals[-2]+all_cals[-3])

main()