#include <bits/stdc++.h>
using namespace std;

int main() {
  vector<int> data(5);
  bool flg = false;
  for (int i = 0; i < 5; i++) {
    cin >> data.at(i);
    if (i != 0) {
      if (data.at(i-1) == data.at(i)) {
        flg = true;
      }
    }
  }
  if (flg) {
    cout << "YES" << endl;
  } else {
    cout << "NO" << endl;
  }
}
