# Exploration: BIBA integrity model

proposed by Kennit J. biba in 1970s and is a MAC manditory integrity model

focuses on Integrity

## Intuition for integrity levels

- the higher the level the more confidence: program will execute or data is reliable or accurate
- relationship between integrity levels and trustworthiness
- integrity levels are not security levels, just about trustworthiness
- useful in modern operating systems in addition to military
	- how much do we trust our software to perform/ not have bugs etc.

### Strict integrety policy

- simple integrity property: S such that S can write to O, only if i(o) <= i(s)
	- this preserves the integrity of O so that unreliable subjects do not inject unreliable data
	- No write up
- Integrity Confinement Property
	- S can read o if and only if i(s)<= i(o)
	- no read down
- invocation Property
	- S1 can invoke S2 if and only if i(s2)<=i(s1)
	- lower integrity processes cannot invoke higher integrity processes
- Dual of Bell-Lapadula model
	- can add categories to get discressionary control to get full dual of Bell-lapadula
### more advance integrity
- add set of categories to the integrity leve to create integrity label
	- Trusted: {proj1, proj2}
	- info in object is trusted only for project 1 and project 2
- same comparison as security labels, must dominate in all categories to be comparable
- simple integrity: subject s can write to an object o if and only if Label(s) dominates label(o)
- integrity confinement: a subject S can read an object o only if the label(o) dominates label(S)
- invocation property: s1 can only invoke s2 if and only if label(s1) dominates label(s2)

### models in practice

- Integrity levels introduce in windows vista as madatory integrity control
- in windows 4, 4 integrity levels: low < medium < high < system
	- standard users have medim integrity
	- System services have system integrity
	- objects with no level have medium integrity
	- anything downloaded from the internet automatically has low integrity
	- this prevents corruption of system files





