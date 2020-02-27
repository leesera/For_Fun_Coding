s1 = "asdf"
s2 = "asdf"
def areSameChrs(s1,s2):
  return sorted(list(s1)) == sorted(list(s2))

print(areSameChrs(s1,s2))
