#include <iostream>
#include <vector>
#include <map>

using namespace std;

int get_kth_divisor(int n, int k) {
  if(k == 1)
    return 1;
  vector<int> low_divisors;
  vector<int> high_divisors;
  map<int, bool> already_divided;
  int aux, current_size, size = 0;
  for(int i = 1; i <= n; i++) {
    if(n % i == 0) {
      if(already_divided.find(i) != already_divided.end()) {
        break;
      } else {
        aux = n / i;
        size++;
        already_divided[aux] = true;
        if(i == n / i) {
          aux = high_divisors[size - 2];
        }
        high_divisors.push_back(aux);
        low_divisors.push_back(i);
        if (size == k) {
          return low_divisors[k - 1];
        }
      }
    }
  }
  if(size * 2 >= k){
    return high_divisors[size - (k - size)];
  }
  return -1;
}

int main() {
  ios_base::sync_with_stdio(false);
  int n, k;
  cin >> n >> k;
  cout << get_kth_divisor(n, k) << endl;
  return 0;
}
