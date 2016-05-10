import unittest

class C1( ):
    def __init__( self ):
        self.x = 2
    def add( self, value ):
        self.x += value

class C1Test( unittest.TestCase ):
    def testC1( self ):
        self.assertTrue( True )

if __name__ == '__main__':
    unittest.main( )
