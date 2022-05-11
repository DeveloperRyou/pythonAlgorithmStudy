/**
최소비용 구하기
A에서 B까지의 최소 : 다익스트라 O(ElogV)
**/
#include <iostream>
#include <vector>
#include <queue>
#define INF 2147483647

using namespace std;
int main()
{
	ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

	int N, M;
	vector<pair<int, int> > list[1001]; // weight, next

	cin>>N>>M;
	for (int i=0;i<M;i++){
		int here, next, weight;
		cin>>here>>next>>weight;
		list[here].emplace_back(weight, next);
	}
	int st, ed;
	cin>>st>>ed;
	
	priority_queue<pair<int, int>, vector<pair<int, int> >, greater<pair<int, int> > > que;
	que.emplace(0, st);
	
	int dist[1001];
	for (int i=0;i<1001;i++)
		dist[i] = INF;
	dist[st]=0;

	while (!que.empty())
	{
		auto p = que.top();
		que.pop();

		int weight = p.first;
		int here = p.second;
		if (dist[here] < weight)
			continue;
		
		for (auto next : list[here]){
			int next_weight = next.first + weight;
			int next_node = next.second;
			if (next_weight < dist[next_node]){
				dist[next_node] = next_weight;
				que.emplace(next_weight, next_node);
			}
		}
	}
	cout<<dist[ed]<<endl;
}