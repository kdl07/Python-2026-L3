# Ex8
listnum = [1,4,5,-1,10]
def extract_even(l):
  return [x for x in l if x % 2 == 0]

if extract_even(listnum):
  print(f" {extract_even(listnum)}")