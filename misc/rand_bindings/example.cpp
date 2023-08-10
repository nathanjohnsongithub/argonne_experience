#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <vector>

using namespace std;
namespace py = pybind11;

py::array_t<double> sum_vectors(py::array_t<double> input1, py::array_t<double> input2) {
    // Get the input arrays as C++ vectors
    py::buffer_info info1 = input1.request();
    py::buffer_info info2 = input2.request();
    vector<double> vec1(static_cast<double*>(info1.ptr), static_cast<double*>(info1.ptr) + info1.size);
    vector<double> vec2(static_cast<double*>(info2.ptr), static_cast<double*>(info2.ptr) + info2.size);

    // Perform vector addition
    vector<double> sum_vec;
    size_t size = max(vec1.size(), vec2.size());
    sum_vec.reserve(size);
    for (size_t i = 0; i < size; ++i) {
        double val1 = (i < vec1.size()) ? vec1[i] : 0.0;
        double val2 = (i < vec2.size()) ? vec2[i] : 0.0;
        sum_vec.push_back(val1 + val2);
    }

    // Create a new numpy array to hold the result
    py::array_t<double> result(size);
    py::buffer_info result_info = result.request();
    double* result_data = static_cast<double*>(result_info.ptr);
    
    // Copy the sum vector data to the result array
    copy(sum_vec.begin(), sum_vec.end(), result_data);

    return result;
}

PYBIND11_MODULE(example, m) {
    m.def("sum_vectors", &sum_vectors, "Compute the sum of two vectors");
}
