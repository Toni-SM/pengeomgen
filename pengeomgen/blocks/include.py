from . import base

class Include(base.Base):
    """
    Insertion of others geometry definition files according to the next formatted text lines
    
    0000000000000000000000000000000000000000000000000000000000000000
    INCLUDE  comment
       FILE=(filename.ext)
       
    filename (string): absolute or relative path of the geometry definition file to be included
    starred (boolean): if True its allow the included file to be considered as if it were part of the main file
    comment (string): short text description
    """

    def __init__(self, filename, starred=False, comment="", **kwargs):
        super().__init__(comment)
        self.filename=filename
        self.starred=starred
        
    def __str__(self):
        s="0000000000000000000000000000000000000000000000000000000000000000\n"
        s+="INCLUDE{0} {1}\n".format("*" if self.starred else " ", self.comment)
        s+="   FILE={0}".format(self.filename)
        return s

    # TODO: delete
    def set_void_inner_volume_factor(self, *k):
        pass