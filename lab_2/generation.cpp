#include <iostream>
#include <random>
#include <string>


std::string generate_random_bits(int length) {
    std::string bits;
    std::random_device rd;
    std::mt19937 gen(rd()); //Вихрь Мерсенна
    std::uniform_int_distribution<> dis(0, 1);

    for (int i = 0; i < length; ++i) {
        bits += std::to_string(dis(gen));
    }

    return bits;
}


int main() {
    std::string bits = generate_random_bits(128);
    std::cout << "Random binary sequence: " << std::endl << bits << std::endl;
    return 0;
}
