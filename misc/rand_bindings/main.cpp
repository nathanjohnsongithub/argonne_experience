#include <Python.h>

int main(int argc, char *argv[])
{
    Py_Initialize();

    // Add the current directory to the Python module path so it can find my_python_class.py
    PyRun_SimpleString("import sys");
    PyRun_SimpleString("sys.path.append(\".\")");

    // Import the Python module
    PyObject* pName = PyUnicode_DecodeFSDefault("my_python_class");
    PyObject* pModule = PyImport_Import(pName);
    Py_DECREF(pName);

    if (pModule != NULL) {
        // Get the MyClass class from the module
        PyObject* pClass = PyObject_GetAttrString(pModule, "MyClass");

        if (pClass && PyCallable_Check(pClass)) {
            // Create an instance of the class
            PyObject* pArgs = Py_BuildValue("(i)", 5); // start value is 5
            PyObject* pInstance = PyObject_CallObject(pClass, pArgs);
            Py_DECREF(pArgs);

            if (pInstance != NULL) {
                // Call the increment method
                PyObject* pValue = PyObject_CallMethod(pInstance, "increment", NULL);

                if (pValue != NULL) {
                    printf("Returned value: %ld\n", PyLong_AsLong(pValue));
                    Py_DECREF(pValue);
                }
                Py_DECREF(pInstance);
            }
        }
        Py_XDECREF(pClass);
        Py_DECREF(pModule);
    }

    if (Py_FinalizeEx() < 0) {
        return 120;
    }
    return 0;
}
