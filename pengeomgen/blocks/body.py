from . import base

class Body(base.Element):
    """
    Creation of homogeneous bodies limited by quadric surfaces according to the next formatted text lines
    
    0000000000000000000000000000000000000000000000000000000000000000
    BODY    (  A4) comment
    MATERIAL(  A4)
    SURFACE (  A4), SIDE POINTER=(I2)
    BODY    (  A4)
    MODULE  (  A4)
    """

    def __init__(self, label, material, surfaces=[], bodies=[], modules=[], comment="", **kwargs):
        super().__init__(label, comment, **kwargs)
        self.material=int(material)
        self.surfaces=surfaces
        self.bodies=bodies
        self.modules=modules
        
    def __str__(self):
        s="0000000000000000000000000000000000000000000000000000000000000000\n"
        s+="BODY    ({0}) {1}\n".format(self.label, self.comment)
        # material
        s+="MATERIAL({0})".format(("    "+str(self.void_inner_volume_factor*self.material if self.material<0 else self.material))[-4:])
        # surfaces
        for surface in self.surfaces:
            s+="\nSURFACE ({0}), SIDE POINTER=({1})".format(("    "+surface[0])[-4:], str(surface[1]) if surface[1]<0 else " "+str(surface[1]))
        # bodies
        for body in self.bodies:
            s+="\nBODY    ({0})".format(("    "+body)[-4:])
        # modules
        for module in self.modules:
            s+="\nMODULE  ({0})".format(("    "+module)[-4:])
        return s
