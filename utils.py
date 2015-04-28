'''
Utilities.

For now this just exports the run() function, which times a test function,
validates its output, and reports how long it took.
'''
import time


def run(function, expected, **medals):
    '''
    Run the function; complain if the expected output is not obtained, else
    go through the provided medals.
    '''
    medals = sorted((time, medal) for medal, time in medals.items())[::-1]

    start = time.time()
    result = function()
    elapsed = time.time() - start

    if result != expected:
        print('Your function did not produce the expected output!')
        return

    print('Your function produced correct output in %0.6f seconds.' % elapsed)
    for i in range(len(medals)):
        if elapsed > medals[i][0]:
            break
    else:
        i += 1
    if i == 0:
        print('Your function won no medal.  Keep trying!')
    else:
        print('Your function won a %s medal!' % medals[i - 1][1])
    if i < len(medals):
        print('To get a %s medal, beat %0.6f seconds.' %
              (medals[i][1], medals[i][0]))
