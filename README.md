# Brightness Setting User Guide

Linux System:  
1. Download the package '''BrightnessControl''' to any user path.
2. Switch to the path (cd path);
3. Execute (sudo chmod 777 setup.sh);
4. Configure the startup environment and run (./setup.sh);
5. The user adjusts the brightness operation (python SetBrightness.py).

config.txt is the brightness saved every time the user runs SetBrightness.py to adjust the brightness script;
DefaultRun.py is the script that is executed by default at startup, and automatically calls the data in config;
SetBrightness.py is a script for the user to modify the brightness. The brightness is from 0-100, and less than or greater than 0 or 100 automatically;
setup.sh is a script that configures DefaultRun.py to start automatically. It only needs to be run once, check whether it is repeated, and give tips.



Download


1.	用户将文件包BrightnessControl拷贝到任意用户路径(path)；
2.	切换到该路径(cd path)；
3.	执行(sudo chmod 777 setup.sh)；
4.	配置开机自启环境，运行(./setup.sh)；
5.	用户调节亮度运行 (python SetBrightness.py)。

config.txt 		是用户每次运行SetBrightness.py调节亮度脚本保存的亮度；
DefaultRun.py 	是开机默认执行的脚本，自动调用config里的数据；
SetBrightness.py 	是用户修改亮度的脚本，亮度从0-100，小于或大于自动为0或100；
setup.sh			是配置DefaultRun.py开机自启的脚本，只需要运行一次，检查是否重复运行，并提给出提示。
