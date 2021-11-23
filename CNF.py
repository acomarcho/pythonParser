terminals = [
  "def",
  "identifier",
  "(",
  ")",
  ":",
  ",",
]

# terminals = [
#   "a",
#   "b"
# ]

def generateCFG(filename):
  R = {}
  with open(filename) as f:
    lines = f.readlines()
    R["__START_VAR__"] = (lines[0].split('->'))[0].strip()
    for line in lines:
      var, tmp = line.split('->')
      var = var.strip()
      tmp = tmp.split('|')
      res = []
      for t in tmp:
        t = t.strip()
        tempList = []
        for k in t.split():
          tempList.append(k.strip())
        res.append(tempList)
      if var in R:
        R[var].extend(res)
      else:
        R[var] = res
  return R

def removeUnitProduction(R):
  for key in R:
    if key == '__START_VAR__':
      continue
    i = 0
    while i < len(R[key]):
      if len(R[key][i]) == 1 and R[key][i][0] not in terminals:
        removedProduction = R[key].pop(i)
        if key != removedProduction[0]:
          for l in R[removedProduction[0]]:
            if l != removedProduction and l not in R[key]:  # l not in R[key] untuk menghindari duplikat
              R[key].append(l)
      else:
        i += 1

def getAvailableVariableName(name, R):
  while name in R or name in terminals:
    name += '*'
  return name

def simplifyRule(R):
  # Bagian 1: Mengonversi ['A', TAIL] menjadi ['A', 'A*'] di mana A* adalah production [HEAD_DARI_TAIL, TAIL_DARI_TAIL], terus sampai selesai.
  for key in list(R):
    if key == '__START_VAR__':
      continue
    i = 0
    while (i < len(R[key])):
      if len(R[key][i]) > 2:
        length = len(R[key][i])
        # Ide: Apabila length = 3, contoh A A B diganti jadi A A*, A* -> A B
        # apabila length = 4, contoh A A B A diganti jadi A A*, A* -> A A**, A** -> B A
        # berarti melakukan iterasi sebanyak length - 2 kali
        lastTail = (R[key][i])[1:]
        lastKey = getAvailableVariableName(R[key][i][0], R)
        R[key][i] = [R[key][i][0], lastKey]
        while(len(lastTail) > 2):
          tmpKey = getAvailableVariableName(lastKey, R)
          if lastKey not in R:
            R[lastKey] = [[lastTail[0], tmpKey]]
          else:
            R[lastKey].append([lastTail[0], tmpKey])
          lastTail = lastTail[1:]
          lastKey = tmpKey
        if lastKey not in R:
          R[lastKey] = [lastTail]
        else:
          R[lastKey].append(lastTail)
      i += 1
  # Bagian 2: Mengonversi ['a', 'B'] menjadi ['a*' 'B'] dan menambah rule a* -> a di mana a* adalah variabel, bukan terminal.
  for key in list(R):
    if key == '__START_VAR__':
      continue
    i = 0
    while i < len(R[key]):
      if len(R[key][i]) == 2 and R[key][i][0] in terminals:
        terminal = R[key][i][0]
        # Ubah terminal menjadi bentuk variabelnya
        R[key][i][0] = getAvailableVariableName(R[key][i][0], R)
        # Apabila rulenya belum ada, buat rulenya
        if R[key][i][0] not in R:
          R[R[key][i][0]] = [[terminal]]
      if len(R[key][i]) == 2 and R[key][i][1] in terminals:
        terminal = R[key][i][1]
        # Ubah terminal menjadi bentuk variabelnya
        R[key][i][1] = getAvailableVariableName(R[key][i][1], R)
        # Apabila rulenya belum ada, buat rulenya
        if R[key][i][1] not in R:
          R[R[key][i][1]] = [[terminal]]
      i += 1
  
def writeRule(filename, R):
  with open(filename, 'w') as f:
    for key in R:
      if key == '__START_VAR__':
        continue
      f.write(f'{key} -> ')
      for i, prods in enumerate(R[key]):
        if i != len(R[key]) - 1:
          f.write(f'{" ".join(prods)} | ')
        else:
          f.write(f'{" ".join(prods)}\n')


R = generateCFG('toCNFplz.txt')
print(R)
removeUnitProduction(R)
print(R)
simplifyRule(R)
print(R)
writeRule('generatedCNF.txt', R)