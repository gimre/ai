import unittest

def getMaxKeyAndValue( dict ):
    return

class C1( ):
    def __init__( self, text ):
        self.text = text

    def longestWord( self ):
        words     = list( reversed( self.text.split( ) ) )
        lengths   = [ len( word ) for word in words ]
        maxLength = max( lengths )
        return words[ lengths.index( maxLength ) ]

    def mostFrequentWord( self ):
        freqMap = self.wordFrequency( )
        mostFrequent  = max( freqMap.keys( ), key = lambda k: freqMap[ k ] )
        return ( mostFrequent, freqMap[ mostFrequent ] )

    def mostFrequentNgram( self, length ):
        return ( )

    def ngramFrequency( self, length ):
        return { }

    def wordFrequency( self ):
        words   = self.text.split( )
        freqMap = {}
        for word in words:
            freqMap[ word ] = freqMap[ word ] + 1 if word in freqMap else 1
        return freqMap


class TestLongestWord( unittest.TestCase ):
    def testSingle( self ):
        self.assertEqual( C1( 'a very clear longest word' ).longestWord( ), 'longest' )
    def testMultiple( self ):
        self.assertEqual( C1( 'this is a nice text' ).longestWord( ), 'text' )

class TestMostFrequent( unittest.TestCase ):
    def testOne( self ):
        self.assertEqual( C1( 'this like is the best like frequency like test' ).mostFrequentWord( ), ( 'like', 3 ) )

class TestNgramFrequency( unittest.TestCase ):
    def testOne( self ):
        self.assertEqual( C1( 'abc deabcd cde' ).ngramFrequency( 3 ) )

class TestWordFrequency( unittest.TestCase ):
    def testOne( self ):
        self.assertEqual( C1( 'this is a nice text' ).wordFrequency( ), {
            'a': 1,
            'is': 1,
            'nice': 1,
            'text': 1,
            'this': 1
        } )
    def testTwo( self ):
        self.assertEqual( C1( 'this like is the best like frequency like test' ).wordFrequency( ), {
            'best': 1,
            'is': 1,
            'frequency': 1,
            'like': 3,
            'test': 1,
            'the': 1,
            'this': 1
        } )

if __name__ == '__main__':
    unittest.main( )
