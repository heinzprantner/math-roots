"""

domain  : math
package : root
version : 0.0.1
class   : t_root
yaml    : resources/classes/math/math_root_classes.yml
factory : class_factory.py

"""

_domain  = "math"
_package = "root"
_version = "0.0.1"

#import bigdata_core_classes
import math
#import math_root_t_root
import time

class class_t_root():
    """Class Definition for t_root

    yaml: resources/classes/math/math_root_classes.yml

    entries:
    """

    def __init__(self,n = 2,tau = 1e-3,s = math.e):
      """
      root functions implementation
      - n ..... dimension, (default: 2)
      - tau ... tolerance, precision, granularity (default: 0.001)
      - s ..... reference value s
      - r ..... reference value r = s^n
      - x ..... y^n = r^ck
      - y ..... n'th root y of input value x, y=s^ck
      - c ..... iteration count, for one x, for one r
      - ck .... calibrated c, D<tau
      - D ..... Delta, misfit of r^c to x
      """
      self._n  = n
      self._tau  = tau
      self._s  = s
      self._c = 0
      self._s = s
      self._r = self._s**self._n


    def _err(self,x,y,n):
      """
      error function, calculate misfit
      """
      return (x - y**n)

    def y(self,x):
       _start_time = time.time()
       result = self._wrapped_y(x)
       _end_time = time.time()
       self._execution_time_y = _end_time - _start_time
       return result

    def get_execution_time_y(self):
      return self._execution_time_y

    def _wrapped_y(self,x):
      """
      iterative, relational root approximation function
      return n'th root y for given x
      """
      self._c = self._calc_c(x,self._r)
      self._ck = self._calibration(self._c,x,self._r)
      _y = self._calc_y(self._s,self._ck)
      self._D = self._err(x,_y,self._n)
      return _y

    def _calc_c(self,x,r):
      """
      iteration for x for a given reference r
      repeated division of x with r
      output of one division becomes input for next division
      until x becomes equal r or smaller
      return c, the number of iterations
      """
      _x = x
      _c = 0
      while (_x >= r):
        _x = _x/r
        _c += 1
      return _c

    def _calc_y(self,s,ck):
      """
      y=s^ck
      """
      _y = s**ck
      _y = round(_y,self._get_decimals(self._tau))
      return _y

    def _calibration(self,c,x,r):
      """
      calibrate c for x and r
      return ck ... calibrated c
      x' = r^ck
      """
      _tau=self._tau/1000
      _decimals = self._get_decimals(_tau)
      _ck = c
      while (_decimals>0):
        _incr = _tau*(10**(_decimals-1))
        while (x>(r**_ck)):
          _ck += _incr
        _ck -= _incr
        _decimals -= 1
      _ck = round(_ck,self._get_decimals(_tau))
      return _ck

    def _get_decimals(self,tau):
      """
      get number of decimal places based on tau
      e.g. tau = 0.001 (1e-3): decimals = 3
      """
      return int(math.log10(1/tau))

