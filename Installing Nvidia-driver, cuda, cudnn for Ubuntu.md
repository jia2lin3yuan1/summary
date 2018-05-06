## Install Nvidia driver.
# Remove existing nvidia driver in the command-line mode.
+ Switch to the command-line mode with <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>F1</kbd>, and stop the service lightdm.
```
service lightdm stop  # if it doesn't work, try:  sudo /etc/init.d/lightdm stop.
```
