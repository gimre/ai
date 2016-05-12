import time

def reject( candidate ):
    return len( candidate ) > 6

def accept( candidate ):
    return sum( candidate ) == 15 and len( candidate ) == 6

def first( candidate ):
    newCandidate = candidate[:] + [1]
    return newCandidate

def next( candidate ):
    last = candidate[-1]
    if last >= 6: return None
    return [ *candidate[:-1], last + 1 ]

def backtrack( candidate ):
    if reject( candidate ): return
    if accept( candidate ): yield candidate

    s = first( candidate )

    while s is not None:
        yield from backtrack( s )
        s = next( s )

count = 0

t1 = time.time( )
for result in backtrack( [] ): count += 1
t2 = time.time( )

print( 'found %d solutions in %s seconds' % ( count, t2 - t1 ) )
