#include <iostream>

using namespace std;

class LinkedListNode{
    public:
        int val;
        LinkedListNode* next;
        LinkedListNode(int val) {
            this->val = val;
            this->next = NULL;
        }
};

int solve(int N, int K) {
    LinkedListNode* sentinel = new LinkedListNode(-1);
    LinkedListNode* curr = sentinel;
    LinkedListNode* top = sentinel;
    for (int i = 1; i <= N; i++) {
        top->next = new LinkedListNode(i);
        top = top->next;
    }

    for (int i = 0; i < N; i++) {
        top->next = curr->next;
        curr->next = curr->next->next;
        top = top->next;
        curr = curr->next;
    }

    int k_position = -1;
    for (int i = 0; i <= N; i++) {
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
    int N, K;
    cin >> T;
    for (int i = 0; i < T; i++) {
        cin >> N >> K;
        cout << solve(N, K) << '\n';
    }
}
