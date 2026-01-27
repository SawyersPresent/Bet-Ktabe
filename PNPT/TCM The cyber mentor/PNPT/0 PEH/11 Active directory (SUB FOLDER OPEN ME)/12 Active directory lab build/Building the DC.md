Password is

```
P@$$w0rd!
```


change name


start menu -> view your PC name -> rename this pc -> HYDRA-DC


server management dashboard


manage -> add roles and fetures -> in server roles pic `Active Directory Domain Services` -> Next until you reach the confirmation, click the restart check and then press install




## Deployment configuration

add a new forest, call it marvel.local -> enter password on next page as `P@$w0rd!` -> hit next all the way untill installation



## More features

do the same steps for ADDS and then click on the funny blue text near the end to configure the ADCS


next -> Role service pick `Certificate authority` -> next ->next -> private key, create new one use SHA256 -> next on everything and install


pimpmyadlab

```
DisplayName   : Disable Defender                                                                                        GpoId         : 5fa4be7e-fe3f-478d-8fba-56735eaa945f                                                                    Enabled       : True                                                                                                    Enforced      : True                                                                                                    Order         : 1                                                                                                       Target        : DC=MARVEL,DC=local                                                                                      GpoDomainName : MARVEL.local                                                                                                                                                                                                                                                                                                                                              [++] Removing and unlinking Default Domain Policy                                                                     
  [++] Installed Sharphound.exe to C:\TCM-Academy\Sharphound


  [++] Disabling Ethernet0 Power Management

  [++] Setting Ethernet0 DNS to 127.0.0.1


  [++] Setting Ipv6 DNS to DHCP


 Script Run 3 of 3 - We are all done! Rebooting one last time! o7 Happy Hacking!


 Write this down! We need this in the Workstation Configuration... Domain Controller IP Address: 192.168.244.250
```