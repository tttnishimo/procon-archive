#include <bits/stdc++.h>
using namespace std;
 
int main() {
  int N, M;
  cin >> N >> M;
  vector<int> A(M), B(M);
  for (int i = 0; i < M; i++) {
    cin >> A.at(i) >> B.at(i);
  }
 
  // ここにプログラムを追記
  // (ここで"試合結果の表"の2次元配列を宣言)
  vector<vector<char>> S(N,vector<char>(N));
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      S.at(i).at(j) = '-';
    }
  }
  for (int i = 0; i < M; i++) {
    S.at(A.at(i)-1).at(B.at(i)-1) = 'o';
    S.at(B.at(i)-1).at(A.at(i)-1) = 'x';
  }
  for (int i = 0; i < N; i++) {
    for (int j = 0; j < N; j++) {
      cout << S.at(i).at(j);
      if (j == N-1) {
        cout << endl;
      } else {
        cout << ' ';
      }
    }
  }
}