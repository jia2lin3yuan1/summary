In this note, it would record the problems I meet in my work and how to solve them.

## 2018-01-25
  + There is a public code in C++ programming, but I want to call function in it in python.
  + Using Cython to call C++ functions, and compile and build it into .so file. Then python could call the Cython function with import.
  + Related official website: <http://cython.readthedocs.io/en/latest/src/userguide/wrapping_CPlusPlus.html#c-left-values>, <https://docs.python.org/3/distutils/apiref.html>
  + There are few things should be noted:
    * The Cython file-name should be different from the C++ filename that the C++ function comes from. Otherwise, there is an error "multiple definition of ...". Because, in comling stage, it would generate a .c file of the .pyx file.
    * The generate .so file-name should be same as the .pyx file. Otherwise, there is the error 'dynamic module does not define init function'.
    * The version of Python calling the .so file should be same as the version of python generate it.
