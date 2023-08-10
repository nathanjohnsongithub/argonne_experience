#include <iostream>
#include <vector>
using namespace std;

void print_vector(vector<int> v1){

    cout << " < ";
    for (auto i = v1.begin(); i != v1.end(); ++i){
        cout << *i << " ";
    }
    cout << "> " << endl;

} 

void print_matrix(vector<vector<int>> m1){

    for (vector<int> vect1D : m1) {
        for (int x : vect1D){
            cout << x << " ";
        }    
        cout << endl;
    }
}

vector<vector<int>> populate_matrix(vector<vector<int>> m, vector<int> v1, vector<int> v2){

    for (int i = 0; i < v1.size(); ++i) {
        for (int j = 0; j < v2.size(); ++j) {
            m[i][j] = v1[i] * v2[j];
        }
    }

    return m;
}

int main() {
    
    vector<int> v1 = {1,2,3,4,5};
    vector<int> v2 = {1,2,3,4,5};

    print_vector(v1);
    print_vector(v2);

    // vector<vector<int>> matrix = {
    //         {1,2,3},
    //         {4,5,6},
    //         {7,8,9}
    // };

    int default_value = 0;

    int size = v1.size();

    vector<int> v(size, default_value);

    vector<vector<int>> matrix(size, v);

    print_matrix(matrix);

    matrix = populate_matrix(matrix, v1, v2);

    print_matrix(matrix);

} 