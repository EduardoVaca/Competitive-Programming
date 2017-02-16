#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int get_minimum_coins(vector<int>& coins, int sum) {
  int min_coins = 0;
  int current_sum = 0;
  sort(coins.begin(), coins.end());
  for(int i = coins.size() - 1; i >= 0; i--) {
    min_coins += 1;
    current_sum += coins[i];
    sum -= coins[i];
    if(current_sum > sum){
      break;
    }
  }
  return min_coins;
}

int main() {
  ios_base::sync_with_stdio(false);
  int rep, coin, sum_coins = 0;
  vector<int> coins;
  cin >> rep;

  for (int i = 0; i < rep; i++) {
    cin >> coin;
    coins.push_back(coin);
    sum_coins += coin;
  }
  cout << get_minimum_coins(coins, sum_coins) << endl;
}
