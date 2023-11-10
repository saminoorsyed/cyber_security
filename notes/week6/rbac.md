# Week 6 Exploration- Intro to Role Based access Control (RBAC)

- most widely used access control model, was introduced in 90s

- gives access to entities based on roles that represent competency, authority and responsibility
- Roles can have permissions updated
- users can have multiple roles
- reduces AC overhead when dealing with transitioning roles/ associations

- can use an access Matrix Representation for roles ACf and assignment of users to roles

in DAC, permissions are assigned directly to users-> groups. in RBAC, permissions are assigned to users->roles
###difference between groups and roles?
- Group: simply a collection of users, 
    - allows users to grant access to object he owns
    - user-role assignment is more fine tuned, but change much more often
- Role: Collection of permissions, and possibly other roles for a specific job function or association relationship.
    - typically users cannot pass on rights to others
    - Role-based permissions change less often than individuals might	

#Exploration: RBAC Models

four different models introduced [SCFY96]:
1. RBAC0
    - Min functionality
2. RBAC1
    - RBAC0 + Role Hierarchies
3. RBAC2
    - RBAC0 + Constraints
4. RBAC3
    - RBAC0+RBAC1+RBAC2

## RBAC0- Base

- users: individuals that need access to the system
- roles: named Job functions in the org. (a grouping of a set of permissions)
- permissions: approval to perform an operation on objects
- session: a mapping between a user and a subset of roles

Users are assigned to roles, and roles have permissions to act on objects.
A single session could have multiple Roles, but only one user.

## RBAC1

- Reflect a hierarchical structure of roles in org
- Mathematically, partial order (reflexive, transitive, anti-symmetric)
- inhertance of role permissions on one direction: (most)Boss <- Manager <- Employee (least)
    - heirarchy works in reverse, bottom up
    - leverage roles so that you don't have to define every role from scratch 
    - doctor inherits from nurse inherits from secretary
- can make primer roles to add extra permissions to variations of roles, or private permissions

## RBAC2

- adds constraints to RBAC0
- Constraints: reflect higher-level organizational policy
	- example: 
	1. Mutually exlusive roles (U-> R and R->)
		- User to only one role in set, permission to only one role
		-therfore, users with different roles will not have shared permissions
                - Auditory cannot be accountant too
	2. Cardinality: 
		- max number of users assigned to a role
		- or max number of roles to one user
		- for instance, only one person can be the CEO
	3. Prerequisite:
		- can only assign role if already assigned prerequisite role
		- another way of having roll hierarchies
		- in role heirarchy, if a user has R2 which inherits from R1, they always have both sets of permissions active
		- with pre-Req, a user may have both roles, but only activate the privledges of one, therefore supporting the least priledge principle
	4. Static Separation of Duty [SSD]
		- Separation of privilidge
		- aims to prevent conflicts of interest
		- SSD := (rs, n) where no user assigned to n or more roles from set rs
			- SSD := ({r1, r2}, 2) This is a mutually exlusive set. no user may have 2 or more roles in the set
	5. Dynamic Separation of Duty [DSD]
		- similar to SSD, but users can be assigned roles, they just cannot activate all priv. in one session
		- typically for temporal conflicts of interest
		- Definition: DSD := (role set, n) (n>=2) no user session may activate >= n roles from role set
## RBAC3
- supports least privilege: only those who need priv are assigned a role
- separation of duties: by ensuring that mutually exclusiv roles must be invoked to complete a ssensitive task

## NIST RBAC STANDARDS
- NATIONAL INSTITUTE OF TECH
- ANSI INCITS 359-2012 (new version, replaces 2004)
- ANSI INCITS 494-2012 suplements the above with enhanced constraints wihch includes attributes
- Ansi INCTS 459-20ll guidance in implementing RBAX systems

# Exploration: RBAC Role Engineering

How do we design an optimal set of roles given an organization

Two approaches that are proposed: Top-down and bottom up

## Top-Down

- RE must capture the orgs business rules as they relate to access control and be reflected in naming, defining structuting and constraining valid sets of roles
    - derives roles from organizational and business analysis
    - start analysis from rss and operations
- Role Engineer sits down with business admin staff:
    - analyze processes and ID job functions
    - decompose functions to tasks
    - ID actions and object for each task and id constraints
    - assign permissions to roles
- Pro: get what you want eventuallyu
- con: expensive and time consuming

## Bottom up

- Role Mining approach: using machine learning technologies to automatically discover roles from existing user permission assignments
- Pro: automated and quick
- Cons: the clusters may not have any meaning and that makes it more difficult to maintain
    - not gaurunteed to be consistent with access control policies
    - depends on how clean your data is. you dont want to feed in data that isn't conssitent with policy
- in practice a hybrid system is used, come up with an automated system and tweak it




















