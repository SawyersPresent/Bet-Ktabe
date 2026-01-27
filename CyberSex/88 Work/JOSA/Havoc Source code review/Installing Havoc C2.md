
```powershell
// Kali specific

// become root1 
sudo su

//cd into the opt folder 2 
cd /opt

//we clone our repository here 3 
git clone https://github.com/HavocFramework/Havoc.git

//we go into the havoc directory 4 
cd Havoc

// Download all necessary repos 5
sudo apt install -y git build-essential apt-utils cmake libfontconfig1 libglu1-mesa-dev libgtest-dev libspdlog-dev libboost-all-dev libncurses5-dev libgdbm-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev libbz2-dev mesa-common-dev qtbase5-dev qtchooser qt5-qmake qtbase5-dev-tools libqt5websockets5 libqt5websockets5-dev qtdeclarative5-dev golang-go qtbase5-dev libqt5websockets5-dev python3-dev libboost-all-dev mingw-w64 nasm libqt5sql5-sqlite

// we go into the teamserver direcetory 6 
cd teamserver

// we download the following necessary packages 7 
go mod download golang.org/x/sys

go mod download github.com/ugorji/go/codec 8

// we cd out the teamserver repo
cd ..

// run the following make commands, warning they are very CPU intensive, leave the commands to run. take a tea break maybe even a coffee break 9
make ts-build

make client-build

// after doing both and letting everything run. the havoc biary should be present, that same binary can be run as a client or as a server
./havoc server --default
./havoc client 


// the default credentials
5pider
password1234
```