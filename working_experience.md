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
     _ in C: 
     ```c++
        void c_func(float *arr);
     ```
     _ in Cython: using np.ndarray(type, ndim, mode='c').
     ```cython
        import numpy as np
        cimport numpy as np
        cdef extern from '***.c' (or '***.h')
            void c_func(float *arr)
        def py_func(np.numpy(float, ndim=1, mode='c') arr not None):
            c_func(arr)
     ```    
     _ in Python: np.array([size], dtype, order='c')
     ```python
        import numpy as np
        from cython_so_fname import py_func
        def myfunc_test():
            arr = np.zeros(10, dtype=np.float32, order='c')
            py_func(arr)
     ```
    * Mtd 2: In Cython, claim ```np.import_array()```
     _ in Cython:
     ```cython
        import numpy as np
        cimport numpy as np
        np.import_array()
        cdef extern from '***.c' (or '***.h')
            void c_func(float *arr)
        def py_func(arr):
            c_func(arr)
     ```    
     _ in Python:
     ```python
        import numpy as np
        from cython_so_fname import py_func
        def myfunc_test():
            arr = np.zeros(10, dtype=np.float32)
            py_func(arr) 
     ```
     * Mtd 3: using Vector in C/C++, array in Python to send data.
     _ in C: 
     ```c++
        #include<vector>
        void c_func(vector<float> arr);
     ```
     _ in Cython: using np.ndarray(type, ndim, mode='c').
     ```cython
        cdef extern from '***.c' (or '***.h')
            void c_func(vector<float> arr)
        def py_func(arr):
            c_func(arr)
     ```    
     _ in Python: np.array([size], dtype, order='c')
     ```python
        import numpy as np
        from cython_so_fname import py_func
        def myfunc_test():
            arr = np.zeros(10, dtype=np.float32)
            py_func(arr)
     ```
  + cimport and import <http://blog.yclin.me/gsoc/2016/06/08/difference-between-float64-and-float64_t/>
  
  
## 20180204, C++ programming
  + sort a std::vector, and return index .
  ```c++
  vector<int> arg_sort(vertex<int> v){
    // initialize original index locations
    vector<size_t> idx(v.size());
    iota(idx.begin(), idx.end(), 0);

    // sort indexes based on comparing values in v
    sort(idx.begin(), idx.end(), [&v](size_t i1, size_t i2) {return v[i1] < v[i2];});
         
    return idx;
       
  }

  ```
## 20180423, 装机Note (Ubuntu)
  + Install Nvidia Driver, then Cuda, then cudnn.
  <https://gist.github.com/wangruohui/df039f0dc434d6486f5d4d098aa52d07>
  <https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html>
  <https://docs.nvidia.com/deeplearning/sdk/cudnn-install/index.html#installdriver>
  + Install Sougou PInyin
  <https://xunyunliu.github.io/post/install_sogou/>

