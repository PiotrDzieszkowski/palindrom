def palindrome(lista):
    wynik = list()
    for text in lista:
        if text[::-1] == text:
            wynik.append(True)
        else:
            wynik.append(False)
    return wynik
 
print(palindrome(["mama", "kajak", "książka","potop", "lalka"]))

def palindrome(lista):
  return lista == lista[::-1]
  

print(palindrome("kajak"))