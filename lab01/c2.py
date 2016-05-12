import unittest


class BacktrackingProblem( ):

    def accept( self, candidate ):
        return False

    def first( self, candidate ):
        return None

    def output( self, candidate ):
        pass

    def next( self, candidate ):
        return None

    def reject( self, candidate ):
        return True

    def root( self ):
        return None

    def solve( self ):
        return self.__backtrack( self.root( ) )

    def __backtrack( self, candidate ):
        if self.reject( candidate ): return
        if self.accept( candidate ): self.output( candidate )
        s = self.first( candidate )
        while s is not None:
            self.__backtrack( s )
            s = self.next( s )


class BanquetProblemCandidate(  ):
    def __init__( self, classes = [ ], students = [ ] ):
        self.classes  = classes[ : ]
        self.students = students[ : ]


class BanquetProblem( BacktrackingProblem ):

    def __init__( self, classes ):
        self.classes = classes
        self.studentCount = sum( [
            boys + girls for boys, girls in self.classes
        ] )
        self.results = [ ]

    def accept( self, candidate ):
        return len( candidate.students ) == self.studentCount

    def first( self, candidate ):
        if len( candidate.students ) < self.studentCount:
            return BanquetProblemCandidate(
                candidate.classes[ : ].append( ( 1, 0 ) ),
                candidate.students[ : ].append( ( 1, 0, len( self.classes ) + 1 ) )
            )
        return None

    def next( self, candidate ):
        currentMax = zip( candidate.classes, self.classes )

        for i, ( current, max ) in enumerate( currentMax ):

            ( currentBoys, currentGirls ) = current
            ( maxBoys, maxGirls )         = max

            if currentBoys < maxBoys:
                return BanquetProblemCandidate(
                    [  ].append( ( currentBoys + 1, currentGirls ) )
                        .append( candidate.classes[ 1: ] ),
                    candidate.students.append( ( 1, 0, i ) )
                )

            if currentGirls < maxGirls:
                return BanquetProblemCandidate(
                    [  ].append( ( currentBoys, currentGirls + 1 ) )
                        .append( candidate.classes[ 1: ] ),
                    candidate.students.append( ( 0, 1, i ) )
                )

        return None

    def output( self, candidate ):
        self.results.append( candidate )

    def reject( self, candidate ):
        return False

    def root( self ):
        return BanquetProblemCandidate( )

    def solve( self ):
        super( BanquetProblem, self ).solve( )
        return self.results


class TestC2( unittest.TestCase ):
    def testOne( self ):
        results = BanquetProblem( [
            ( 3, 5 ), ( 6, 4 )
        ] ).solve( )
        self.assertEqual( results, True )


if __name__ == '__main__':
    unittest.main( )
