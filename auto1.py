#import Library
import paramiko
import time
import sys

#perintah try except
#perintah try
try:
#variabel ip (untuk ip yang diremote), username (untuk masuk ssh), password (password ssh)
    ip_address = ("192.168.122.230")
    username = ("admin")
    password = ("")

#perintah untuk melakukan koneksi ssh client ke mikrotik
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=ip_address,username=username,password=password)

#keterangan jika login ssh sukses
    print (f"sukses login to {ip_address}")

#perintah di mikrotik yang dibuat automation
    ssh_client.exec_command("/system identity set name=very")
    ssh_client.exec_command("/tool romon set enabled=yes secrets=very")
    ssh_client.exec_command("/ip dhcp-client add dhcp-options=hostname,clientid disabled=no interface=ether1")
    ssh_client.exec_command("/ip address add address=192.168.1.1/24 interface=ether2 network=192.168.1.0")
    ssh_client.exec_command("/ip dhcp-server network add address=192.168.1.0/24 gateway=192.168.1.1")
    ssh_client.exec_command("/ip pool add name=dhcp_pool0 ranges=192.168.1.2-192.168.1.254")
    ssh_client.exec_command("/ip dhcp-server add address-pool=dhcp_pool0 disabled=no interface=ether2 name=dhcp1")
    ssh_client.exec_command("/ip service disable telnet,ftp,www,api-ssl")
    ssh_client.exec_command("/ip firewall nat add chain=srcnat out-interface=ether1 action=masquerade")
    ssh_client.exec_command("/user set admin name=very password=123456")


#keterangan kalau konfigurasi berhasil (optional)
    print (f"Konfigurasi Router dengan ip address {ip_address} berhasil")

#memberikan waktu selama 2 detik sehingga setelah dieksekusi kita bisa melihat reportnya
    time.sleep(2)
    sys.exit()

#perintah except
except KeyboardInterrupt:
    print ("\n Exit \n")
    sys.exit()
