#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;
int main()
{
	int N, K;
	int coin[100];

	cin>>N>>K;
	for (int i=0;i<N;i++)
		cin>>coin[i];
	sort(coin, coin+N);

	int DP[10001];
	memset(DP, 0, sizeof(int)*10001);
	DP[0] = 1;
	for (int i=0;i<N;i++){
		for (int j=0;j<=K;j++){
			if (j - coin[i] >= 0){
				DP[j] += DP[j - coin[i]];
			}
		}
	}
	cout<<DP[K]<<endl;
}