

## Situational awareness


```powershell

// Basic User Enumeration 
whoami

// Seeing my ID
id

// Seeing my hostname
hostname

// looking at the IP config
ifconfig

// seeing the sudo permissions
sudo -l 

// enumerating the path
$PATH
echo $PATH

// Enumerating environment airabes
env 

// Seeing the OS version and name
uname -a


// so to chcek other stuff
cat /etc/os-release

// Enumerating CPU information
lscpu 

cat /etc/shells # seeing what login shells exists

// Checking defenses

- [Exec Shield](https://en.wikipedia.org/wiki/Exec_Shield)
- [iptables](https://linux.die.net/man/8/iptables)
- [AppArmor](https://apparmor.net/)
- [SELinux](https://www.redhat.com/en/topics/linux/what-is-selinux)
- [Fail2ban](https://github.com/fail2ban/fail2ban)
- [Snort](https://www.snort.org/faq/what-is-snort)
- [Uncomplicated Firewall (ufw)](https://wiki.ubuntu.com/UncomplicatedFirewall)



// this finds printers in the system
lsblk

// checking for mounted and unmounted drives
cat /etc/fstab

// checking the routing table
route 
netstate -rn

// checking DNS configuration
/etc/resolv.conf

// We'll also want to check the arp table to see what other hosts the target has been communicating with.
arp -a



// Existing Users
cat /etc/passwd
cat /etc/passwd | cut -f1 -d:
grep "*sh$" /etc/passwd

// Existing Groups
cat /etc/group



// We can then use the getent command to list members of any interesting groups
getent group sudo

// Mounted File Systems
df -h

// Unmounted File Systems
cat /etc/fstab | grep -v "#" | column -t


// All Hidden Files
find / -type f -name ".*" -exec ls -l {} \; 2>/dev/null | grep htb-student

// All Hidden Directories
find / -type d -name ".*" -ls 2>/dev/null

// Temporary Files
ls -l /tmp /var/tmp /dev/shm




```




check defenses

- Exec Shield
- iptables
- apparmor
- SELinux
- Fail2ban
- Snort
- Uncomplicated Firewall
- df -h 
	- this shows mounted file systems
- unmounted file systems
	- cat /etc/fstab | grep -v "#" | column -t
- find hidden files
	- `find / -type f -name ".*" -exec ls -l {} \; 2>/dev/null | grep htb-student`
- Find Hidden Directories
	- `find / -type d -name ".*" -ls 2>/dev/null`
- Temporary Files
	- `ls -l /tmp /var/tmp /dev/shm`
- 





# Internals

## Network

```powershell
// ------------------------------------------ Network Interfaces ------------------------------------------  //

// Checking IP stuff
ip a

// checking the hosts
cat /etc/hosts

// Checking users login
lastlog

// logged in Users, Might help us to see who else has been active on the system
w

// command history
history

// Finding history files
find / -type f \( -name *_hist -o -name *_history \) -exec ls -l {} \; 2>/dev/null

// cron
ls -la /etc/cron.daily/

// Proc
find /proc -name cmdline -exec cat {} \; 2>/dev/null | tr " " "\n"



// ------------------------------------------ Services  ------------------------------------------  //

// Installed Packages, this also shows us their version
apt list --installed | tr "/" " " | cut -d" " -f1,3 | sed 's/[0-9]://g' | tee -a installed_pkgs.list

// SUDO VERSION
sudo -V

// Binaries
ls -l /bin /usr/bin/ /usr/sbin/

// GTFOBins
for i in $(curl -s https://gtfobins.github.io/ | html2text | cut -d" " -f1 | sed '/^[[:space:]]*$/d');do if grep -q "$i" installed_pkgs.list;then echo "Check GTFO for: $i";fi;done

// Trace Systems calls
strace ping -c1 10.129.112.20

// Configuration Files
find / -type f \( -name *.conf -o -name *.config \) -exec ls -l {} \; 2>/dev/null

// Scripts
find / -type f -name "*.sh" 2>/dev/null | grep -v "src\|snap\|share"

// Running services By User
ps aux | grep root
ps aux 

```






# TDLR;


When taking backups its important to take note of credentials, shit like `.conf`, `.comfig`, `.xml`. the `/var` directory credentials may be useful for escalating to other users or even root, acessing databases and other systems within the environment /

`/var` is the web root for whatever web server is running on the host. it may contain database credentials or other types of creds that can be leveraged for further access something like MYSQL database creds within wordpress config files exists.


```powershell
// ----------------------------------- Credential Hunting  ----------------------------------- //
// Credential Hunting
cat wp-config.php | grep 'DB_USER\|DB_PASSWORD'

// Another credential hunting thing
find / ! -path "*/proc/*" -iname "*config*" -type f 2>/dev/null

// SSH keys, Check the known_hosts file. Finds potential lateral movement targets
ls ~/.ssh
```




