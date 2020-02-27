string = "hihihiadlkfjwioer"

def check_uniq_chrs(string):
  checker = 0
  for s in list(string):
    _ascii = ord(s)-ord('a')
    if(checker & (1<<_ascii)):
      return False
    checker = checker | (1<<_ascii)
  return True

print(check_uniq_chrs("asdf"))




