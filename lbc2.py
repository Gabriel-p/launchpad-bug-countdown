#!/usr/bin/env python

import urllib
import os
import re

"""
Retrieves the number of bugs left in a Launchpad project.

Run via console with: ./lbc2.py
"""

# Project's Launchpad ID.
project = 'freya-beta2'
# Name of project
proj_name = 'Freya beta 2'

bug_types = {'span class="statusNEW">': 0,
    'span class="statusINCOMPLETE">': 0,
    'span class="statusCONFIRMED">': 0,
    'span class="statusTRIAGED">': 0,
    'span class="statusINPROGRESS">': 0}

# Even though we have to use `open` and `close` and can simply enclose the next
# for loop with the calls, I still would load the file into a temporary array.
# Then iterate over that.
file = urllib.urlopen("https://launchpad.net/elementary/+milestone/" + project)
lines = [str(line) for line in file]
file.close()

# Because of the way `urlopen` streams the data, we cannot use the `next` command.
# Therefore, we need to use a flag to remember what kind of bug we found on the 
# previous line.
bug_type = ''
for index, line in enumerate(lines):
    if index >= 470:
        break

    if bug_type:
        bug_types[bug_type] += sum(map(int, re.findall('\d+', line)))
        bug_type = ''
    else:
        for key in bug_types:
            if key in line:
                bug_type = key
                break

# Print to console.
bugs = sum(bug_types.values())
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

message = ' bugs left until ' + proj_name + '. '  + message
print('\n{} {} \n'.format(bugs, message))