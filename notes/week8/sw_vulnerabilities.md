# Common Software Vulnerabilities

- The open web aplication security project maintains a list of top 10 security risks Mobile and web lists
- CWE/Sans has a top 25 list from 2011 cwe.mitre.org

## Defensive programming

- need to consider a malicious actor, not just erros due to accidents
- often this conflicst with time to market
- Make no assumptions!!!
- most security attacks exploit implicit assumptions
- don't assume that users need more than 15 digits
- enforce that it is the input you weant
- don't assume that there will be enough disk space

- it is ok to make explicit assumptions, then enforce them

1. Program input (input checking)
2. Program Code (logic errors)
3. Interactions with OS and other programs: memory leaks, race conditions, envi variables
4. Program Output (output checking): cross site scripting

## Handling Input

- User  malicious or innocent directly impacts the prgm
	- always verify user input
	- whitelist expected results
- input can come from: Text entry, configuration files, Environment Variables, Network

## INJECTION ATTACKS
- Error in input handling tthat results in unexpected execution flow
	- Script writer expects user input to be data
	- User inputs text that will be interpreted as code
	- Scripting languages are particularly vulnerable (html etc)
	
- A few examples:
	- code injections (buffer overflows env variables)
	- command injections
	- SQL injections 

## Safer code

- COunter the attack by validating input
	- compare to pattern that rejects invalid input
	- Do not search for bad inputs, ensure patterns only accept valid inputs

## SQL Injection
- Widely exploited
- When input used in sql query to database is manipulated
	- SQL meta-chars are the concern
	- must check and validate the input

## Cross site scripting ( XSS) - input and output handling
- Goal - inject malicious code that is viewed by others
- HTML formatted user input stored
- Blog coments, Wiki entries with script
- injects code into others browsers which get rendered and a dif user might execute it

## Input checks
- Canonicalize input before performing checks
	- map the multiple versions of A to a particular value (Canonicalize it)
	- Issue for numeric values
		- is the number 16 bits or 32
		- signed or unsigned?
	- use good libraries: Java-> OWASP ESAPI toolkit + others

## Input Fuzzing
- can we test a program to find bad input processing?
- Generate "random" inputs to test programs
	- Environment variables
	- Input strings
	- network values
- could be completely random or structured
	- Minifuz
	- ShareFuzz
	- Spike
	- MuDynamics
- these are standard components of Microsofts dev lifecycle

# Volnurabilities from interacting with the operating system

## Correct Use of Memory
	- Memory leaks
		- Run our of memory DoS
		- Firefox: the more tabs open you run out of mory
		- if attacker knows this, could have server use up all mem
	- Free/ Allocation Errors
		- Heap overflow, can enable arbitrary execution
	- Could be solved by tools that track memory errors
		- Valgrind
		- Duma
	- Race Conditions and Shared memory:
		- multiple threads are not synchronized properly
		- Deadlocks
		- tough to ID because errors show up differently every time
		- Attackers could try to trigger latent threading errros
	- Environment Variables
		- another form of program input
		- should be validated and sanitized before use
		- example: Using PATH or IFS env var, 
			- cause script to execute attackers program
			- attacker now has privlidges of script
			- if SetUID is set to Root, then attacker now has root
		- Almost impossible to prevent especially using IFS
			- IFS is limited in most modern command shells
			- IFS defines what a delimeter in script
			- attacker adds = sign to delimeter, then 
			- PATH = 'filePath' is treated like a program with an argument
		- set path variables explicitly
		- Dynamic libraries are loaded at invocation time
		- Loader mus search the system to find the libraries needed by the executable
		- if attacker can modify Path variable, they can control what libraries
## Least Privilege
- Ideally run program with minimumn access required
- Root in Unix is not a great example of least priv
- Many Unix flavored distributions like Mac are getting rid of root
- web Servers and file access: previous attacks happened b/c web servers had too much
- if a prgm needs a special priv, how long does it need it? limit that time
	- once a prgm does what it needs to do, it drops it "capabilities"
	- divide prgm into diff parts with diff privilidges on dif processes

## System Calls and std Library functions

- Programs use System Calls and standard function for common operations
	- we make assumption about their operation
	- unexpected behavior may be a result of sytem optimizing to to share rss
		- buffering,, re-sequencing, modifying req
	- can conflic with prgm goals
## Secure File Shredder Example
- OS often does not wipe data, just drops pointer
- Allows forensic experts to  find this data
- Content must be over written
	- takes content patterns and over writes the whole file 
	- this does not actually clear data, bc it might be stored in the magnetic media
	- need to over write the data many many times
	- even this might not work b/c of system optomizations
		- might write all pattens, which never actually make it to the disk. still in buffer
	- the solution: write to file, flush application buffer (to kernel) sync kernle/ file system with device for each time you write a pattern
	- SSD - Driver/ file system might change the location of file to save the hardware
	- journaling system( file location moves every time)
	- even Apple could not make this promise

## Race Conditions
- OS mediates to avoid synch issues. files can be used to access OS RSS. if file exists, you cannot access, else no access. doesnt work because creating the log file is not atomic
- TOCTOU = Time of Check Time OF Use. when you check at a dif time than you use, causes race conditions

## Temporary Files
- Many programs create temp intermediate files
	- can create unique names based on Process id
	- if an adversary can guess the name of the temp file, and created a symbolic link between temp file and password file, so initial file overwrote password file on accident.

## Buffer Overflow
- " a condition at an interface underwhich more input can be placed into a buffer or data holding area than the capacity allocated, overwriting other info"
- used for exploitation:
	- inducing crashes
	- Taking control of a program
	- Also called Stack smashing
		Overflow when targeted buffer is located on the stack as a local var in stackFrame of a function. changing what the return address might be
		overwrite return address/ frame pointer to address of attack code in memory
C= each function call creates a stack frame, variable is initialized and space on stack is allocated. then stack pointer is moved


































