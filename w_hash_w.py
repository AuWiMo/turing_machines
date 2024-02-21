startstring = "aba#"
index = 0

stringList = [*startstring]

def printState():
  print("$", end ="");
  for i in range(len(stringList)):
    if (index == i):
      print('q_0', end ="")
    if stringList[i] != '#':
      print(stringList[i], end ="")
    else :
      print("\#", end ="")
  if (index == len(stringList)):
    print('q_0', end ="")
  print("$\\\\");


while (True): 
  printState()

  if stringList[index] == 'a':
    stringList[index] = r'\dot{a}'
    index += 1
    printState()

    while (index < len(stringList)):
      index += 1 
      printState()

    stringList.append('a')
    index -= 1 
    printState()

  elif stringList[index] == 'b':
    stringList[index] = r'\dot{b}'
    index += 1
    printState()

    while (index < len(stringList)):
      index += 1 
      printState()

    stringList.append('b')
    index -= 1 
    printState()

  elif stringList[index] == '#':
    break; 

  while ((stringList[index] != r"\dot{a}") and (stringList[index] != r"\dot{b}")):
    index-=1;
    printState()
  
  if (stringList[index] == r"\dot{a}"):
    stringList[index] = "a"
    index+=1
  elif (stringList[index] == r"\dot{b}"):
    stringList[index] = "b"
    index+=1

    
  
 


