#

# Source *linux handbook* | `search` blockexample
import sys
usage = '\nPass a num, check that is `1` or not'
 
a = sys.argv[1] if len(sys.argv) > 1 else print(usage)

if a == "1":
    print('\n==> `a` is one')
    print('This is still the THEN clause of the IF statement.')

else:
    print('\n==> `a` is', a)
    print('This is still the ELSE clause of the IF statement.')

print('\n\t==> This is after the IF statement.\n')
