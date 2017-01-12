def Binary_Search(arr, to_find):
  """A direct implementation of Newton's Method
     (For sanity assume that func and func_prime define there own division correctly,
     that is, don't cast anything to a float)
     params: arr (a list ordered from least to greatest)
             to_find (the item to find in arr)
     returns: index (int), x, s.t. arr[x] == to_find
              None(none-type) if for all x, arr[x] != to_find
  """
  L, R = 0, len(arr)-1
  while L <= R:
    m = (L+R)/2
    if arr[m] < to_find:
      L = m+1
    elif arr[m] > to_find:
      R = m-1
    else:
      return m

def Bisection(func, left_side, right_side, tol=1e-5):
  """A direct implementation of Newton's Method
     (For sanity assume that func and func_prime define there own division correctly,
     that is, don't cast anything to a float)
     params: func (a function)
             left_side (a value for the function to take on, it should have opposite sign from `right_side`)
             right_side (a value for the function to take on, it should have opposite sign from `left_side`)
             tol (a value for which the function should return once a value at least that distance from zero is found)
     returns: root (float), x, s.t. abs(func(x))<tol
              None(none-type) if func(left_side), func(right_side) < 0 or func(left_side), func(right_side) > 0
  """
  def sign(num):
    if num < 0:
      return False
    else:
      return True

  N = 1
  while N < 100000:
    c = (left_side+right_side)/2.
    print c
    if func(c) == 0 or abs((left_side-right_side)/2.) <= tol:
      return c
    N += 1
    if sign(func(c)) == sign(func(left_side)):
      left_side = c
    else:
      right_side = c
  return "Reached maximum number of iterations"