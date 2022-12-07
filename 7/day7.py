import sys
def readfile():
  with open(str(sys.argv[1])+'.txt') as f:
    lines = f.read().splitlines()
  return lines

def get_directory_structure(lines):
  dir_structure = set()
  tree = []
  current_dir = ''
  for x in range(len(lines)):
    if '$' in lines[x]:
      if ' cd ' in lines[x]:
        if '..' not in lines[x]:
          if current_dir != '':
            current_dir += lines[x].split('cd ')[1]+'/'
            dir_structure.add(current_dir)
          else:
            current_dir = '/'
            dir_structure.add(current_dir)
        else:
          current_dir = current_dir.rsplit('/',2)[0]+'/'
      elif ' ls' in lines[x]:
        y = x+1
        while '$' not in lines[y]:
          if 'dir ' not in lines[y]:
            current_file = current_dir + lines[y].split(' ')[1]
            size = int(lines[y].split(' ')[0])
            tree.append([current_file,size])
          y+=1
          if y == len(lines):
            break
  return tree,dir_structure

def get_dir_size(tree,dir_structure,dir_sizes):
  for directory in dir_structure:
    for element in tree:
      if element[0].find(directory,0,len(directory)) != -1:
        dir_sizes[directory] += element[1]

def main():
  tree,dir_structure = get_directory_structure(readfile())
  dir_sizes = {}
  for directory in dir_structure:
    dir_sizes[directory] = 0
  get_dir_size(tree,dir_structure,dir_sizes)

  sum_under_100k = 0
  for element in dir_sizes.values():
    if element <= 100000:
      sum_under_100k += element
  print(sum_under_100k)

  ## Part 2
  total_filesystem_size = 70000000
  required_space = 30000000
  disk_usage = dir_sizes['/']
  free_space = total_filesystem_size-disk_usage
  min_size_to_delete = required_space - free_space
  current_size_to_delete = 100000000000000000
  for element in dir_sizes.values():
    if element >= min_size_to_delete and element < current_size_to_delete:
      current_size_to_delete = element
  print(current_size_to_delete)

main()


