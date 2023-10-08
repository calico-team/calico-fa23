#include <iostream>
#define ll long long
using namespace std;

class LinkedListNode{
    public:
        ll val;
        LinkedListNode* next;
    LinkedListNode(ll val){
        this->val = val;
        this->next = NULL;
    }
};

ll solve(ll N, ll K) {
    // YOUR CODE HERE
    LinkedListNode* sentinel = new LinkedListNode(-1);
    LinkedListNode* curr = sentinel;
    LinkedListNode* top = sentinel;
    ll k_position =0;
    for (int i = 1; i <= N; i++) {
        top->next = new LinkedListNode(i);
        top = top->next;
    }

    for (int i=0; i < N; i++) {
        top->next = curr->next;
        curr->next = curr->next->next;
        top = top->next;
        curr = curr->next;
    }

    for (int i=0; i <= N; i++) {
        if (sentinel->val == K) {
            k_position = i;
        }
        curr = sentinel;
        sentinel = sentinel->next;
        delete curr;
    }

    return k_position;    
}

int main() {
    int T;
    ll N, K;
    cin >> T;
    for (int i = 0; i < T; i++) {
        cin >> N >> K;
        cout << solve(N, K) << '\n';
    }
}
