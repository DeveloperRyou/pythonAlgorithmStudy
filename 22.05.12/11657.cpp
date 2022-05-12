/*
타임머신
음수가중치 -> 다익스트라 불가능
벨만포드 : O(EV)
*/

#include <iostream>
#include <vector>
#include <tuple>
#define INF 99999999999999

using namespace std;

int main()
{
	int N, M;
	cin>>N>>M;
	vector<tuple<int, int, int>> edges;
	for (int i=0;i<M;i++){
		int a, b, c;
		cin>>a>>b>>c;
		edges.emplace_back(a, b, c);
	}

	long long dist[501];
	for (int i=0;i<=N;i++)
		dist[i] = INF;
	dist[1] = 0;
	// 벨만포드
	for (int idx = 1;idx<=N;idx++){ 
		// 최대 노드개수만큼 움직일 수 있음, +1의 이동에서 갱신시 음의 순환 발생
		for (auto edge : edges){
			// 모든 간선 검사
			int node = get<0>(edge);
			int to = get<1>(edge);
			int weight = get<2>(edge);

			if (dist[node] != INF && dist[node]+weight < dist[to]){ // 갱신가능
				if (idx == N){ // 음의 순환
					cout<<-1;
					return 0;
				}
				dist[to] = dist[node]+weight;
			}
		}
	}
	// 출력
	for (int idx=2;idx<=N;idx++){
		if (dist[idx] == INF)
			dist[idx] = -1;
		cout<<dist[idx]<<endl;
	}
}