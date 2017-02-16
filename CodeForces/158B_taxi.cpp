#include <iostream>
#include <vector>

using namespace std;

const int kids_per_taxi = 4;

int get_minimum_by_summary(vector<int>& summary) {
  int taxis = 0;
  taxis += summary[kids_per_taxi - 1];
  taxis += summary[kids_per_taxi - 2];
  summary[0] -= summary[kids_per_taxi - 2];
  taxis += (summary[kids_per_taxi - 3] / 2);

  if(summary[1] % 2 != 0) {
    taxis += 1;
    summary[0] -= 2;
  }
  if(summary[0] > 0) {
    taxis += summary[0] / 4;
    if(summary[0] % 4 != 0) {
      taxis += 1;
    }
  }
  return taxis;
}

int get_minimum_taxis(vector<int>& groups, int size) {
  vector<int> summary (4, 0);
  for(int i = 0; i < size; i++) {
    summary[groups[i] - 1] += 1;
  }
  return get_minimum_by_summary(summary);
}

int main() {
  ios_base::sync_with_stdio(false);
  int n_groups, current;
  cin >> n_groups;
  vector<int> groups;
  for (int i = 0; i < n_groups; i++) {
    cin >> current;
    groups.push_back(current);
  }
  cout << get_minimum_taxis(groups, n_groups) << endl;
  return 0;
}
