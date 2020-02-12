# This is a sample macro file with a single command.  When NatSpeak has the
# focus, say "demo sample one".  It should recognize the command and print it.

import natlink
from natlinkutils import *

class ThisGrammar(GrammarBase):

    gramSpec = """
        <start> exported = demo sample one;
    """
    
    def initialize(self):
        self.load(self.gramSpec)
        self.activateAll()

    def gotResults_start(self,words,fullResults):
		print 'Detected "demo sample one"'

thisGrammar = ThisGrammar()
thisGrammar.initialize()

print 'Demo command loaded, say "demo sample one"!'

def unload():
    global thisGrammar
    if thisGrammar: thisGrammar.unload()
    thisGrammar = None
