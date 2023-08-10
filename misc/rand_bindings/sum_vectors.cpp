#include <vector>
#include <iostream>
using namespace std;

extern "C" {
    void sum_vectors(const int* vec1, const int* vec2, int size, int* result) {
        vector<int> v1(vec1, vec1 + size);
        vector<int> v2(vec2, vec2 + size);

        vector<int> v(size, 0);

        vector<vector<int>> sum(size, vector<int>(size));

        for (int i = 0; i < v1.size(); ++i) {
            for (int j = 0; j < v2.size(); ++j) {
                sum[i][j] = v1[i] * v2[j];
            }   
        }

        int* dest = result;
        for (const auto& row : sum) {
            dest = copy(row.begin(), row.end(), dest);
        }
    }
}