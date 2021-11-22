# from tabulate import tabulate

def generateGrammar(filename):
  '''
  Membuat dictionary grammar dari suatu file.
  '''
  with open(filename) as f:
    R = {}
    lines = f.readlines()
    R["__START_VAR__"] = (lines[0].split('->'))[0].strip()
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
      print(f'Token {tokens[i]} tidak ditemukan pada grammar!')
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
    print('List of token diterima!')
  else:
    print('List of token tidak diterima!')
  # print("=======> Tabel algoritma CYK <=======")
  # print(tabulate(cyk_table))

cyk(generateGrammar('grammar.txt'), ['b', 'a', 'a', 'b', 'a'])
