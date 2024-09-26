#/usr/bin/sh

pinctrl set 17 op

while :
do
    pinctrl set 17 dl
    sleep .1
    pinctrl set 17 dh
    sleep .1
done
