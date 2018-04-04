#!/bin/bash

err_exit() {
    echo $1
    exit $2
}


test $UID -eq 0 || err_exit "请使用sudo运行!"

read -p "请输入100-200之间的数字(全班不能重复): " num

cd ~

cat > /etc/network/interfaces << EOF
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).

source /etc/network/interfaces.d/*

# The loopback network interface
auto lo
iface lo inet loopback

auto enp2s0
iface enp2s0 inet dhcp

auto enp2s0:0
iface enp2s0:0 inet static
address 3.3.3.$num
netmask 255.255.255.0
EOF

ifdown enp2s0
ifup enp2s0
service networking restart

ping -c 1 3.3.3.3 &> /dev/null || err_exit "网络配置有误, 请重启电脑!"

test -e kyo_env.tar && rm kyo_env.tar -f
test -e kyo_env && rm kyo_env -rf
wget http://3.3.3.3:81/tools/kyo_env.tar
tar -xf kyo_env.tar
cd kyo_env
./install.sh
