![[0 Theory-20260126041647736.webp|706]]


- External
	- A non-transitive trust between two specific domains in separate forests that are not connected by a forest trust. This trust applies only to the two domains involved and does not extend to any other domains in either forest. It uses SID filtering for security, and because it is non-transitive, users from the trusted domain can access resources in the trusting domain only if explicitly permitted, while users from other domains in the trusted forest cannot authenticate into the trusting forest by default. 
		- For example, if `corpA.local` creates an external trust with `partnerB.local`, users from `partnerB.local` can be granted access to a file server in `corpA.local`, but users from any other domain in `partnerB`’s forest (such as `dev.partnerB.local`) will not have access unless a separate trust is explicitly configured
- Forest
	- A transitive trust between two forest root domains, meaning that any user residing in the trusted forest can authenticate to any domain residing in the trusting forest\
- SID-Filtering




references:
https://blog.harmj0y.net/redteaming/a-guide-to-attacking-domain-trusts/
https://posts.specterops.io/not-a-security-boundary-breaking-forest-trusts-cd125829518d
https://dirkjanm.io/active-directory-forest-trusts-part-one-how-does-sid-filtering-work/




