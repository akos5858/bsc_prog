#include <iostream>
#include <vector>
#include <utility>   // for std::pair
#include <cassert>   // for assert
#include <numeric>   // for std::gcd
		    
#include "rational.h"

// constructor
Rational::Rational(int n, int d) : num_(n), denom_(d) {
    assert(d != 0);
    canonicalQ();    // ensure canonical form
}

// normalizer
void Rational::canonicalQ() 
{
    assert( 0 != denom_ );

    if (num_ == 0) 
    {
        denom_ = 1;
        return;
    }
    
    if ( denom_ < 0 ) 
    {
        num_ = -num_;
        denom_ = -denom_;
    }

    int gcd = std::gcd(num_, denom_);
    num_ /= gcd;
    denom_ /= gcd;
}

// getters
int Rational::num() const {
    return num_;
}

int Rational::denom() const {
    return denom_;
}

// reciprocal
Rational Rational::operator~() const {
    return Rational(denom_, num_);
}

// output stream operator
std::ostream& operator<<(std::ostream& os, const Rational& r) {
    os << r.num_ << "/" << r.denom_;
    return os;
}

// arithmetic operators
Rational operator+(const Rational a, const Rational b) {
    return Rational(a.num_ * b.denom_ + b.num_ * a.denom_, a.denom_ * b.denom_);
}

Rational operator-(const Rational a, const Rational b) {
    return Rational(a.num_ * b.denom_ - b.num_ * a.denom_, a.denom_ * b.denom_);
}

Rational operator*(const Rational a, const Rational b) {
    return Rational(a.num_ * b.num_, a.denom_ * b.denom_);
}

Rational operator/(const Rational a, const Rational b) {
    return Rational(a.num_ * b.denom_, a.denom_ * b.num_);
}



int main()
{
  std::vector<std::vector<std::pair<int,int>>>  test_input = {
    { {  1,  2 }, {  2,  4 } },
    { { -2,  4 }, {  2, -3 } },
    { {  0,  2 }, {  5,  8 } }
  };

  for ( auto v : test_input )
  {
    Rational r1{ v[0].first, v[0].second };
    Rational r2{ v[1].first, v[1].second };

    std::cout << r1 << " + " << r2 << " == " << (r1+r2) << '\n';
    std::cout << r1 << " - " << r2 << " == " << (r1-r2) << '\n';
    std::cout << r1 << " * " << r2 << " == " << (r1*r2) << '\n';
    std::cout << r1 << " / " << r2 << " == " << (r1/r2) << '\n';
  }
  Rational x{16,-12};
  std::cout << "x{16/-12} == " << x.num() << "/" << x.denom() << '\n';
  Rational y{7};  // Rational(7/1)
  std::cout << "y{7} == " << y.num() << "/" << y.denom() << '\n';
  Rational z;     // Rational(0/1)
  std::cout << "z == " << z.num() << "/" << z.denom() << '\n';
  Rational v = x;  
  std::cout << "v == " << v << '\n';
  std::cout << "~v == " << ~v << '\n';  // reciprocal
  std::cout << "1 + ~v == " << (1 + ~v) << '\n';
  std::cout << "(1 + ~v)/2 == " << ((1 + ~v) / 2) << '\n';

  return 0;
}

/* expected output:

1/2 + 1/2 == 1/1
1/2 - 1/2 == 0/1
1/2 * 1/2 == 1/4
1/2 / 1/2 == 1/1
-1/2 + -2/3 == -7/6
-1/2 - -2/3 == 1/6
-1/2 * -2/3 == 1/3
-1/2 / -2/3 == 3/4
0/1 + 5/8 == 5/8
0/1 - 5/8 == -5/8
0/1 * 5/8 == 0/1
0/1 / 5/8 == 0/1
x{16/-12} == -4/3
y{7} == 7/1
z == 0/1
v == -4/3
~v == -3/4
1 + ~v == 1/4
(1 + ~v)/2 == 1/8

*/