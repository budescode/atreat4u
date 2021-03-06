<<<<<<< HEAD
#ifndef Py_ITEROBJECT_H
#define Py_ITEROBJECT_H
/* Iterators (the basic kind, over a sequence) */
#ifdef __cplusplus
extern "C" {
#endif

PyAPI_DATA(PyTypeObject) PySeqIter_Type;
PyAPI_DATA(PyTypeObject) PyCallIter_Type;
PyAPI_DATA(PyTypeObject) PyCmpWrapper_Type;

#define PySeqIter_Check(op) (Py_TYPE(op) == &PySeqIter_Type)

PyAPI_FUNC(PyObject *) PySeqIter_New(PyObject *);


#define PyCallIter_Check(op) (Py_TYPE(op) == &PyCallIter_Type)

PyAPI_FUNC(PyObject *) PyCallIter_New(PyObject *, PyObject *);

#ifdef __cplusplus
}
#endif
#endif /* !Py_ITEROBJECT_H */

=======
#ifndef Py_ITEROBJECT_H
#define Py_ITEROBJECT_H
/* Iterators (the basic kind, over a sequence) */
#ifdef __cplusplus
extern "C" {
#endif

PyAPI_DATA(PyTypeObject) PySeqIter_Type;
PyAPI_DATA(PyTypeObject) PyCallIter_Type;
PyAPI_DATA(PyTypeObject) PyCmpWrapper_Type;

#define PySeqIter_Check(op) (Py_TYPE(op) == &PySeqIter_Type)

PyAPI_FUNC(PyObject *) PySeqIter_New(PyObject *);


#define PyCallIter_Check(op) (Py_TYPE(op) == &PyCallIter_Type)

PyAPI_FUNC(PyObject *) PyCallIter_New(PyObject *, PyObject *);

#ifdef __cplusplus
}
#endif
#endif /* !Py_ITEROBJECT_H */

>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
