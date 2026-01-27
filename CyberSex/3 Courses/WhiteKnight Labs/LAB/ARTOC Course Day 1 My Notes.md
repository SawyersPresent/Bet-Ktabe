

operator machines are multiple




create a user using IAM and get their access key

https://us-east-1.console.aws.amazon.com/iam/home?region=eu-north-1#/users/details/Sawyer/create-access-key


```
PS D:\ARTOC\ARTOC Lab Deployment\ARTOC-Client-Machines-v1.4\ARTOC-Client-Machines-v1.4> aws configure --profile wkl
AWS Access Key ID [None]: <REDACTED>
AWS Secret Access Key [None]: <REDACTED>
Default region name [None]:
Default output format [None]:
```



```
PS D:\ARTOC\ARTOC Lab Deployment\ARTOC-Client-Machines-v1.4\ARTOC-Client-Machines-v1.4> .\build.bat

D:\ARTOC\ARTOC Lab Deployment\ARTOC-Client-Machines-v1.4\ARTOC-Client-Machines-v1.4>terraform init
Initializing the backend...
Initializing provider plugins...
- Finding latest version of hashicorp/random...
- Finding latest version of hashicorp/local...
- Finding latest version of hashicorp/aws...
- Finding latest version of hashicorp/tls...
- Installing hashicorp/random v3.7.1...
- Installed hashicorp/random v3.7.1 (signed by HashiCorp)
- Installing hashicorp/local v2.5.2...
- Installed hashicorp/local v2.5.2 (signed by HashiCorp)
- Installing hashicorp/aws v5.95.0...
- Installed hashicorp/aws v5.95.0 (signed by HashiCorp)
- Installing hashicorp/tls v4.0.6...
- Installed hashicorp/tls v4.0.6 (signed by HashiCorp)
Terraform has created a lock file .terraform.lock.hcl to record the provider
selections it made above. Include this file in your version control repository
so that Terraform can guarantee to make the same selections by default when
you run "terraform init" in the future.

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.
```



if you lose the terminal output

go back to the folder where the labs where deployed and then run terraform output to get back said values


for SAWYER ONLY

```
Guacamole-Login-Password = "qmbZv880oY31bn9C"
Guacamole-Login-Username = "admin"
Guacamole-Server-HTTPS-Address = "https://54.149.137.251/guacamole/"
Ubuntu-Redirector-Server-IP = "100.20.200.14"
```




tailsacle -> teamserver 




## Traffic relay & redirection


how to setup your c2 redirector and harden it in the next lab

redirector vs relay

- rediretor
	- takes traffic from somewhere and send it somewhere else
	- redirector is a server and uses a domain to conceal itself
- relay
	- a CDN, such as Azure front door or AWS lambda/cloudfront, ms dev tunnels
	- something not related to your domain directly
	- usually buy a domain for your RTO
		- aged atleast 90 days
		- next gen firewalls check for this
	- a relay bypasses that because CDNs are created always all the time
- relay is CDN can be spanned whenever


## HTTPs redirector

namecheap

GDPR will protect you from leaking information about the traffic and etc. 

check the categorizations of the target



for cloudfare

turn off proxy from cloudflare

have the A record point to the redirector, have the proxy be DNS only

APT's use zeroSSL

provider would be njalla


you can host multiple VHOST on 1 apache server, so you can have your entire offensive infra pointing to the same infrastructure

use diffrent domains for each purpose for the server



alot of filtering, header filtering, geolocation filtering, remove as much attack attribution as possible


modifying the files to move into the c2


server-setup.sh & domain-setup.sh


long haul is usually 30 minutes - 1 hours
short haul usually  15 minutes


```
curl https://twodollahsandabeers.org/jquery/user/preferences/aasd -A 'cheeseburger' -H 'Access-X-Control: asda'
```

