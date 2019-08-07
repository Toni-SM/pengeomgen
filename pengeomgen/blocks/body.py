from . import base

class Body(base.AdvancedElement):
    """
    Creation of homogeneous bodies limited by quadric surfaces according to the next formatted text lines
    
    0000000000000000000000000000000000000000000000000000000000000000
    BODY    (  A4) comment
    MATERIAL(  A4)
    SURFACE (  A4), SIDE POINTER=(I2)
    BODY    (  A4)
    MODULE  (  A4)
    """

    def __init__(self, label, material, comment="", **kwargs):
        super().__init__(label, material, comment, **kwargs)
        
    def __str__(self):
        s="0000000000000000000000000000000000000000000000000000000000000000\n"
        s+="BODY    ({0}) {1}\n".format(self.label, self.comment)
        # material
        s+="MATERIAL({0})".format(("    "+str(self.void_inner_volume_factor*self.material if self.material<0 else self.material))[-4:])
        # surfaces, bodies and modules 
        s+=self.representation_elements()
        return s
