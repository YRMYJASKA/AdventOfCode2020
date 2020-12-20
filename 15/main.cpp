#include <bits/stdc++.h>

using namespace std;

int solution(vector<long> starting, long limit = 2020) {
    unordered_map<long, long> locations;
    for (int i = 0; i < starting.size() - 1; i++) locations[starting[i]] = i;
    long prev;
    long curr = starting[starting.size() - 1];
    for (int i = starting.size() - 1; i < limit; i++) {
        prev = curr;
        if (locations.find(curr) != locations.end()) {
            curr = i - locations[curr];
        } else {
            curr = 0;
        }
        locations[prev] = i;
    }
    return prev;
}

int main() {
    vector<long> input = {0, 14, 1, 3, 7, 9};
    cout << "solution: " << solution(input, 30000000) << endl;
}
