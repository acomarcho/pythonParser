import os
import argparse
from parser import *

def logo():
    print("                                          __                     __     ")
    print("                              _    _____ / /______  __ _  ___   / /____ ")
    print("                             | |/|/ / -_) / __/ _ \/  ' \/ -_) / __/ _ \ ")
    print("                             |__,__/\__/_/\__/\___/_/_/_/\__/  \__/\___/ \n\n")
    print("██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗    ██████╗  █████╗ ██████╗ ███████╗███████╗██████╗ ")
    print("██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║    ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗")
    print("██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║    ██████╔╝███████║██████╔╝███████╗█████╗  ██████╔╝")
    print("██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║    ██╔═══╝ ██╔══██║██╔══██╗╚════██║██╔══╝  ██╔══██╗")
    print("██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║    ██║     ██║  ██║██║  ██║███████║███████╗██║  ██║")
    print("╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝    ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝\n")
    print("=========================================================================================================")
    print("                            Ketik X apabila anda ingin keluar dari program!")
    print("=========================================================================================================")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", nargs="?", help="parse a python file", type=str)
    args = parser.parse_args()
    logo()
    if not args.filename:
      # Membuka file input
      filename = input('Enter the file name : ')
      while filename != 'X':
          if os.path.isfile(filename):
              print(f'Processing {filename}!')
              text_file = open(filename, "r")
              text_file_string = text_file.read()
              text_file.close()
              print("VERDICT: ", end="")
              cyk(generateGrammar('generatedCNF.txt'), convertLine(text_file_string))
          else:
              print('File tidak ditemukan, Silahkan tulis ulang nama file!')
          filename = input('\nEnter the file name : ')
    else:
      if os.path.isfile(args.filename):
          print(f'Processing {args.filename}!')
          text_file = open(args.filename, "r")
          text_file_string = text_file.read()
          text_file.close()
          print("VERDICT: ", end="")
          cyk(generateGrammar('generatedCNF.txt'), convertLine(text_file_string))
      else:
          print('File tidak ditemukan, Silahkan tulis ulang nama file!')

