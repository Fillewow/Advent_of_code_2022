#include <iostream>
#include <fstream>
#include <string>
#include <ostream>
#include <vector>
#include <iterator>
#include <algorithm>
int main()
{

    std::ifstream is("input.txt");
    std::istream_iterator<int> start(is), end;
    std::vector<int> numbers(start, end);
    std::cout << "Read " << numbers.size() << " numbers" << std::endl;

    std::cout << "numbers read in:\n";
    std::copy(numbers.begin(), numbers.end(),
              std::ostream_iterator<double>(std::cout, " "));
    std::cout << std::endl;

    return 0;
}