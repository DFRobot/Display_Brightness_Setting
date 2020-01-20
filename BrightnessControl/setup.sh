#!/bin/bash
script_abs=$(readlink -f "$0")
script_dir=$(dirname $script_abs)
data=${script_dir}"/DefaultRun.py "
data=${data}$script_dir
data=${data}"\""
data1="su "
data1=${data1}$USER
data1=${data1}" -c \"python "
data1=${data1}$data
#data1=  su pi -c "python /home/pi/Desktop/pwm.py /home/pi/Desktop"
grep -q "$data1" /etc/rc.local
if [ $? -eq 0 ]
then 
    echo "This configuration already exists!"
else
    sudo sed -e '/fi/a\'"$data1" -i /etc/rc.local
    sudo sed -e '/fi/a\sleep 6' -i /etc/rc.local
    echo "Configuration succeeded!"
    exit 0
fi










