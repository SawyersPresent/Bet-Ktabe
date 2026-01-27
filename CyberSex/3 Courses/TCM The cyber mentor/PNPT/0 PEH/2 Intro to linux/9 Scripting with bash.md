
## Building a ping sweeper device




```bash
#!/bin/bash
if [ "$1" == "" ]
then
echo "You forgot an IP address!"
echo "Syntax: ./ipsweep.sh 192.168.1"

else
for ip in `seq 1 254`; do
ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &
done
fi
```


Doing more inline automation

`for ip in $(cat ips.txt); do nmap $ip; done`

while this may differ in the shell you use, i use fish so for me the script would look like this

`for ip in (cat ips.txt); nmap $ip; end`