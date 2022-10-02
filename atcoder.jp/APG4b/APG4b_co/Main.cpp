#include <bits/stdc++.h>
using namespace std;

int main() {
  int p;
  cin >> p;

  if (p == 1) {
    int price;
    int N;
    cin >> price;
    cin >> N;
    cout << price * N << endl;
  }

  if (p == 2) {
    string text;
    int price;
    int N;
    cin >> text >> price;
    cin >> N;
    cout << text << "!" << endl;
    cout << price * N << endl;
  }
}
