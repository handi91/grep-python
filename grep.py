from genericpath import isdir
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

def print_line(path, line, sentence):
  print("{:40s} line {:<3d} {:40s}".format(path, line, sentence))

def scan_file(file, pattern, direktori):
  line_idx = 0
  for line in file:
    line_idx += 1
    if re.search(pattern, line.strip()):
      print_line(direktori, line_idx, line.strip())

def handle_with_option(option, direktori, pattern, is_file):
  pass

def handle_without_option(direktori, pattern, is_file):
  if is_file:
    file = open(direktori, "r")
    scan_file(file, pattern, direktori)
    file.close()
    return
  
  if direktori[-1:] != "\\":
    direktori = direktori + "\\"
  
  for dir in os.listdir(direktori):
    new_dir = direktori+dir
    if os.path.isfile(new_dir):
      handle_without_option(new_dir, pattern, True)
    elif os.path.isdir(new_dir):
      handle_without_option(new_dir, pattern, False)

def main():
  valid_args = get_valid_arguments()

  if valid_args is None: 
    print("Argumen program tidak benar.")
    return

  is_file = False
  option = ""

  direktori = valid_args[1] if len(valid_args) == 2 else valid_args[2]
  if os.path.exists(direktori):
    if os.path.isfile(direktori):
      is_file = True
  else:
    print(f"Path {direktori} tidak ditemukan.")
    return

  if len(valid_args) == 3:
    option = valid_args[0]
    handle_with_option(option, direktori, valid_args[1], is_file)
  else:
    handle_without_option(direktori, valid_args[0], is_file)


if __name__ == '__main__':
  main()
