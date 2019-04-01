from random import choice
from prueba import codones_RNA


userinput = raw_input("Pon la cadena en una linea \n")

def cadenainput(bases):
  cadena = ""
  for i in bases:
    if i != " " :
      cadena = cadena + i
  return cadena

def Transcripcion(linea):
  cadenaRNA = ""
  prov = cadenainput(linea)
  for i in prov:
    if i != 'T':
      cadenaRNA = cadenaRNA + i
    else:
      cadenaRNA = cadenaRNA + 'U'
  print cadenaRNA
  return cadenaRNA

def Traduccion(num):
  proteina = ""
  cadRNA = Transcripcion(num)
  for x in range(len(cadRNA)):
    codon = cadRNA[x] + cadRNA[x+1] + cadRNA[x+2]
    if codon == 'AUG':
      rango = range(x, (len(cadRNA) + 1))
      codonfin = x + 2
      print "posicion del codon de inicio: {} - {} bp".format(x,codonfin)
      break
  for i in rango[::3]:
    codon = cadRNA[i] + cadRNA[i+1] + cadRNA[i+2]
    if codones_RNA[codon] != 'STOP':
      proteina += codones_RNA[codon] + '-'
    elif i == len(cadRNA):
      proteina += codones_RNA[codon] + "xxxxxxxxxxxx--->"
    elif i > len(cadRNA):
      proteina += "xxxxxxxxxxxx--->"
      break
    else:
      proteina = proteina[:len(proteina)-1:]
      fincodon = i + 2
      print "posicion del codon de terminacion: {} - {} bp".format(i,fincodon)
      return proteina


print Traduccion(userinput)
