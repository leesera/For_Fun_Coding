s = "asdfasdfdddd"
def compressString(string):
  compressed_string = ""
  target = string[0]
  num = 1
  for s in list(string)[1:]:
    if( s == target):
      num += 1
    else:
      #diff
      compressed_string += target+str(num)
      target = s
      num = 1
  compressed_string += target+str(num)
  return compressed_string

print(compressString(s))


