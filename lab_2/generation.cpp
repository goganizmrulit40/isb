#include <iostream>
#include <random>
#include <string>
#include <fstream>


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


void write_bits_to_file(const std::string& bits, const std::string& filename) {
    std::ofstream outFile(filename);
    if (outFile.is_open()) {
        outFile << bits;
        outFile.close();
    } else {
        std::cerr << "Error when opening a file" << std::endl;
    }
}



int main() {
    std::string bits = generate_random_bits(128);
    std::cout << "Random binary sequence: " << std::endl << bits << std::endl;

    write_bits_to_file(bits, "random_bits_cpp.txt");

    return 0;
}
