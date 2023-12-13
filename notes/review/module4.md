# User Authentication
1. Which of the folloing is user authentication?
- Establishing someone is who they claim to be and establishing identity

2. what is multi-factor authentication?
- user authenticating to an atm using a chip card and a pin

3. what is the processed form of information to verify identity stored at the server called?
- complementation information

4. what are the factors of authentication?
- who you are, what youknow, what you do, where you are (psuedo), what you have

5. Authintication is a critical step for Access control

# passwords 1

1. what are some advantages to password systems?
- Easier to replace or recover from lost password, less expensive/ no special hardware, easy to implement

2. what is Anderson's formula?
- P = (TG/N)
	- P = prob of guessing a password in a specified period of time, T.
	- G = number of guesses tested in the time unit
	- T = Time
	- N = Number of possible passwords
3. which password strategy is easier to remember and has high entropy?
- passphrases

4. what are some password vulnerabilities?
- password selection/strength, password storage, password sharing, social engineering/ pre-texting, trusted path/electronic monitoring, system design

# passwords 2
prevention of attacks: hide password file where attacker cant get to it (root)
			no remote access
1. How are passwords stored on the server?
- One-way hash functions of the passwords are stored in case the file is compromised, that way, the password is not compromised

2. what are the requirements of a bloom filter?
- Always catches a bad password + will sometimes label a good password as bad

3. what is a type1 dictionary attack?
- (Offline) An attacker gains access to the password file, knows functions and registered info, can repeatedly try different guesses to find a match

4. what is a type two dictionary attack?
- Have access to verification functions, try guesses until success

5. what is salting?
- randomly select one of many hash functions, store id of function along with password
- does not help for targetted accounts, but does work for untargeted attacks
- add 3 bits of salt to create 8 different hashes

# passwords 3

1. Down sides of using the same password on multiple sites?
- increases impact of comprimise if just one site is compromised

2. Downside of sharing passwords?
- Sharing passwords results in a loss of accountability

3. what are some solutions for password re-use?
- Single sign on, password manglers, password managers
