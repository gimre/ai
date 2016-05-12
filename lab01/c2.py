from collections import namedtuple
import backtrack
import unittest


Student = namedtuple( 'Student', [ 'isBoy', 'classIndex' ] )


class BanquetProblem( backtrack.BacktrackingProblem ):

    def __init__( self, classes ):
        self.classes = classes
        self.studentCount = sum( [
            boys + girls for boys, girls in self.classes
        ] )

    def accept( self, candidate ):
        return len( candidate ) == self.studentCount

    def first( self, candidate ):
        if len( candidate ) == self.studentCount: return None
        return [ *candidate, Student( True, 0 ) ]

    def next( self, candidate ):
        student = candidate[-1]
        if student.isBoy: return [ *candidate[:-1], Student( False, student.classIndex ) ]
        if student.classIndex == ( len( self.classes ) - 1 ): return None
        return [ *candidate[:-1], Student( True, student.classIndex + 1 ) ]

    def reject( self, candidate ):
        if len( candidate ):
            for idx, ( maxBoys, maxGirls ) in enumerate( self.classes ):
                totalBoys = totalGirls = 0
                students = [ candidate[-1], *candidate, candidate[0] ]
                for prv, student, nxt in [ students[i-1:i+2] for i in range( 1, len( students ) - 1 ) ]:
                    if not student.isBoy and ( not prv.isBoy or not nxt.isBoy ): return True
                    #if prv.classIndex == student.classIndex: return True
                    if student.classIndex == idx:
                        totalBoys += ( 1 if student.isBoy else 0 )
                        totalGirls += ( 1 if not student.isBoy else 0 )
                if totalBoys > maxBoys or totalGirls > maxGirls: return True

    def root( self ):
        return [ ]


class TestBanquetProblem( unittest.TestCase ):
    def testOne( self ):
        problem = BanquetProblem( [
            ( 0, 1 ),
            ( 1, 0 ),
            ( 1, 0 )
        ] )
        for solution in problem.solve( ):
            print( list( map(
                lambda student: (
                    'boy' if student.isBoy else 'girl', student.classIndex + 1
                ),
                solution
            ) ) )


if __name__ == '__main__':
    unittest.main( )
