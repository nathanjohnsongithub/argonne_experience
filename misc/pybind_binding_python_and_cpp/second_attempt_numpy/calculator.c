#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#include <Python.h>
#include <numpy/arrayobject.h>
#include <stdio.h>

// multiply method which multiplies every element of numpy array by 5 and return an array with those values as doubles
static PyObject *multiply(PyObject *self, PyObject *args) {
    // make array of PyObject
    PyArrayObject *arr;
    // populate array
    PyArg_ParseTuple(args, "O", &arr);
    //error handling
    if (PyErr_Occurred()){
        return NULL;
    }
    //more error handling
    if (!PyArray_Check(arr)) {
        PyErr_SetString(PyExc_TypeError, "Argument must be a numpy array");
        return NULL;
    }

    // get size of the array
    int64_t size = PyArray_SIZE(arr); // equivalent to len(arr)
    // new array to store the args and also for error handling
    double *data;
    // number of dimensions of the array
    npy_intp dims[] = { [0] = size};
    // even more error handling and making data = arr
    PyArray_AsCArray((PyObject **)&arr, &data, dims, 1, PyArray_DescrFromType(NPY_DOUBLE));
    // error handling
    if (PyErr_Occurred()) {
        return NULL;
    }

    // create new PyObject that we can return to python 
    PyObject *result = PyArray_SimpleNew(1, dims, NPY_DOUBLE);
    double *result_data = PyArray_DATA((PyArrayObject *)result);

    // actually multiply everything
    for (int i = 0; i < size; ++i) {
        result_data[i] = 5.0 * data[i];
    }

    return result;
}

// header for the methods
static PyMethodDef methods[] = {
    {"multiply", multiply, METH_VARARGS, "Multiple every element in numpy array by 5"},
    { NULL, NULL, 0, NULL }
};

// defines the basic information and structure for "calulator" module
static struct PyModuleDef calculator = {
    PyModuleDef_HEAD_INIT,
    "calculator",
    "This is a module for numpy in c",
    -1,
    methods
};

// initilization 
PyMODINIT_FUNC PyInit_calculator() {
    printf("Activated!\n");
    PyObject *module = PyModule_Create(&calculator);
    import_array();
    return module;
}