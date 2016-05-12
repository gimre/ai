class BacktrackingProblem( ):

    def accept( self, candidate ):
        return False

    def first( self, candidate ):
        return None

    def output( self, candidate ):
        return candidate

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
        if self.accept( candidate ): yield self.output( candidate )
        s = self.first( candidate )
        while s is not None:
            yield from self.__backtrack( s )
            s = self.next( s )
