import backtrack
import time
import unittest


BanquetProblemCandidate = namedtuple( 'BanquetProblemCandidate', [
    'classes',
    'students'
] )


class BanquetProblem( backtrack.BacktrackingProblem ):

    def __init__( self, classes ):
        self.classes = classes
        self.studentCount = sum( [
            boys + girls for boys, girls in self.classes
        ] )

    def accept( self, candidate ):
        return len( candidate.students ) == self.studentCount

    def first( self, ( classes, students ) ):
        return None

    def next( self, candidate ):
        ( classes, students ) = candidate
        lastIndex = len( classes ) - 1
        ( isBoy, isGirl, classIndex ) = students[ lastIndex ]
        ( maxBoys, maxGirls ) = self.classes[ lastIndex ]

        if( current < maxBoys ) {
            return BanquetProblemCandidate(
                [ *classes[:-1], (  ) ]
            )
        }


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

    def reject( self, ( classes, students ) ):
        return len( students ) > self.studentCount

    def root( self ):
        return BanquetProblemCandidate( [ ], [ ] )


class TestBanquetProblem( unittest.TestCase ):
    def testOne( self ):
        problem = BanquetProblem( [
            ( 3, 5 ),
            ( 6, 4 )
        ] )
        for solution in problem.solve( ): print( solution )


if __name__ == '__main__':
    unittest.main( )
