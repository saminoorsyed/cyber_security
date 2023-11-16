# What are Authentication protocols

- communication protocols used for auth
	- typically involve the use of cryptographic primiatives/ methods
	- run on top of other network protocols
- Password Authentication protocol PAP
	- originally designed for point-to-point protocol (one of the oldest 1992)
	- weak or insecure - transmits password in tthe clear only used as a last resort
- Challenge Handshake Auth Protocol (CHAP)
	- also designed for point-to-point (PPP), obsoletes PAP
	- doesn't transmit passwords in the clear
	- requires password/secret to be available in the clear
- Extensible AUth protocol EAP
	- devel for point to point protocol, but widely used (WPA, WPA2)
	- general client server auth framework with 40+ specific methods
	- EAP passowrd, EAP-preshared keu, etc.
- Remote Authentication Dial-in User service (RADIUS)
	- centralized authentication, authorization and accounting for network service
	- when we log in to wifi, our info is sent to a backend RADIUS SERVER
	- application layer that runs on UDP
	- widely used by ISP for network access controll'
	- USES otther auth schemes, CHAP or EAP
	- updated by DIAMETER (diffrent protocol)
- Kerberos
	- centralized network auth service dev at MIT
	- based on the Needham-schroeder symmetric key protocol
	- windows 2000 and above use it + Unix flavors
- TACACAS, XTACACS< TACACAS+ CISCO
- SAML Security association markup lang
- OpenID

## PAP:

- user sends username and password to system, then systems checks what is storeds
- vulnerable to being caught on the wire

## CHAP:

- three way handshake
- Server sends Auth message with a challenge (unique random number)
- User responds with user name with Hash(Challenge, password).
- doesn't transmit password in the clear
- system  looks up username, calculates same challenge on stored pass and compares recieved hash
- if server is compromised, then passwords are compromised

## needham-schroder key exchange

- pre-cursor to kerberos
- more than simple auth protocol: establishes shared session keys
- solution to the following problem:
	- using chap, a group of n computers would need on the scale of n^2 keys to communicate with each other
	- not scalable
- leverages a third trusted party (ttp) that helps to establish a shared session key
- ttp manages one key for each user, and establishes a temporary shared key
- Notation:
	- {m}k sub A = encryption of m with K sub A where a is for alice.
- protocol:
	- Alice, requests a session with bob from Cathy
	- Cathy sends session key back to Alice encrypted with Alice's key
	- Cathy also sends the session key to Alice encrypted under bobs key
	- Alice sends the second message to Bob, who decodes it with his own key
	- Bob can extract the session key
- The Problem:
	- great for protection against passive adversaries who are only listening
	- not great for someone who drops and inserts a new message because they can get Bob's session key
	- Authentication is not provided
	- session keys are reused
	- if hacker cracked the key, they can get info and snoop communications
- Original protocol:
	- Alice sends message to Cathy in the open: Alice||Bob||R1 (random number 1)
		- knows it's not some sort of replay b/c of random number
	- Cathy sends {Alice||Bob||R1 {Alice||Ks}Kb}Ka
		- same message encrypted with Alices key, and inside it is a separate message encrypted with bob's key
		- Alice cannot understand it. it is cipher text
	- Alice sends cipher key to bob
	- bob decodes the message that has a session key with Alice
	- Bob sends Alice {R2}Ks
	- Alice sends {R2-1}Ks
		- last two numbers confirm that Alice is decrypting number because she has the session key
		- these are the authentication messages
		- R1 and R2 are called Nonces and should only be used once ever
- The flaw:
	- Bob cannot be sure that the ticket sent by Alice is not a replay of some other cracked previous message
- The fix:
	- two messges are added to the beginning
	- Alice asks bob to start a shared session
	- bob sends back a rndm number challenge, {A, R2}KB, encrypted with a his key that he shares with TTP
	- ALice now concatenates this with her original message to cathy
	- Cathy understands this and includes the R3 in the ticket she sends to Alice that will eventually go to bob
	- Alice sends the {Ks, R3, Alice}Ks to bob, who sees his random number
	- ALice never new R3
	- users have to keep track of random number challenge to make sure it's not a replay

	- other fixes:
		- use timestamps in Kerberos to fix replay problem
			- helps you to understand if it's fresh or not
			- all communicating entities must be synchonized
	
	















