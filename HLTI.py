#!/usr/bin/env python

import urllib
import os

"""
Retrieves the number of bugs left until the arrival of elementary OS Freya beta 1.

Run via console it with: ./HLTI.py
"""

# Get Launchpad data.
f = urllib.urlopen("https://launchpad.net/elementary/+milestone/freya-beta1")
s = f.read()
f.close()

# Write data to temp file.
ff = open("temp.del", "w")
ff.write(s)
ff.close()

# Find number of bugs left.
temp = open("temp.del", "r")
for i, line in enumerate(temp):

	# New bugs.
	if 'span class="statusNEW">' in line and i < 450:
		a = temp.next()
		b = a.split('<strong>')
		c = b[1].split('</strong>')
		b_new = int(c[0])

	# Incomplete bugs.
	if 'span class="statusINCOMPLETE">' in line and i < 450:
		a = temp.next()
		b = a.split('<strong>')
		c = b[1].split('</strong>')
		b_incomp = int(c[0])

	# Confirmed bugs.
	if 'span class="statusCONFIRMED">' in line and i < 450:
		a = temp.next()
		b = a.split('<strong>')
		c = b[1].split('</strong>')
		b_conf = int(c[0])

	# In progress bugs.
	if 'span class="statusINPROGRESS">' in line and i < 450:
		a = temp.next()
		b = a.split('<strong>')
		c = b[1].split('</strong>')
		b_inprog = int(c[0])

# Delete temp file.
os.remove('temp.del')

# Print to console.
bugs = b_new + b_incomp + b_conf + b_inprog
if bugs >= 15:
	print '\n%d bugs left until Freya beta 1. Quit moaning.\n' % bugs
elif 10 <= bugs < 15:
	print '\n%d bugs left until Freya beta 1. Getting there.\n' % bugs
elif 5 <= bugs < 10:
	print '\n%d bugs left until Freya beta 1. Countdown begins!\n' % bugs
elif 1 < bugs < 5:
	print '\n%d bugs left until Freya beta 1. Soooo close!\n' % bugs
elif bugs == 1:
	print '\n%d bugs left until Freya beta 1. JUST ONE MORE TO GO!\n' % bugs
elif bugs == 0:
	print 'elementary OS Freya beta 1 has landed. You can officially freak out now.\n'
