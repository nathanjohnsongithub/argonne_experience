#define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
#define PY_SSIZE_T_CLEAN
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

static PyObject *class_instance(PyObject *self, PyObject *args){
    
    // Initialize the python interpreter
    // Note: This automatically externs C 
    Py_Initialize();

    // Ensure the GIL (Global Interpreter lock) so that multiple threads doing something doesnt cause seg fault
    PyGILState_STATE gstate;
    gstate = PyGILState_Ensure();

    const char* str;
    int num1, num2;

    // parse the args int 3 seperate variables
    // the "sii" stands for what each part of the args should be equal to
    // s = string
    // i = int
    PyArg_ParseTuple(args, "sii", &str, &num1, &num2);
     
    // Pack Them into a tuple
    PyObject* pTup = PyTuple_Pack(3, PyUnicode_FromString(str), PyLong_FromLong(num1), PyLong_FromLong(num2));

    // If there was an error stop the program
    if (PyErr_Occurred()){
        return NULL;
    }

    // Check if the Tup was successfully created
    if (!PyTuple_Check(pTup)){
        PyErr_SetString(PyExc_TypeError, "Argument must be a tuple of this format \n (string, int, int) )");
        return NULL;
    }

    // Initialize now so Its within scope of return statement
    PyObject *pInstance;

    // Add the current directory to the Python module path so it can find py_rectangle_class.py
    PyRun_SimpleString("import sys");
    PyRun_SimpleString("sys.path.append(\".\")");
    
    // Import the rectangle module
    PyObject *pName = PyUnicode_DecodeFSDefault("py_rectangle_class");
    PyObject *pModule = PyImport_Import(pName);
    Py_DECREF(pName); // Clean up pName

    // error handling making sure pModule actually works and was found
    if (pModule != NULL) {

        // Get the Rectangle class from the Module 
        PyObject *pClass = PyObject_GetAttrString(pModule, "Rectangle");
        Py_DECREF(pModule); // Clean up pModule

        // error handling. Making sure we actually found the class
        if (pClass != NULL && PyCallable_Check(pClass)) {

            // Create the instance of the class
            pInstance = PyObject_CallObject(pClass, pTup);
            Py_DECREF(pClass); // Clean up pClass
            Py_DECREF(pTup);//    Clean up pTup

            // If we successfully created the instance
            if (pInstance != NULL){

                // print out the instance
                PyObject* pStr = PyObject_Repr(pInstance);
                if (pStr != NULL) {
                    printf("[C++] Instance: %s\n\n", PyUnicode_AsUTF8(pStr));
                    Py_DECREF(pStr); // Clean up pStr
                }

                // call the __str__ method so we can print out the info of the rectangle
                PyObject* pPrint = PyObject_CallMethod(pInstance, "__str__", NULL);
                if (pPrint != NULL){
                    printf("\n[C++]\n%s\n", PyUnicode_AsUTF8(pPrint));
                    Py_DECREF(pPrint); // Clean up pPrint
                }
            
                // call the area method
                // pArea is equal to what the area function returned 
                PyObject *pArea = PyObject_CallMethod(pInstance, "area", NULL);
                if (pArea != NULL){
                    // if we actually have a pArea, print it out
                    printf("\n[C++] Returned area: %ld\n\n  ", PyLong_AsLong(pArea));
                    Py_DECREF(pArea);
                }

                // Release the GIL state so all threads can work together again. 
                PyGILState_Release(gstate);
            }
        }
    }

    // return the class instance
    return pInstance;
    
}

// header for the methods
static PyMethodDef methods[] = {
    {"multiply", multiply, METH_VARARGS, "Multiple every element in numpy array by 5"},
    {"class_instance", class_instance, METH_VARARGS, "create class from python then return it"},
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
    printf("Activated!\n================================\n\n");
    PyObject *module = PyModule_Create(&calculator);
    import_array();
    return module;
}
