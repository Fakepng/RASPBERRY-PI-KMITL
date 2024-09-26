#/usr/bin/sh

pinctrl set 14 op

while :
do
    pinctrl set 14 dl
    sleep .1
    pinctrl set 14 dh
    sleep .1
done
