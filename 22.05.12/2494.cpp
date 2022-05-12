/*
숫자 맞추기
왼쪽(숫자 커질때)는 아래 숫자 같이 커지고
오른쪽(숫자 작아질때)는 해당 숫자만 바뀜
10번 회전시 원상태
회전상태를 인덱스로 하는 DP
*/

#include <iostream>
#include <stdio.h>
#include <vector>
#include <queue>
#include <stack>

#define INF 999999999

using namespace std;

pair<int, int> find_rotate(int s, int e) // left, right rota
{
	if (s<e)
		return make_pair(e-s, 10-(e-s));
	else if (e<s)
		return make_pair(10-(s-e), s-e);
	else
		return make_pair(0,0);	
}

int main()
{
	int N;
	cin>>N;

	int st[10000], ed[10000];
	for (int i=0;i<N;i++)
		scanf("%1d", &st[i]);
	for (int i=0;i<N;i++)
		scanf("%1d", &ed[i]);
	
	// 현재 회전상태에서 최소 회전수, 그 전 회전상태(경로찾기 위함)
	pair<int, int> DP[10][10000];
	for (int i=0;i<10;i++)
		for (int j=0;j<N;j++)
			DP[i][j] = make_pair(INF, INF);
	pair<int, int> rota = find_rotate(st[0], ed[0]);
	DP[rota.first][0] = make_pair(rota.first, 0); // left rota
	DP[0][0] = make_pair(rota.second, 0); // right rota

	for (int j=0;j<N-1;j++){
		for (int i=0;i<10;i++){
			if (DP[i][j].first != INF){
				rota = find_rotate((st[j+1] + i)%10, ed[j+1]); // 회전한거 반영
				
				if (DP[i][j].first + rota.first < DP[(i + rota.first)%10][j+1].first)
					DP[(i + rota.first)%10][j+1] = make_pair(DP[i][j].first + rota.first, i); // left rota
				if (DP[i][j].first + rota.second < DP[i][j+1].first)
					DP[i][j+1] = make_pair(DP[i][j].first + rota.second, i); // right rota
			}
		}
	}
	int idx;
	int weight = INF;
	for (int i=0;i<10;i++){
		if (DP[i][N-1].first < weight){
			weight = DP[i][N-1].first;
			idx = i;
		}
	}
	cout<<weight<<endl;
	stack<pair<int, int> > stk;
	for (int i=N-1;i>0;i--){
		bool is_left = true;
		if (idx == DP[idx][i].second)
			is_left = false;
		int weight = DP[idx][i].first - DP[DP[idx][i].second][i-1].first;
		if (!is_left)
			weight = -weight;
		stk.emplace(i+1, weight);
		idx = DP[idx][i].second;
	}
	if (idx == 0)
		stk.emplace(1, -DP[idx][0].first);
	else
		stk.emplace(1, DP[idx][0].first);
	while (!stk.empty())
	{
		pair<int, int> out = stk.top(); stk.pop();
		printf("%d %d\n", out.first, out.second);
	}
}
