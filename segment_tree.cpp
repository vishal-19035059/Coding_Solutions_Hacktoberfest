// Segment Tree ?
// Segment Tree is a basically a binary tree used for storing the intervals or segments. Each node in the Segment Tree represents an interval. Consider an array A of size N and a corresponding Segment Tree T:

// The root of T will represent the whole array A[0 : N-1].
// Each leaf in the Segment Tree T will represent a single element A[i] such that 0<=i<N.
// The internal nodes in the Segment Tree T represents the union of elementary intervals A[i : j] where 0<=i<j<N.

//Build segment tree

#include <bits/stdc++.h>
using namespace std;
vector<int>tree , A;

void build(int node, int start, int end)
{
    if(start == end)
    {
        // Leaf node will have a single element
        tree[node] = A[start];
    }
    else
    {
        int mid = (start + end) / 2;
        // Recurse on the left child
        build(2*node, start, mid);
        // Recurse on the right child
        build(2*node+1, mid+1, end);
        // Internal node will have the sum of both of its children
        tree[node] = tree[2*node] + tree[2*node+1];
    }
}
