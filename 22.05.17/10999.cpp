/*
구간합구하기 2
세그먼트 트리 - lazy 사용
*/
#include <iostream>

using namespace std;
long long tree[2200000];
long long lazy[2200000];
long long leaf[1000000];
int N, M, K;

void makeTree(int st, int ed, int idx)
{
	if (st == ed){
		tree[idx] = leaf[st];
	}
	else{
		int mid = (st+ed)/2;
		makeTree(st, mid, idx*2 + 1);
		makeTree(mid + 1, ed, idx*2 + 2);
		tree[idx] = tree[idx*2 + 1] + tree[idx*2 + 2];
	}
}

void lazy_update(int st, int ed, int idx)
{
	tree[idx] += (long long)(ed - st + 1) * lazy[idx];
	if (st != ed){
		lazy[idx*2 + 1] += lazy[idx];
		lazy[idx*2 + 2] += lazy[idx];
	}
	lazy[idx] = 0;
}

void update(int st, int ed, int idx, long long prefix_st, long long prefix_ed, long long val)
{
	if (lazy[idx] != 0) lazy_update(st, ed, idx);
	
	if (prefix_ed < st || ed < prefix_st) return;
	if (prefix_st <= st && ed <= prefix_ed){ // set lazy
		lazy[idx] += val;
		lazy_update(st, ed, idx);
	}
	else{
		int mid = (st+ed)/2;
		update(st, mid, idx*2 + 1, prefix_st, prefix_ed, val);
		update(mid+1, ed, idx*2 + 2, prefix_st, prefix_ed, val);
		tree[idx] = tree[idx*2 + 1] + tree[idx*2 + 2];
	}
}

long long query(int st, int ed, int idx, long long prefix_st, long long prefix_ed)
{
	if (lazy[idx] != 0) lazy_update(st, ed, idx);

	if (prefix_ed < st || ed < prefix_st) return 0;
	if (prefix_st <= st && ed <= prefix_ed) 
		return tree[idx];
	else{
		int mid = (st+ed)/2;
		return query(st, mid, idx*2 + 1, prefix_st,  prefix_ed) + \
			query(mid+1, ed, idx*2 + 2, prefix_st, prefix_ed);
	}
}

int main()
{
	cin>>N>>M>>K;
	for (int i=0;i<N;i++)
		cin>>leaf[i];
	makeTree(0,N-1,0);
	for (int i=0;i<M+K;i++){
		long long a, b, c, d;

		cin>>a;
		if (a==1){ // update
			cin>>b>>c>>d;
			update(0, N-1, 0, b-1, c-1, d);
		}
		else{ // query
			cin>>b>>c;
			cout<<query(0, N-1, 0, b-1, c-1)<<endl;
		}
	}
}
