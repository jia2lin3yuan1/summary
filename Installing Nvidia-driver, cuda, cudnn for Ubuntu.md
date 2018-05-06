## Install Nvidia driver.
  The summary is based on two blogs [How to fix NVIDIA driver failure on Ubuntu](https://codeyarns.com/2013/02/07/how-to-fix-nvidia-driver-failure-on-ubuntu/) and [Install NVIDIA Driver and CUDA](https://gist.github.com/zhanwenchen/e520767a409325d9961072f666815bb8).
  
+ Switch to the command-line mode with <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>F1</kbd> | ... | <kbd>F6</kbd>, and stop the service lightdm.
```
service lightdm stop  # if it doesn't work, try:  sudo /etc/init.d/lightdm stop.
```
  * Remove existing NVIDIA drivers in the command-line mode.
    - Purge, not just remove, all installed NVIDIA packages.
      ```
      sudo apt-get purge nvidia-*
      ```
    - There may still have some NVIDIA modules stuck in the kernel. List the kernel modules by:
      ```
      dkms status
      ```
      You may get output of this form:
      ```
      nvidia, 390.48, 1.3.0-48-generic, x86_64: installed
      ```
      Here nvidia is the module name, 390.48 is the module version and 1.3.0-48-generic is the kernel version.
    - Remove all the nvidia modeules. For example, to remove the abover:
      ```
      sudo dkms remove nvidia/390/48 -k 1.3.0-48-generic
      ```

  *  Install NVIDIA drivers.
    - Now install back the drivers. I highly recommend staying away from the drivers on NVIDIA’s website. For drivers that have been tested and packaged by Ubuntu volunteers, there are two options: current and current-updates.
    
    - current is what was well tested and shipped with the Ubuntu version you are using. It may be pretty old. current-updates is a package that is drawn from NVIDIA’s releases, but is tested and packaged by Ubuntu. This is pretty safe.
    
    - Depending on what you pick, the install is:
      ```
      sudo apt-get install nvidia-current-updates nvidia-settings-updates
      ```
