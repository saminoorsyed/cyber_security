# What is Cyber security

1. Which of the following actions fall under computer security?
	- Guarding computer against malware
	- protect your tax return files with passwords
	- locking your phone screen so it can only open with a pin or password
2. why is security hard?
	- users can make mistakes in configuring their systems or not use difficult mechanisms
	- More often than not security is added to the system later and not designed in from the beggining
	- attackers have to find just one weakness where defenders have to plug all defenses
	- Systems, environment, attackers are constantly changing and evolving
3. categories of adversaries in order of increasing capability
	- prying family/ friends
	- Mischief makers (script kiddies)
	- Hackers
	- Hacktivists
	- Organized crime
	- Nation states
# Key Concepts of Cyber Security
what cyber security issues are we dealing with?
	- Confidentiality: unauthorized disclosure of sensitive data
	- Privacy: preventing unauthorized acces or disclosuer of data about people (cc numbers, ssn etc)
	- Integrity: unauthorised modification- computer running unauthorised malware is performing actions as if it were the owner of the computer
	- Accountability: the actions of an entity are not traceable to a unique entity
	- Availability: self explanitory
1. Bob in accounting accidentally sends company balance sheet to the company mailing list instead of an individual
	- Confidentiality
2. Ellen clicked on the link her friend posted on Fb that promised cute dancing banies. now her computer is running slower and her friends are complaining about the adds being sent from her account
	- Integrity
3. cyber security experts cant track who sent the link that loaded malware onto ellen's computer
	- Accountability
4. Canvas is unresponsive as David tries to submit his homework at 11:58pm
	- Availability
5. David bought a copy of a well-known tax preparation software as a dvd from a local store. it turned out to have stolen his tax data
	- Privacy- personal information
	- Confidentiality- company information
	- Authenticity
# Terminology
1. Asset: something of value data, hardware, network, service etc
2. threat: set of circumstances that has the potential to breach security and cause harm
	- snooping
	- Falsification
	- masquerading/ spoofing
	- repudiation - false denial of receiving info or taking an action
3. threat levels:
	- low impact = loss of time/ productivity
	- moderat impact = sever adverse affect, loss of revenue and capability
	- high impact = severe or catastrophic
4. Adversary
5. Vulnerability
6. Attack
7. Controls and counter measures: storing sensitive data  on the database/ encrypting it + independent data backup
8. Surface: Reachable exploitable vulnerabilities: network, software, humans

#Cyber security strategy

- Specification/policy
	- what does it mean to be secured?
	- a statement of what is and what is not allowed
	- divides the world into secure and non-secure states
	- a secure system starts in a secure state
	- considerations of security vs ease of use, cost/ return on investment

	- Is this secure: web server accepts all connections, self registration,connected to the internet. this is a secure state depending on the context and purpose of the server

- implementation/ Mechanism
	- how to enforce a sepcified security policy?
	- prevention (encryption of data)
	- Detection (crypto hashes)
	- response (locking out after x attempts)
	- recovery (backing up with remote databse)
- Correctness/ Assurance
	- does the security system work as expected/ advertised?
	- collect evidence: specifications, design, implementation
	- how much trust can we place in the system
	
- Incentives
	- are the right incentives in place for creating right policy, mechs adn using them

# Cyber security principles

Every access must be checked by a monitor - complete mediation
in the event of a failure, block access to rss - fail-safe (fail-close)
give users only permissions needed- least privilege
security of system should not depent on being confidential - open design
for sensitive tasks divide permissions- separation of privileges
