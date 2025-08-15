#include "util.hpp"
#include <iostream>
int touch_all();
int main(){
  std::cout << greet("world") << " -> touch_all=" << touch_all() << "\n";
  return 0;
}
