#include <bits/stdc++.h>
using namespace std;
 
int main() {
  int N, A;
  cin >> N;
  cin >> A;
  for (int i = 0; i < N; i++) {
    string s;
    int B;
    cin >> s >> B;
    if (s == "+") {
      A += B;
      cout << i+1 << ":" << A << endl;
    }
    else if (s == "-") {
      A -= B;
      cout << i+1 << ":" << A << endl;
    }
    else if (s == "/") {
      if (B == 0) {
        cout << "error" << endl;
        break;
      }
      A /= B;
      cout << i+1 << ":" << A << endl;
    }
    else if (s == "*") {
      A *= B;
      cout << i+1 << ":" << A << endl;
    }
  }
}