#include <bits/stdc++.h>
using namespace std;
 
int main() {
  string s;
  int ans = 1;
  cin >> s;
  for (int i = 0; i < s.size()/2; i++){
    if (s.at(2*i+1) == '+') {
      ans++;
    } else {
      ans--;
    }
  }
  cout << ans << endl;
}