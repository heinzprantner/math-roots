"""

root application

"""

import math_root_t_root

def main():
   """
   application of the root function
   """
   tau=1e-3
   n = 2
   root = math_root_t_root.class_t_root(n=n,tau=tau)
   x = 81
   y = root.y(81)
   print('root n={} x={}: y={}'.format(n,x,y))

if __name__ == "__main__":
  main()
