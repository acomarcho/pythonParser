def FA(s):
  '''
  Mengemulasikan suatu FA untuk mengetahui apakah nama variabel benar/salah.
  Mengembalikan True jika nama variabel valid, False jika tidak.
  '''
  # By default, set bahwa string ini diterima.
  accepted = True
  # Apabila string kosong, tentu saja accepted.
  if (len(s) == 0):
    accepted = False
  else:
    # Pembacaan huruf pertama: HARUS letter atau _ 
    if not ((ord(s[0]) >= ord('A') and ord(s[0]) <= ord('Z')) or (ord(s[0]) >= ord('a') and ord(s[0]) <= ord('z')) or (s[0] == '_')):
      accepted = False
    else:
      # Cek huruf di index ke-1 sampai index terakhir: HARUS alfanumerik atau _
      i = 1
      while (i < len(s) and accepted):
        if not ((ord(s[i]) >= ord('A') and ord(s[i]) <= ord('Z')) or (ord(s[i]) >= ord('a') and ord(s[i]) <= ord('z')) or (s[i] == '_') or (ord(s[i]) >= ord('0') and ord(s[i]) <= ord('9'))):
          accepted = False
        else:
          i += 1
  return accepted

# For debugging purposes only.
# while True:
#   check = input("Masukkan nama variabel: ")
#   print(FA(check))