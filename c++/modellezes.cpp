#include <cmath>
#include <vector>
#include <algorithm>

const double h = 6.62607015e-34;
const double c = 299792458;
const double boltzmann = 1.380649e-23;

int partition(int n, std::vector<int> omegas) {
    int m = omegas.size();
    std::vector<int> dp(n+1, 0);
    dp[0] = 1;
    for (int i = 0; i < m; i++) {
        for (int j = omegas[i]; j <= n; j++) {
            dp[j] += dp[j-omegas[i]];
        }
    }
    return dp[n];
}

double Q(double Temperature, std::vector<int> molecule) {
    double const_val = 100 * h * c / (boltzmann * Temperature);
    int upper_bound = round(10 * Temperature);
    double sum = 0;
    for (int k = upper_bound; k >= 0; k--) {
        sum += partition(k, molecule) * exp(-const_val*k);
    }
    return sum;
}

double dQ(double Temperature, std::vector<int> molecule) {
    double const_val = 100 * h * c / (boltzmann * Temperature);
    int upper_bound = round(10 * Temperature);
    double sum = 0;
    for (int k = upper_bound; k >= 0; k--) {
        sum += k * partition(k, molecule) * exp(-const_val*k);
    }
    sum *= 1/(boltzmann * pow(Temperature, 2));
    return sum;
}

double d2Q(double Temperature, std::vector<int> molecule) {
    double const_val = 100 * h * c / (boltzmann * Temperature);
    int upper_bound = round(10 * Temperature);
    double sum = 0;
    for (int k = upper_bound; k >= 0; k--) {
        sum += pow(k, 2) * partition(k, molecule) * exp(-const_val*k);
    }
    sum *= 1/pow(boltzmann * Temperature, 4);
    return sum;
}