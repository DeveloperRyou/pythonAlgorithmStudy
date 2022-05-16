/*
보석줍기
어떤 인덱스에서 M 이상의 구간합을 최대로 만들기
*/
#include <iostream>
#define INF 2147483647
using namespace std;

int main()
{
	int N, M;
	cin>>N>>M;
	int arr[100000];
	for (int i=0;i<N;i++)
		cin>>arr[i];
	int DP[100000];
	int presum[100000];
	presum[0] = arr[0];
	for (int i=1;i<N;i++){
		presum[i] = presum[i-1] + arr[i];
	}
	DP[M-1] = presum[M-1];
	int answer = DP[M-1];
	for (int i=M;i<N;i++){
		DP[i] = max(presum[i] - presum[i-M], DP[i-1] + arr[i]);
		answer = max(answer, DP[i]);
	}
	if (answer < 0)
		cout<<0;
	else cout<<answer;
}
