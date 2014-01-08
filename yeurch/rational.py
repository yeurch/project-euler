'''rational.py:  Module to do rational arithmetic.

  For full documentation, see http://www.nmt.edu/tcc/help/lang/python/examples/rational/.
  Exports:
    gcd ( a, b ):
      [ a and b are integers ->
          return the greatest common divisor of a and b ]
    Rational ( a, b ):
      [ (a is a nonnegative integer) and
        (b is a positive integer) ->
          return a new Rational instance with 
          numerator a and denominator b ]
    .n:    [ the numerator ]
    .d:    [ the denominator ] 
	.__eq__(self, other):
	  [ other is a Rational instance ->
	      return whether the two fractions are of equal value ]
    .__add__(self, other):
      [ other is a Rational instance ->
          return the sum of self and other as a Rational instance ]
    .__sub__(self, other):
      [ other is a Rational instance ->
          return the difference of self and other as a Rational
          instance ]
    .__mul__(self, other):
      [ other is a Rational instance ->
          return the product of self and other as a Rational
          instance ]
    .__truediv__(self, other):
      [ other is a Rational instance ->
          return the quotient of self and other as a Rational
          instance ]
    .__str__(self):
      [ return a string representation of self ]
    .__float__(self):
      [ return a float approximation of self ]
    .mixed(self):
      [ return a string representation of self as a mixed
        fraction ]
'''
def gcd ( a, b ):
    '''Greatest common divisor function; Euclid's algorithm.

      [ a and b are integers ->
          return the greatest common divisor of a and b ]
   '''
    if  b == 0:
        return a
    else:
        return gcd(b, a%b)

class Rational:
    """An instance represents a rational number.
    """
    def __init__ ( self, a, b ):
        """Constructor for Rational.
        """
        if  b == 0:
            raise ZeroDivisionError( "Denominator of a rational "
                "may not be zero." )
        else:
            g  =  gcd ( a, b )
            self.n  =  a // g
            self.d  =  b // g
    def __eq__ ( self, other ):
        """Determine whether two rational numbers are equal.
        """
        return self.n == other.n and self.d == other.d
    def __ne__ ( self, other ):
        return not self == other
    def __lt__ ( self, other ):
        return float(self) < float(other)
    def __le__ ( self, other ):
        return self == other or self < other
    def __gt__ ( self, other ):
        return not self <= other
    def __ge__ ( self, other ):
        return not self < other
    def __add__ ( self, other ):
        """Add two rational numbers.
        """
        return Rational ( self.n * other.d + other.n * self.d,
                          self.d * other.d )
    def __sub__ ( self, other ):
        """Return self minus other.
        """
        return Rational ( self.n * other.d - other.n * self.d,
                          self.d * other.d )
    def __mul__ ( self, other ):
        """Implement multiplication.
        """
        return  Rational ( self.n * other.n, self.d * other.d )
    def __truediv__ ( self, other ):
        """Implement division.
        """
        return  Rational ( self.n * other.d, self.d * other.n )
    def __str__ ( self ):
        '''Display self as a string.
        '''
        return "%d/%d" % ( self.n, self.d )
    def __float__ ( self ):
        """Implement the float() conversion function.
        """
        return  float ( self.n ) / float ( self.d )
    def mixed ( self ):
        """Render self as a mixed fraction in string form.
        """
        #-- 1 --
        # [ whole  :=  self.n / self.d, truncated
        #   n2  :=  self.n % self.d ]
        whole, n2  =  divmod ( self.n, self.d )
        #-- 2 --
        # [ if self.d == 1 ->
        #     return str(self.n)
        #   else if whole == zero ->
        #     return str(n2)+"/"+str(self.d)
        #   else ->
        #     return str(whole)+" and "+str(n2)+"/"+str(self.d) ]
        if  self.d == 1:
            return str(self.n)
        elif whole == 0:
            return "%s/%s" % (n2, self.d)
        else:
            return "%s and %s/%s" % (whole, n2, self.d)