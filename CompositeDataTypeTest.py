"""
CompositeDataTypeTest
"""

import logging
import re
import string
from cgi import escape
from galaxy.datatypes.data import Text, Data
from galaxy.datatypes.metadata import MetadataElement
from galaxy.datatypes import metadata

log = logging.getLogger(__name__)

class CompositeDataTypeTest( Text ):
    
    file_ext = 'cdt'
    #is_binary = False
    composite_type = 'auto_primary_file'
    #allow_datatype_change = False

    MetadataElement( name="meta_1", default=0, desc="Metadata test 1", readonly=True, visible=False, optional=True, no_value=0 )


    def __init__( self, **kwd ):
        Text.__init__( self, **kwd )

        log.debug("\n\n\n######### Composite Data Test ############\n\n\n")
        
        self.add_composite_file('test_file_1.txt', description = 'test file 1', mimetype = 'text/html', is_binary = False )
        self.add_composite_file('test_file_2.txt', description = 'test file 2', mimetype = 'text/html', optional = True, is_binary = False )
        self.add_composite_file('test_file_3.txt', description = 'test file 3', mimetype = 'text/html', optional = True, is_binary = False )
        

    def set_meta( self, dataset, overwrite=True, **kwd ):
        log.debug("\n\n####### setting metadata #########\n\n")
        dataset.metadata.meta_1 = 'meta_1 testval'
        

    def set_peek( self, dataset, is_multi_byte=False ):
        log.debug("\n\n####### set_peek() " +  dataset.file_name + " ##########\n\n")
        dataset.peek = 'peek test'
        dataset.blurb = 'blurb test'

                
    def generate_primary_file( self, dataset = None ):
        log.debug("\n\n######## generate_primary_file() for Test data #######\n\n")

        return('<html><body>my test html</body></html>')

        
    def sniff( self, filename ):
        log.debug("\n\n##### Sniffing file: " + filename + "  ################\n\n")
        return False

