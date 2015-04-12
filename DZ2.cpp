//
//  DZ2.cpp
//  
//
//  Created by Антон Крючков on 09.04.15.
//
//

#include <stdio.h>
#include <vector>

extern "C" {
#include <Python.h>
}

using namespace std;

static PyObject * DZ2(PyObject *module, PyObject *args) {

    PyObject *mat = PyTuple_GetItem(args, 0);
    int num = PyObject_Length(mat);
    vector<vector<double>> d(num, vector<double>(num));
    
    for (int i = 0; i < num; i++) {
        PyObject *st = PyList_GetItem(mat,i);
        for (int j = 0; j < num; j++) {
            d[i][j] = PyFloat_AsDouble(PyList_GetItem(st,j));
        }
    }
    
    for (int k = 0; k < num; k++) {
        for (int i = 0; i < num; i++) {
            for (int j = 0; j < num; j++) {
                d[i][j] = 1.0 / (1.0 / d[i][j] + 1.0 / (d[i][k] + d[k][j]) );
            }
        }
    }
    
    PyObject *ans = PyList_New(num);
    
    for (int i = 0; i < num; i++) {
        PyObject *st = PyList_New(num);
        PyList_SetItem(ans,i,st);
        for (int j = 0; j < num; j++) {
            PyObject *zn = PyFloat_FromDouble(d[i][j]);
            PyList_SetItem(st,j,zn);
        }
    }
    return ans;
}

PyMODINIT_FUNC PyInit_DZ2()
{
    static PyMethodDef ModuleMethods[] = {
        { "DZ2", DZ2, METH_VARARGS, "С++ module of Floyd algorithm." },
        { NULL, NULL, 0, NULL }
    };
    
    static PyModuleDef ModuleDef = {
        PyModuleDef_HEAD_INIT,
        "DZ2",
        "fast method",
        -1, ModuleMethods,
        NULL, NULL, NULL, NULL
    };
    PyObject *module = PyModule_Create(&ModuleDef);
    return module;
}