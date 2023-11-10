# Mandatory Access control (MAC), Bell-laPadula (BLP) Model

- access decisions cannot be changed by normal users
- enforced by a system wide set of rules
- examples are SELinux, Windows Vista Integrity Levels
- believe that strong system security needs mac and ordinary users cannot be trusted

##Confidentiality Policy

- Goal is to prevent unauthorized disclosure of information
	- Deals with information flow
	- integrity/ other security principles supported are purely incidental
- Multi-level Security Models are best-known examples:
	- Bell-Lapadula Model (BPL) is basis for most of them

### Bell laPadula: basics
- Subjects and objects are all associated with a security level
- Security levels = basic security class
- the lebels are completely ordered: Top Secret> Secret> confidential> restricted> unclasified
- the subject's level is called a security clearance
- an object's security level is a classification level

- BLP: simple Security Property
	- you cannot read Up security levels
	- subject can only read its own class and below
- BLP: * -property
	- No write Down- prevents the accidental declassification of information
	- can only append (write-only) into an object of greater or equal security level
	- a subject can only read + write into an object of the same security level
- BLP: ds-property
	- discresionary security property
	- A mac system may also include a traditional discretionary access controll check
		- DAC in a MAC
	- if * -property and simple security propery checks pass *then* also check the discretionary access rules
### More Advanced security classes
- simple linear ordering not adequate
- add set of categories to the security level to create a security label:
	- top secret:{project1, project2} - a security label (a separate security class)
	- as clearance subject is cleared to top secret only for proj1 and proj2, not proj3
	- need to know
- set of security labels forms a partial ordering or a lattice
- use the phrase dominate for >= all labels must be greater
- can define clearance flexibility
	- principle and types of tranquility
		- Strong Traquility: the clearances of subjects and the classification of objects do not change ever
		- weak Tranquility: The clearances of subjects and the classification of the objects change in accordance with specified policy
	- raising an object security level: once available, no longer though. not great security
	- lowering object's security level: essentiall violates * - property


















