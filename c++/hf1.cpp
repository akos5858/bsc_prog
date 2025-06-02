#include <iostream>
#include <vector>
#include <utility>                  // for std::pair
		     
struct Rational
{
  int num; 	                        // numerator
  int denom;	                      // denominator, should be always positive
};


int euclidean(int a, int b)         // Euclidean algorithm to find the greatest common divisor 
{     
  if (b == 0)                       // base case
  {                     
    return a;     
  }     
     
  return euclidean(b, a % b);       // recursive call
}


Rational canonicalQ(int n, int d)   // define this function
{
  int gcd = euclidean(n, d);        // find the greatest common divisor
  n /= gcd;
  d /= gcd;
  
  if (d < 0)                        // assure that the denominator is positive
  {                      
    n *= -1; 
    d *= -1; 
  }

  return {n, d};                    // return canonical form 
}


int main()
{
  std::vector<std::pair<int,int>>  test = {
     {   1,  2  },
     {   2,  4  },
     {  -2,  4  },
     {  -2, -4  },
     {   2, -4  },
     {   2,  3  },
     {   0,  2  },
     {   0, -2  },  
     {  12345678, 12345679 },      // my own test cases ->
     {   5,  5  }, 
     {  -5,  5  }, 
     {   5, -5  }, 
     {  -5, -5  }, 
     {   7,  1  },  
     {  -7,  1  },   
     {   1,  7  },  
     {   1, -7  }, 
     {  13,  17 },      
     { -13,  17 },   
     {  13, -17 },  
     { -13, -17 }, 
     {  0, 100  },
     {  29, 58  }, 
     {  37, 111 },     
     {   987654,  12345   }, 
     {  1000000, 500000   },
     { -1000000, 500000   },
     {   500000, -1000000 }
  };

  Rational q{ 2, 3 };              // this is the way to create a Rational

  for ( auto [a, b] : test )
  {
    Rational r = canonicalQ(a, b);
    std::cout << a << "/" << b << " = " 
              << r.num << '/' << r.denom << '\n';
  }

  return 0;
}

// Expected output: 
/*
1/2 = 1/2
2/4 = 1/2
-2/4 = -1/2
-2/-4 = 1/2
2/-4 = -1/2
2/3 = 2/3
0/2 = 0/1
0/-2 = 0/1
12345678/12345679 = 12345678/12345679
*/