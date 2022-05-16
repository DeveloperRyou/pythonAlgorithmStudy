/*
작업
위상정렬하면서 걸리는 시간 파악하기
bfs로 찾기
*/
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main()
{
	int N;
	cin>>N;
	int time[10000] =  {0, };
	int workcount[10000] = {0, };
	int mx[10000] =  {0, };
	vector<int> nextwork[10000];
	
	for (int i=0;i<N;i++){
		int num;
		cin>>time[i]>>num;
		workcount[i] = num;
		for (int j=0;j<num;j++){
			int temp;
			cin>>temp;
			nextwork[temp-1].push_back(i);
		}
	}
	queue<pair<int, int>> que;
	for (int i=0;i<N;i++)
		if (workcount[i] == 0)
			que.emplace(i, time[i]);
	int answer = 0;
	while (!que.empty()){
		auto node_pair = que.front(); que.pop();
		int node = node_pair.first;
		int weight = node_pair.second;
		answer = max(answer, weight);
		for (auto idx : nextwork[node]){
			mx[idx] = max(mx[idx], weight);
			workcount[idx]--;
			if (workcount[idx] == 0)
				que.emplace(idx, mx[idx] + time[idx]);
		}
	}
	cout<<answer;
}
