#Chinese wall Model

- addresses conflict of interest policies
- consultant knows sensitive info about company A and its competitor company B because it's consulting both of them
- insider trading
- same law firm working with defendant and prosecuter
- utility company operations people are not allowed to deal with energy markets

## Definitions

- Subjects: active entities
- Information:
	- objects: files individual items
	- dataset (DS): all objects that concern the same corporation
	- conflict of interest (CI) class: all data sets whose corporations are in competition
- Access rules -rules for read and write access

- Simple security Rule: 
	- subject S can read an object O only if O is in the same DS as object accessed by S
	- or O belongs to a CI from which S has not already accessed information
	- what you can access now is based on what you have had access to in the past
- * -property rule: A subject S can write to an object O only if:
	- S can read O according to the simple security rule
	- all objects that S can read are in the same DS as O
	- prevents indirect transferance of info through a shared object
	- alice and bob consult for competing companies A and B, they should not be able to read and write to company C b/c then info about A and B would pass through C between Alice an bob
