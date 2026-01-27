
# Theory

`Resource-based constrained delegation` (`RBCD`) was introduced with Windows Server 2012. This type of delegation allows delegation settings to be configured on the target service instead of the service account being used to access resources.

RBCD relies on security descriptors instead of an allowed list of SPNs. An administrator defines which security principals can request Kerberos tickets for a user. When a service receives a request to grant access on behalf of another user, the KDC checks against the [security descriptors](https://learn.microsoft.com/en-us/windows/win32/secauthz/security-descriptors) in the `msDS-AllowedToActOnBehalfOfOtherIdentity` attribute of the principal running the backend service.

If the security descriptor of the backend service matches that of the frontend service, then access will be granted. RBCD works regardless of the domain functional level but does require at least one Domain Controller running Windows Server 2012 or later in the same domain as both the backend and frontend servers.











# Exploit



## Windows




## Linux




