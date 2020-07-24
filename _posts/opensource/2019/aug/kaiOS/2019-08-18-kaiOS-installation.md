---
layout: post
title: "KaiOS - Installation "
excerpt: "Setting Up KaiOS"
modified: 2019-08-18T04:17:25-04:00
categories: kaios
tags: [kaios]

---


* Firefox WebIDE

  Install firefox v59 or older version from ftp
  * [v59 firfox](https://ftp.mozilla.org/pub/firefox/releases/59.0/linux-x86_64/en-US/)
  * [ftp](https://ftp.mozilla.org/pub/firefox/releases/)

* Install Make -

  * sudo apt-get install make

  * sudo apt-mark hold make

  * sudo dpkg --add-architecture i386

  * sudo dpkg --add-architecture amd64

  * sudo apt install --no-install-recommends autoconf2.13 bison bzip2 ccache curl flex gawk gcc g++ g++-multilib git lib32ncurses5-dev lib32z1-dev libgconf2-dev zlib1g:amd64 zlib1g-dev:amd64 zlib1g:i386 zlib1g-dev:i386 libgl1-mesa-dev libx11-dev make zip lzop libxml2-utils openjdk-8-jdk nodejs unzip python
  * ccache -M 10G

  * sudo apt install android-tools-adb android-tools-fastboot



* [Setting Up WebIDE](https://developer.mozilla.org/en-US/docs/Archive/WebIDE)

TODO - CI/CD

* [Gaia Build Setup](https://developer.mozilla.org/en-US/docs/Archive/B2G_OS/B2G_OS_build_prerequisites)
