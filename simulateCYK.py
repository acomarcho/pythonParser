'''
Mensimulasikan algoritma table-filling algorithm CYK.
(1) Melakukan pengisian cell [0, X] dengan X [0..length(tokens)]
(2) Pengisian mengikuti pola seperti ini:
[1,0] adalah [0,0] x [0,1]; [1,1] adalah [0,1] x [0,2]; [1,2] adalah [0,2] x [0,3]; [1,3] adalah [0,3] x [0,4].
[2,0] adalah [1,0] x [0,2] U [0,0] x [1,1]; [2,1] adalah [1,1] x [0,3] U [0,1] x [1,2]; dst.
[3,0] adalah [2,0] x [0,3] U [1,0] x [1,2] U [0,0] x [2,1]; [3,1] adalah [2,1] x [0,4] U [1,1] x [1,3] U [0,1] x [2,2]; dst.
'''

def simulateCYK(X):
  # Pengisian baris ke-0.
  print(">>>> Pengisian baris ke-0.")
  for i in range(X):
    print(f'\tDiisi sel [0,{i}]')
  # Pengisian baris ke-1 s.d. ke-(X - 1)
  for i in range(1, X):
    # Baris ke-i memiliki kolom sebanyak X - i
    print(f'>>>> Pengisian baris ke-{i}')
    for j in range(X - i):
      print(f'\t>> Pengisian kolom ke-{j}')
      # Untuk setiap kolom, ada i kali pengisian.
      for k in range(i):
        # Dilakukan pengisian [i - 1 - k, j] X [k, j + i - k]
        print(f'\t\t[{i - 1 - k},{j}] X [{k},{j + i - k}]')

simulateCYK(5)