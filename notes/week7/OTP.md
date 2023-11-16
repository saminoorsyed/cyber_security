# One time passwords

- a password that can only be used once
- challenge response mechanism
- problems
	- synchronize user and system/server
	- Generartion of good rand passwords
	- password distribution
- motivation: reduce the window of opportunity for adversaries (sms text from banks/ Canvas log in)

## S/key
- one-time password scheme based on "Lamport"
- based on a one-way hash function (SHA-256 etc)
- User choses initial seed, k
- Server calculates h(k) = k1, h(k1)= k2, ..., h(kn) = kn+1
	- server needs to only save kn+1, not all the other parts of the chain
	- passwprds are the reverse order, p1 = kn, p2 = kn-1. etc pn = k1
Central Idea:
- next password is p', relaationship is h(p') = p.
- is one way, so knowing one password will not compromise previous paswords
- server computes hash of passwords until it matches the last password

HOTP:
- HMAC-based one-time password
- server and user establish a shared key at begining counter val C
Hotp(k,C) = truncate (HMAC-SHA-1(K,C) [31 bits]
- hotp pass = HOTP(k, C) mod 10^d wher d is the password length (usually  6-8)
- truncate extracts 31 bits. takes last 4 bits which represent a number, start at the bit at the indicated index number + 1. dynamic truncation
- counter is updated after every successful login

TOTP: time based onetime passaword

- pre established sahred secret
- Ct = floor[ (current unix time - time0)/time step
- T is current Unix time, time step defaults to every 30 seconds
- rest of algo is the same
- some times there are synchronization issues & network delays, will also check Ct+ or - 1 as well.
- counter value is calculated from time not chosen and shared
