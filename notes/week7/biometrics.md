# Biometrics

- Fingerprints, DNA, Palm print, hand geometry, iris patterns, retinal patters, typing rythm, gait, voice

- typing rhythm, gait and voice are behavioral (dynamic)
- others are physiological features (Static)

Advantages over passwords:
	- no need to remember it
	- most have more entropy than passwords (maybe not true esp for fingerprints)
	- convenient to use across multiple systems (assuming it's not compromised)

## What makes a good biometric:
	- all users of a system must possess the trait
	- uniqueness- trait should be different for each user
	- permanence/ stability over time so system can keep up
	- collectability trait should be easy to measure and process
	- performance. speed for collection + robust tech for collecting
	- acceptability from users (are they ok with it?)
	- Circumvention (ease with which trait can be imitated)
## biometrics in use

	1. Fingerprints:
		- maps fingerprint into a graph and compares with database
		- measurements are imprecise, so approximate matching algos are used
	2. Voices: speaker verification or recognition
		- verification: uses statistical techniques to test that speaker is who it claims
		- Recognition: checks content of answers (how/ what you answer password wise)
		- be weary of you voice being copied and used
	3. Eyes: patterns in irises and retnas
		- often used for higher val targets
		- do statistical test to match retinas
		- a bit more invasive
	4. Face: image, distance between features
		- lighting, view of face or other noise might hinder matching
	5. keystroke dynamics: believed to be unique
	 	- intervals, pressure, duration of the stroke, where key is struck
		- statistical test is used to match
	Great as a second means of checking ie. asked to type in password and keystrokes are checked

Users need to register information which is encoded into a template using some compliment function ( a hash)
this way raw data is not stored

## Performance Measures

- Enrollement failure rate:
	- rate of failure for creating templates
	- mainly due to low quality inputs (worn out fingers)
- Failure to captuyre/ Measure:
	- oily fingers, leftovers from previous person
- False Match/ false positive
	- could result in impersonation
- False Non-match/ False neg rate
	- denial of service/ locked out
## used for Identification/ surveillance as well

## Biometrics can be fooled and can change in time


