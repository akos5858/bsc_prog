#include <iostream>
#include <vector>
#include <utility>   // for std::pair
#include <cassert>   // for assert
#include <numeric>   // for std::gcd
		    
struct Rational
{
  int num; 	    // numerator
  int denom;	  // denominator, should be always positive
};

// output function for a Rational number
std::ostream& operator<<(std::ostream& os, Rational r)
{
  os << "( " << r.num << "/" << r.denom << " )";
  return os;
}

Rational canonicalQ( int n, int d);

// this four functions should be implemented:
Rational add( Rational r1, Rational r2)
{
  return canonicalQ( r1.num * r2.denom + r2.num * r1.denom, r1.denom * r2.denom);
};

Rational sub( Rational r1, Rational r2)
{
  return canonicalQ( r1.num * r2.denom - r2.num * r1.denom, r1.denom * r2.denom);
};

Rational mul( Rational r1, Rational r2)
{
  return canonicalQ( r1.num * r2.num, r1.denom * r2.denom);
};

Rational div( Rational r1, Rational r2)
{
  return canonicalQ( r1.num * r2.denom, r1.denom * r2.num);
};


int main()
{
  std::vector<std::vector<std::pair<int,int>>>  test_input = {
    {  {  1,  2 }, {  2,  4 } },
    {  { -2,  4 }, {  2, -3 } },
    {  {  0,  2 }, {  5,  8 } }
  };

  for ( auto v : test_input )
  {
    Rational r1 = canonicalQ( v[0].first, v[0].second);
    Rational r2 = canonicalQ( v[1].first, v[1].second);

    std::cout << r1 << " + " << r2 << " == " << add(r1,r2) << '\n';
    std::cout << r1 << " - " << r2 << " == " << sub(r1,r2) << '\n';
    std::cout << r1 << " * " << r2 << " == " << mul(r1,r2) << '\n';
    std::cout << r1 << " / " << r2 << " == " << div(r1,r2) << '\n';
  }
}

// create canonical format of Rational number
// denominator should be always positive
Rational canonicalQ( int n, int d)
{
  assert( 0 != d );
  if ( 0 == n ) return Rational{ 0, 1 };

  int g = std::gcd( n, d); 
  if ( d < 0 ) 
  {
    n = -n;
    d = -d;
  }
  return Rational{ n/g, d/g };
}

/* expected output:
 
( 1/2 ) + ( 1/2 ) == ( 1/1 )
( 1/2 ) - ( 1/2 ) == ( 0/1 )
( 1/2 ) * ( 1/2 ) == ( 1/4 )
( 1/2 ) / ( 1/2 ) == ( 1/1 )
( -1/2 ) + ( -2/3 ) == ( -7/6 )
( -1/2 ) - ( -2/3 ) == ( 1/6 )
( -1/2 ) * ( -2/3 ) == ( 1/3 )
( -1/2 ) / ( -2/3 ) == ( 3/4 )
( 0/1 ) + ( 5/8 ) == ( 5/8 )
( 0/1 ) - ( 5/8 ) == ( -5/8 )
( 0/1 ) * ( 5/8 ) == ( 0/1 )
( 0/1 ) / ( 5/8 ) == ( 0/1 )

*/