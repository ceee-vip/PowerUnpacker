
# Build Pack Command

```
#mac pack command
pyinstaller -D -w main_mac.spec

#windows pack command
pyinstaller -D -w main_windows.spec
```


# Debug
```shell script
macdeplotqt  main.app
otool -L main
otool -L libcocoa.dylib

```