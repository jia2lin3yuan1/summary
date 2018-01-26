In this note, it would record the problems I meet in my work and how to solve them.

## 2018-01-25, Using Cython to connect C/C++ source code to python api.
  + There is a public code in C++ programming, but I want to call function in it in python.
  + Using Cython to call C++ functions, and compile and build it into .so file. Then python could call the Cython function with import.
  + Related official website: <http://cython.readthedocs.io/en/latest/src/userguide/wrapping_CPlusPlus.html#c-left-values>, <https://docs.python.org/3/distutils/apiref.html>
  + There are few things should be noted:
    * The Cython file-name should be different from the C++ filename that the C++ function comes from. Otherwise, there is an error "multiple definition of ...". Because, in comling stage, it would generate a .c file of the .pyx file.
    * The generate .so file-name should be same as the .pyx file. Otherwise, there is the error 'dynamic module does not define init function'.
    * The version of Python calling the .so file should be same as the version of python generate it.
    
  + connect C/C++ array with numpy array in python:
    * Mtd 1: In Cython and Python, claim the numpy array ordered in 'C' alignment.
     '''
        in C: void c_func(float *arr);
        
        in Cython: using np.ndarray(type, ndim, mode='c').
        cdef extern from '***.c' (or '***.h')
            void c_func(float *arr)
        def py_func(np.numpy(float, ndim=1, mode='c') arr not None):
            c_func(arr)
            
        in Python: np.array([size], dtype, order='c')
        from cython_so_fname import py_func
        def myfunc_test():
            arr = np.zeros(10, dtype=np.float32, order='c'
            py_func(arr)
            
     '''
