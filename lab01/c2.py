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

class BanquetProblem( BacktrackingProblem ):
    def __init__( self, classes ):
        self.classes = classes
        self.results = [ ]
    def output( self, candidate ):
        self.results.append( candidate )
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
