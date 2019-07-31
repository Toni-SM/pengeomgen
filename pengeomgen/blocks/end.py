from . import base

class End(base.Base):
    """
    Cancel the reading of geometry data for the PENELOPE PENGEOM application
    
    0000000000000000000000000000000000000000000000000000000000000000
    END      0000000000000000000000000000000000000000000000000000000
    """

    def __init__(self, **kwargs):
        super().__init__()
        
    def __str__(self):
        s="0000000000000000000000000000000000000000000000000000000000000000\n"
        s+="END      0000000000000000000000000000000000000000000000000000000"
        return s
