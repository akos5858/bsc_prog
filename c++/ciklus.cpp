#include <iostream>

int main() {
    for (int i=0; i < 6; i++){
        std::cout << i;
    }
    std::cout << '\n';
    for (int i=0; i < 6; ++i){
        std::cout << i;
    }
}