// we define PY_SSIZE_T_CLEAN because the documentation recommended it
#define PY_SSIZE_T_CLEAN
#include <Python.h>

int main() {

    // Initialize the python interpreter
    // Note: This automatically externs C 
    Py_Initialize();

    // Initialize all of the variables we will use
    // Also do this for each variable this is just what I did
    PyObject *pName, *pModule, *pDict, *pClass, *pArgs, *pInstance, 
    *pValue, *pAttrName, *pAttrWidth, *pAttrHeight;

    // Add the current directory to the Python module path so it can find py_rectangle_class.py
    PyRun_SimpleString("import sys");
    PyRun_SimpleString("sys.path.append(\".\")");
    
    // Import the rectangle module
    pName = PyUnicode_DecodeFSDefault("py_rectangle_class");
    pModule = PyImport_Import(pName);

    // error handling making sure pModule actually works and was found
    if (pModule != NULL) {
        // Get the Rectangle class from the Module 
        pDict = PyModule_GetDict(pModule); 
        pClass = PyObject_GetAttrString(pModule, "Rectangle");

        // error handling. Making sure we actually found the class
        if (pClass != NULL && PyCallable_Check(pClass)) {
            
            // Create a Python tuple to hold constructor arguments
            pArgs = PyTuple_New(3);
            PyTuple_SetItem(pArgs, 0, PyUnicode_FromString("rect1"));
            PyTuple_SetItem(pArgs, 1, PyLong_FromLong(10)); 
            PyTuple_SetItem(pArgs, 2, PyLong_FromLong(5));

            // Create the instance of the class
            pInstance = PyObject_CallObject(pClass, pArgs);

            // If we successfully created the instance
            if (pInstance != NULL){

                // print out the instance
                PyObject* pStr = PyObject_Repr(pInstance);
                if (pStr != NULL) {
                    printf("[C++] Instance: %s\n\n", PyUnicode_AsUTF8(pStr));
                    Py_DECREF(pStr);
                }

                // print rectangle info from c++
                pAttrName = PyObject_GetAttrString(pInstance, "name");
                pAttrWidth = PyObject_GetAttrString(pInstance, "width");
                pAttrHeight = PyObject_GetAttrString(pInstance, "height");

                // make sure getting the info worked               
                if ((pAttrName != NULL && PyUnicode_Check(pAttrName)) 
                && (pAttrWidth != NULL && PyLong_Check(pAttrWidth)) 
                && (pAttrHeight != NULL && PyLong_Check(pAttrHeight))) {
                    Py_ssize_t size;
                    long width = PyLong_AsLong(pAttrWidth);
                    long height = PyLong_AsLong(pAttrHeight);
                    const char *name = PyUnicode_AsUTF8AndSize(pAttrName, &size);
                    printf("[C++] Rectangle Name:  %.*s\n", (int)size, name);
                    printf("[C++] Rectangle Width: %ld\n", width);
                    printf("[C++] Rectangle Height: %ld\n", height);
        
                    Py_DECREF(pAttrName);
                    Py_DECREF(pAttrWidth);
                    Py_DECREF(pAttrHeight);
                }
            
                // pValue is equal to what the area function returned 
                pValue = PyObject_CallMethod(pInstance, "area", NULL);

                if (pValue != NULL){
                    // if we actually have a pValue, print it out
                    printf("\n[C++] Returned area: %ld\n\n  ", PyLong_AsLong(pValue));
                }
            }
        }
    }

    // Clean up all of the variables we used
    Py_DECREF(pName);
    Py_DECREF(pModule);
    Py_DECREF(pDict);
    Py_DECREF(pClass);
    Py_DECREF(pArgs);
    Py_DECREF(pInstance);
    Py_DECREF(pValue);
    
    // close the interpreter
    if (Py_FinalizeEx() < 0) {
        return 120;
    }

    return 0;
}
