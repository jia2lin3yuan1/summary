+ Add source to source list.
+ install upgrades: 
    ```
    sudo -s -- <<EOF
    apt-get update
    apt-get upgrade -y
    apt-get dist-upgrade -y
    apt-get autoremove -y
    apt-get autoclean -y
    EOF
    ```
+ Install vim: ```sudo apt-get install vim```. And install a fantastic vim configuration, like follow [my-vim-runtime](https://github.com/encorechow/my-vim-runtime/tree/master/.vim_runtime) from encorechow.
+ If using python, install virtualenv, virtualenvwrapper following [Install virtualenv and virtualenvwrapper on Ubuntu](http://exponential.io/blog/2015/02/10/install-virtualenv-and-virtualenvwrapper-on-ubuntu/)
+ Install visual studio code as editor.
+ If from China, install Sougou PInyin w.r.t. <https://blog.csdn.net/ljheee/article/details/52966456>
+ Install Git, a version management tool.
+ Install of TeamViewer, which is a great remote connecter.
+ Install of opencv (not for python):sudo apt-get install libopencv-dev 
+ Install Kompare, for comparing different files.
+ Install Kazam, for screen installing.
```
sudo apt-add-repository ppa:sylvain-pineau/kazam
sudo apt-get update
sudo apt-get install kazam 
```
