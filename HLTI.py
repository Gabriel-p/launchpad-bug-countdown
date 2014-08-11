#!/usr/bin/env python

import urllib
import os

"""
Retrieves the number of bugs left in a Launchpad project.

Run via console it with: ./HLTI.py
"""

# Project's Launchpad ID.
project = 'freya-beta2'
# Name of project
proj_name = 'Freya beta 2'


# Get Launchpad data.
f = urllib.urlopen("https://launchpad.net/elementary/+milestone/" + project)
s = f.read()
f.close()

# Write data to temp file.
ff = open("temp.del", "w")
ff.write(s)
ff.close()

# Find number of bugs left.
temp = open("temp.del", "r")
b_new, b_incomp, b_conf, b_triaged, b_inprog = 0, 0, 0, 0, 0
break_lim = 470
for i, line in enumerate(temp):

	if i < break_lim:

		# New bugs.
		if 'span class="statusNEW">' in line:
			a = temp.next()
			b = a.split('<strong>')
			c = b[1].split('</strong>')
			b_new = int(c[0])

		# Incomplete bugs.
		if 'span class="statusINCOMPLETE">' in line:
			a = temp.next()
			b = a.split('<strong>')
			c = b[1].split('</strong>')
			b_incomp = int(c[0])

		# Confirmed bugs.
		if 'span class="statusCONFIRMED">' in line:
			a = temp.next()
			b = a.split('<strong>')
			c = b[1].split('</strong>')
			b_conf = int(c[0])

		# Triaged bugs.
		if 'span class="statusTRIAGED">' in line:
			a = temp.next()
			b = a.split('<strong>')
			c = b[1].split('</strong>')
			b_triaged = int(c[0])

		# In progress bugs.
		if 'span class="statusINPROGRESS">' in line:
			a = temp.next()
			b = a.split('<strong>')
			c = b[1].split('</strong>')
			b_inprog = int(c[0])
	else:
		break

# Delete temp file.
os.remove('temp.del')

# Print to console.
bugs = b_new + b_incomp + b_conf + b_triaged + b_inprog
if bugs >= 15:
	message = 'Quit moaning.\n'
elif 10 <= bugs < 15:
	message = 'Getting there.\n'
elif 5 <= bugs < 10:
	message = 'Countdown begins!\n'
elif 1 < bugs < 5:
	message = 'Soooo close!\n'
elif bugs == 1:
	message = 'JUST ONE MORE TO GO!\n'
elif bugs == 0:
	message = ''

print ('\n%d bugs left until ' + proj_name + '. '  + message) % bugs
