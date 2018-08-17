#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("wget --no-check-certificate https://github.com/teddysun/across/raw/master/bbr.sh")
os.system("chmod +x bbr.sh")
os.system("./bbr.sh")

f = open('/etc/sysctl.conf', 'a')
f.write(
"\nfs.file-max = 51200"
"\nnet.core.rmem_max = 67108864"
"\nnet.core.wmem_max = 67108864"
"\nnet.core.netdev_max_backlog = 250000"
"\nnet.core.somaxconn = 4096"
"\nnet.ipv4.tcp_syncookies = 1"
"\nnet.ipv4.tcp_tw_reuse = 1"
"\nnet.ipv4.tcp_tw_recycle = 0"
"\nnet.ipv4.tcp_fin_timeout = 30"
"\nnet.ipv4.tcp_keepalive_time = 1200"
"\nnet.ipv4.ip_local_port_range = 10000 65000"
"\nnet.ipv4.tcp_max_syn_backlog = 8192"
"\nnet.ipv4.tcp_max_tw_buckets = 5000"
"\nnet.ipv4.tcp_fastopen = 3"
"\nnet.ipv4.tcp_mem = 25600 51200 102400"
"\nnet.ipv4.tcp_rmem = 4096 87380 67108864"
"\nnet.ipv4.tcp_wmem = 4096 65536 67108864"
"\nnet.ipv4.tcp_mtu_probing = 1")
f.close()

os.system("sysctl -p")

f = open('/etc/security/limits.conf', 'a')
f.write(
"\n* soft nofile 51200"
"\n* hard nofile 51200")
f.close()


f = open('/etc/pam.d/common-session', 'a')
f.write(
"\nsession required pam_limits.so")
f.close()

f = open('/etc/profile', 'a')
f.write(
"\nulimit -n 51200")
f.close()

os.system("ulimit -n 51200")

os.system("/etc/init.d/shadowsocks restart")
