def FindIntersection(strArr):

  # code goes here
  a = set(strArr[0].split(', '))
  b = set(strArr[1].split(', '))
  
  result = sorted(list(a.intersection(b)), key=lambda str: int(str))

  return ",".join(result) if len(result) > 0 else False

# keep this function call here 
print(FindIntersection(input()))