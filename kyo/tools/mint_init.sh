#!/bin/bash

err_exit() {
    echo $1
    exit $2
}


apt_config() {
    cat > /etc/apt/sources.list << EOF
deb http://mirrors.aliyun.com/ubuntu/ xenial main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ xenial-security main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ xenial-updates main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ xenial-proposed main restricted universe multiverse
deb http://mirrors.aliyun.com/ubuntu/ xenial-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ xenial main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-security main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-updates main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-proposed main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-backports main restricted universe multiverse
EOF
    apt update
}

lang_install() {
    sudo apt install language-pack-gnome-zh* language-pack-zh* -y
    # language-pack-gnome-zh-hans-base language-pack-zh-hans language-pack-zh-hans-base
    sudo apt install libreoffice-l10n-zh-cn libreoffice-help-zh-cn       \
                thunderbird thunderbird-locale-zh-hans              \
                thunderbird-locale-zh-cn thunderbird-gnome-support -y
}

fcitx_install() {
    sudo apt-get install fcitx fcitx-table-wbpy fcitx-ui-classic         \
                    fcitx-config-gtk fcitx-frontend-gtk3            \
                    fcitx-pinyin fcitx-sunpinyin fcitx-table-wubi   \
                    fonts-arphic-ukai fonts-arphic-uming -y

    sed -i 's/^run_im .*$/run_im fcitx/' ~/.xinputrc

    # fcitx-frontend-all
    # fcitx-frontend-fbterm
    # fcitx-frontend-gtk2
    # fcitx-frontend-qt4
    # fcitx-frontend-qt5
    # fcitx-libs-qt
    # fcitx-libs-qt5
    # fcitx-module-kimpanel
    # fcitx-module-lua
    # fcitx-tools
    # fcitx-ui-light
    # gir1.2-fcitx-1.0
}

soft_install() {
    sudo apt remove vim-common -y
    sudo apt install vim git tmux gcc libc6-dev libc6-i386 nfs-kernel-server  \
                chromium-browser mplayer openssh-server remmina* -y
    sudo apt install python3-pip -y
}

if test -z "$1" ; then
    # vim配置
    sudo mount 192.168.7.170:/kyo /mnt
    cp /mnt/tools/tmux.conf ~/.tmux.conf
    cp /mnt/tools/chromium-vim ~/ -rfapuv
    cp /mnt/tools/kyo_env/kyo_vim ~/kyoVim -rfapuv
else
    test $UID -eq 0 || err_exit "sudo运行..."
    # 源设置
    apt_config
    # 语言包
    lang_install
    # 输入法
    fcitx_install
    # nfs vim git ssh vnc tmux
    soft_install
fi

