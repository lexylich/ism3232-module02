# debug_log.md
# Author: Alexis (Lexy) Lichtenstein

## Bug 1
Error type: KeyError: 'amount'
File + line: week8_buggy.py, line 12, in get_total()
What the error means: Python looked for the key 'amount' in a dictionary and it wasn't there because line 4 spells 'amout'.
What I told the duck: The function starts total at 0, loops through each record, adds that record's 'amount' value to total, then returns it.
What I tried: I read through the records list 
How I fixed it: I changed 'amout' to 'amount' in line 4

## Bug 2
Error type: TypeError
File + line:week8_buggy.py, line 16, in is_over_limit()
What the error means: Python can’t compare a number to text, 1000 is a number but ‘1000’ in quotes is text.
How I fixed it: I removed the quotes from 1000 in line 16

## After Fixing Both Bugs
Final output: Total: $5150.00 across 3 records, True
Did pytest pass? Yes

## AI Literacy Reflection
Did I use AI? Yes
If yes -- exact prompt I used: What do these errors mean?
What AI explained: That KeyError means the key 'amount' wasn't in the dictionary, and that the quotes around '1000' made it text, so it needed to be the number 1000.
What I changed myself: I found and fixed the 'amout' typo on line 4 using the DEBUG print, and I made the pytest file and ran it.
Can I explain every fixed line? Yes

## What I learned
I learned how to read a traceback from the bottom up to find the error type and the line it happened on. A KeyError means a dictionary key is missing or misspelled, and a TypeError means I compared two different kinds of data. Using a print statement to check each record helped me spot the typo instead of guessing.