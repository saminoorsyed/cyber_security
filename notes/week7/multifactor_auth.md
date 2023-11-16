# Multifactor Identifacation

- using multiple elements to prove Identity
Factors of Identification:
	- what an entity knows(passwords, private key)
	- what an entity has ( badge, smart card)
	- what an entity is (fingerprints, retinal scans)
	- what an entity does (handwriting, voice pattern, type rhythm)
	- Where an entity is (in front of a particular terminal) this one is considered psuedo factor
Example: chip and Pin Credit card transactions
	- in europe cc with chip needs a pin as well

- Provides additional protection when one factor is not sufficient
- number of factors should be commensurate with value of protected asset
- password + SMS = dual authentication
	- insufficient for very high value targets
	- cloned sim cards
- two factor auth is the norm, because pasword auth is vulnerable
	- b/c everyone has a second device it is now feasible
	- usually a password and something else
	- hardware dongle, authenticator software
	- bofa used to have a site key to let users know that they were at the right website
		before logging in. same image picked during account creation.
		flawed bc all a hacker had to do was guess a user name to see site key.
		but this process still increased cost to do attack b/c making individualized website is 
		more expensive. secondary benefit of being able to pursue hackers who enter passwords
		other peoples accounts

