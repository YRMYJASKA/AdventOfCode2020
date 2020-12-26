#include <bits/stdc++.h>

using namespace std;

struct LinkedNode {
    int val;
    LinkedNode* nxt;
};

long long solution(string starting, int N = 100, bool part2 = false) {
    int maxval = 0;
    vector<LinkedNode*> num_to_pos(9);
    LinkedNode* head = new LinkedNode;
    {
        LinkedNode* previous = head;
        head->val = starting[0] - 48;
        num_to_pos[starting[0] - 48 - 1] = head;
        for (int i = 1; i < starting.length(); i++) {
            int num = starting[i] - 48;
            LinkedNode* current = new LinkedNode;
            current->val = num;
            if (num > maxval) {
                maxval = num;
            }
            num_to_pos[num - 1] = current;
            previous->nxt = current;
            previous = current;
        }
        if (part2) {
            for (int i = maxval + 1; i <= 1000000; i++) {
                LinkedNode* current = new LinkedNode;
                current->val = i;
                num_to_pos.push_back(current);
                previous->nxt = current;
                previous = current;
            }
            maxval = 1000000;
        }

        previous->nxt = head;
    }
    LinkedNode* curr = head;
    for (int i = 0; i < N; i++) {
        int v = curr->val;
        // Snip off the next three values
        unordered_set<int> filtered_values;
        filtered_values.insert(v);
        LinkedNode* picked_up = curr->nxt;
        LinkedNode* picked_up_tail = curr;
        for (int x = 0; x < 3; x++) {
            picked_up_tail = picked_up_tail->nxt;
            filtered_values.insert(picked_up_tail->val);
        }
        curr->nxt = picked_up_tail->nxt;

        // Find the value of the destination
        int dest = 0;
        for (int x = v - 1;; x--) {
            if (x == 0) {
                x = maxval;
            }
            if (filtered_values.find(x) == filtered_values.end()) {
                dest = x;
                break;
            }
        }

        // Now look for that destination value and insert the picked up
        auto destination_node = num_to_pos[dest - 1];
        LinkedNode* t = destination_node->nxt;
        destination_node->nxt = picked_up;
        picked_up_tail->nxt = t;

        // Move on
        curr = curr->nxt;
    }
    curr = num_to_pos[0];

    if (part2) {
        return (long long)(curr->nxt->val) * (long long)(curr->nxt->nxt->val);
    }

    string answer = "";
    for (int i = 0; i < 8; i++) {
        curr = curr->nxt;
        answer += to_string(curr->val);
    }

    return atoll(answer.c_str());
}

int main() {
    string input = "685974213";
    cout << "Part 1: " << solution(input, 100) << endl;
    cout << "Part 2: " << solution(input, 10000000, true) << endl;
}
