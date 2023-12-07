# Viruses

- malicious SW that replicates or copies itself onto other programs when executed
- Virus creators exploit sys vuln to infect and propagate virus

## Virus Parts
- Infection mech: how the virus moves from vpu to cpu
- Trigger condition: causes payload to be activated and delivered
- Payload: the activitiy of the virus/ the damage it does

## Virus operation
- Dormant Phase: waiting on trigger
- propagation: replicating to programs or disks
- triggering: By event to execute payload
- Execution: delivers or extracts payload

- details usially machine/' OS specific
	-exploits weaknesses of underlying platform
## Virus pseudocode

beginVirus:
If spread-condition begin:
	- for some set of target files do begin:
		if targetr is not infected then begin:
			- determin where to place virus
			- copu instructions from begin virus
			- alter tartget to execute new instructions
	if trigger pulled
		-perform some actions
	goto beginning of infected program
end virus

## Virus attachement:

- A Virus  can attach itseelf to a program or to dta by 
	- appending itself to the beggining or end of source code or assembly
		- so it is activated when prgm is run
	- Integrate itself into program, spread out code
		- harder to spot and cut out
		- compress original prgm so additon of virus does not change File sys
		- Integrate into data: executable text macro, scripting
- AN activated virus can do:
	- cause direct or immediate harm
	- Run as a memory resident program
	- replace or relocate boot sector programs, start at system startup
##Macro Viruses

- Macro code is attached to some data file
	- interpreted crather than compiled
	- platform independent
	- Mobile code
- interpreed by program using the file
	- word/ excel macrtos
	- esp using auto command and command macros
	- often automatically invoked
- blur distinction between data and prgm files making detection harder
- classic trade off ease of use vs sec

## Email Viruses
- Spread using email attachement condtaing macro
	- Melissa, lovebug
- Triggered when user opens or execures attachement
	- also when mail is used by scripting features in mail agent
	- usually targeted at microsoft outlook mail agent and word/ excel documents
## Basic precautions
- dont import untrusted programs!
- but viruses can be anywhere
- check crypto Sha-256 hashes from standard download sites. oof lots to do
- scans for viruses, install anti-virus software
	-virus scanners are only about 50% or less effective
	- need to update it regularly
## Signature scanning
- early viruses had charachteristic code patters:
	- just had to search for a database of patters
- can only be used for known signatures
- these were first gen virus scans
- malware evolved to avoid detection
- Polymorphic virus:
	- uses alternate but equiv code
	- gets around sig scanners
	- whale virus 32 varients
- Stealth virus:
	- actively tries to hide all signs of presance
	- a virus can intercept calls to read a file and retun correct values
	- Brain  Virus
- Encrypted virus
	-bulk of logic is kept encrypted
- Metamorphic virus:
	- mutates with every infection and is a complete re-write
## other virus scanners
- second gen:
	- use heuristics:
		-look for encryppt decrypt loops
		- integrioty checks to see changes
- Third gen:
	-track viruses by actions rather than code
	- ID notify and prevent anomalous behaviour
		- intallation of device driver after visiting website
- Fourth Gen:
	-schanning, access control/ whitelisting, behavioural analysis


















