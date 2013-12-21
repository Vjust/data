"""  Sample regular expression code

~~~~~~~~~~begin text 

•	Begich (AK) – Flake(AZ) Crop Insurance Transparency Amendment - SUPPORT
This amendment permits RMA to disclose the names of insurance subsidy recipients, making crop insurance disclosure requirements consistent with requirements for other subsidies, disaster payments, and conservation payments at no cost to the taxpayer.

•	Feinstein (CA) – McCain(AZ)  Tobacco Insurance Amendment - SUPPORT
While this amendment does not prohibit tobacco farmers from obtaining crop insurance, it does prohibits RMA from providing insurance premium support to tobacco farmers, generating more than $300 million in savings over ten years. 

•	Boxer (CA) GE Labeling Amendment - SUPPORT
This amendment expresses the sense of the Senate that the United States should join 64 other nations in giving their consumers the right to know whether there are genetically engineered ingredients in their food.  At least 93 percent of Americans want to know whether there are GE ingredients in their food, regardless of race, income, education, or party affiliation and 26 states are moving to require GE labeling

•	Senator (STATE) Amendment Name - POSITION
Description of the amendment.

~~~~~~~~~~ end of text ~~~~~~~~~~~~~~~~~~~~~~~"""

restring=r"^(.)\W*(\w*\W*\(.*\))\W*(.*)(SUPPORT|OPPOSE)"
lines=open("c:/Users/vrao/Desktop/amendment.txt").readlines()
t2 = re.match(restring, lines[6])
t1 = re.match(restring, lines[0])
t1.groups()[1:4]
#>> ('Begich (AK) \xe2\x80\x93 Flake(AZ)', 'Crop Insurance Transparency Amendment - ', 'SUPPORT')
t2.groups()[1:4]
#>>> ('Boxer (CA)', 'GE Labeling Amendment - ', 'SUPPORT')