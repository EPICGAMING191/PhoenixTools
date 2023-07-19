class math:
  import math 
  def sqr(number):
    number=number*number
    return number
    
  def power(number,power):
    times=power-1
    for x in range(times):
      number=number*number
    return number

  def sqrroot(number):
    root=math.sqrroot(number)
    return root