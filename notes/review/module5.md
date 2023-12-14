# Access control

1. What are the 3 As of authentication?
- Authorization, Authentication, Audit

2. Which access policy allows users to adjust it?
- Discrestionary access control

3. Which access control policy uses attributes of the environment?
- Attribute-based access control

4. Which access control model is based on labels associated with process and resrsources?
- Mandatory access control - Military (top-secret, confidential etc)
- users fit into an immovable system

5. What are the key principles of all access control policies?
- least privilege and separation of duty (also dual control for critical tasks)

# Access control matrix

1. What are the three access control elements?
- subject, object, access rights

2. what is obtained by slicing the access control matrix by column?
- Access control lists

3. What is obtained by slicing the access control matrix by row?
- Capabilities

4. what is easier to audit when using contro lists?
- per-object review

5. What is easier to audit when using capabilities?
- Per subject review

#DAC (discretionary access control)
1. how many protection bits are associated with each file and directory in traditional unix systems?
- 12 bits! there are three extra bits or set UserID, set Group ID (temporary permissions granting) and sticky bits (only the owner can rename, move or delete file)

2. Whose permissions are encoded in the second octet amont the 9 protection bits?
- Group

3. In Unix File systems Access control are super users exempt from usual access control restrictions?
- True!

4. In modern windows systems thre are two ACLs associated with objects, the system ACL and the discretionary ACL.
- True


