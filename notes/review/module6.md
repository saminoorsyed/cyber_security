#RBAC
1. Rbac sessions cannot have multple active users, but a user can have multiple roles

2. Static separation of duty is applied during role assignment for conflict of interests

3. Dynamic separation of duty prevents temporal conflict of interest and is applied during role activation in sessions

4. Rbac supports separation of privilege and least privilege

# Mandatory security Policies

1. what is the simple security property in BLP?
- No read up

2. what is the \* security property in the BLP confidentiality model?
- no write down

3. When using DAC along with MAC which what determines access?
- Only gran access if MAC policy also grants access
- Only grant access if both mac and dac allow access

4. what does it mean when a security label dominates another?
- that it matches the labels and exceeds them
- subject s can only read object o if label s dominates label o (meets it beats it)
- can only read and write if the labels are the same

#BIBA integrity model

1. the higher the integrity level, the more confident we are in the reliability of the information contained withing

2. the higher the integrity level, the more confident we are that it will execute correctly

3. What is The simple security property in BIBA?
- No Write up

4. what is the \* security property in BIBA?
- no Read down

#Chinese firewall

1. Chineses fire wall enforces conflic of interest policies

2. What is the simple security principle of chinese fire wall policy?
- Cannot read two object belonging to the same CI class bu in separate datasets

3. what are the implications of the \* security property in chinese wall model?
- Can Write to an object O IFF all the objects the subject has ever read are in the same DS as O
- Cannot write to objects belonging to different data sets
- to write to an object, the subject must first have read access
- prevents writing info that might be picked up by a competitor
