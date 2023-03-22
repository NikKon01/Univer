str1 = 'katas'
str2 = 'steak'

def scramble(str1, str2):
  str1_list = list(str1)
  for i in str2:
    if i in str1_list:
      str1_list.pop(str1_list.index(i))
    else:
      return False
  return True

print(scramble('rkqodlw', 'world'))
print(scramble('cedewaraaossoqqyt', 'codewars'))
print(scramble('katas', 'steak'))

d.items