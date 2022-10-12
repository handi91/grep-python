import os
import sys
import re

def get_valid_arguments():
  args = sys.argv[1:]  # ambil argumen setelah nama file program

  # argumen yang valid diberikan minimal 2, maksimal 3
  if len(args) > 3 or len(args) < 2:
    return
  
  # jika argumen ada 3 maka ia valid iff nilainya -i atau -w
  if len(args) == 3:
    if len(args[0]) == 2:
      if re.search('^-', args[0]):
        if args[0][1] == 'w' or args[0][1] == 'i':
          return args
    return
  
  # jumlah argumen 2
  return args

def main():
  valid_args = get_valid_arguments()

  if valid_args is None: 
    print("Argumen program tidak benar.")
    return
  
  print(valid_args)
  print("benar")

if __name__ == '__main__':
  main()
