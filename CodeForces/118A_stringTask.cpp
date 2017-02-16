#include <iostream>

using namespace std;

void get_new_string(string s) {
  for(char c : s) {
    if (c < 'a') {
      c = c + 32;
    }
    if(c != 'a' && c != 'e' && c != 'i' && c != 'o' && c != 'u' && c != 'y')
      cout << "." << c;
  }
  cout << endl;
}

int main() {
  ios_base::sync_with_stdio(false);
  string s;
  cin >> s;
  get_new_string(s);
  return 0;
}
