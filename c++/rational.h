#ifndef RATIONAL_H
#define RATIONAL_H

#include <iostream>

class Rational
{
  public:

    Rational(int n=0, int d=1);  // default constructor: 0/1 
                                 // n/1 for an integer n

    int num() const;             // numerator getter
    int denom() const;           // denominator getter

    Rational operator~() const;  // reciprocal 

    friend std::ostream& operator<<(std::ostream& os, const Rational& r);

    friend Rational operator+(const Rational a, const Rational b);
    friend Rational operator-(const Rational a, const Rational b);
    friend Rational operator*(const Rational a, const Rational b);
    friend Rational operator/(const Rational a, const Rational b);

  private:
  
    int num_; 	                 // numerator
    int denom_;	                 // denominator, should be always positive

    void canonicalQ();           // canonical form 
};

#endif // RATIONAL_H;