from tabulate import tabulate
from FA import FA

def generateGrammar(filename):
  '''
  Membuat dictionary grammar dari suatu file.
  '''
  with open(filename) as f:
    R = {}
    lines = f.readlines()
    R["__START_VAR__"] = (lines[0].split('->'))[0].strip()
    i = 1
    for line in lines:
      '''
      Algoritma:
      Ubah bentuk A -> B | C | D menjadi var -> tmp
      Lalu, ubah tmp dari bentuk a | b c | d ke dalam result = ['a', 'b c', 'd']
      Masing-masing result akan dipetakan ke array yang berisikan variabelnya.
      '''
      # Bentuk var dan result
      var, tmp = line.split('->')
      var = var.strip()
      tmp = tmp.split('|')
      results = []
      for t in tmp:
        t = t.strip()
        results.append(t)
      # Petakan masing-masing result ke dalam R
      for r in results:
        if r in R:
          R[r].append(var)
        else:
          R[r] = [var]
  return R

def cyk(grammar, tokens):
  '''
  Menentukan apakah barisan token 'tokens' memenuhi grammar atau tidak.
  tokens adalah sebuah array of string.
  grammar adalah sebuah dictionary.
  '''
  # Inisialisasi tabel untuk table-filling algorithm.
  n = len(tokens)
  cyk_table = [[set() for i in range(n)] for j in range(n)]
  # Mengisi baris pertama cyk_table.
  for i in range(n):
    if tokens[i] in grammar:
      for var in grammar[tokens[i]]:
        cyk_table[0][i].add(var)
    else:
      if FA(tokens[i]):
        for var in grammar['_IDENTIFIER']:
          cyk_table[0][i].add(var)
      elif tokens[i].isnumeric():
        for var in grammar['_INTEGER']:
          cyk_table[0][i].add(var)
      for var in grammar["_ANY"]:
        cyk_table[0][i].add(var)
  # Mengisi baris lain pada cyk_table.
  for i in range(1, n):
    for j in range(n - i):
      finalSet = set()
      for k in range(i):
        tempSet = set()
        # Menghitung hasil tabel [i - 1 - k, j] X [k, j + i - k]
        for l in cyk_table[i - 1 - k][j]:
          for r in cyk_table[k][j + i - k]:
            res = l + ' ' + r
            # Apakah res ada grammarnya?
            if res in grammar:
              # Masukkan komponen res ke tempSet!
              for r in grammar[res]:
                tempSet.add(r)
        finalSet = finalSet.union(tempSet)
      cyk_table[i][j] = finalSet
  # Syarat CYK adalah cyk_table[n - 1, 0] mengandung __START_VAR__
  if grammar["__START_VAR__"] in cyk_table[n - 1][0]:
    print('Accepted')
  else:
    print('Syntax Error')
  # print("=======> Tabel algoritma CYK <=======")
  # print(tabulate(cyk_table))

def convertLine(l):
  # Mengonversi sebuah line yang dibaca, 'l' menjadi list of tokens.
  l = l.replace("\n", " _NEWLINE ")
  l = l.replace('"""', ' _TRIPDQUOTE ')
  l = l.replace("'''", " _TRIPSQUOTE ")
  l = l.replace("==", " _EQ ")
  l = l.replace("!=", " _NEQ ")
  l = l.replace(">=", " _GE ")
  l = l.replace("<=", " _LE ")
  l = l.replace("+=", " _CPLUS ")
  l = l.replace("-=", " _CMIN ")
  l = l.replace("//=", " _CDIVI ")
  l = l.replace("/=", " _CDIVF ")
  l = l.replace("**=", " _CPOW ")
  l = l.replace("*=", " _CMUL ")
  l = l.replace("%=", " _CMOD ")
  l = l.replace("//", " _DIV ")
  l = l.replace("**", " _POW " )
  l = l.replace("#", "# ")
  l = l.replace("=", " = ")
  l = l.replace('(', ' ( ')
  l = l.replace(')', ' ) ')
  l = l.replace(':', ' : ')
  l = l.replace(';', ' ; ')
  l = l.replace("'", " ' ")
  l = l.replace(",", " , ")
  l = l.replace("[", " [ ")
  l = l.replace("]", " ] ")
  l = l.replace("{", " { ")
  l = l.replace("}", " } ")
  l = l.replace(".", " . ")
  l = l.replace('"', ' " ')
  l = l.replace('%', ' % ')
  l = l.replace('+', ' + ')
  l = l.replace('-', ' - ')
  l = l.replace('/', ' / ')
  l = l.replace('*', ' * ')
  tokens = l.split(' ')
  i = 0
  while (i < len(tokens)):
    tokens[i] = tokens[i].strip()
    if len(tokens[i]) == 0:
      del tokens[i]
    else:
      i += 1
  return tokens
