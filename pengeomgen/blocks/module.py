from . import base

class Module(base.Element):
    """
    Creation of modules according to the next formatted text lines

    0000000000000000000000000000000000000000000000000000000000000000
    MODULE  (  A4) comment
    MATERIAL(  A4)
    SURFACE (  A4), SIDE POINTER=(I2)
    BODY    (  A4)
    MODULE  (  A4)
    1111111111111111111111111111111111111111111111111111111111111111
      OMEGA=(         E22.15       ,  I4) DEG (DEFAULT=0.0)
      THETA=(         E22.15       ,  I4) DEG (DEFAULT=0.0)
        PHI=(         E22.15       ,  I4) DEG (DEFAULT=0.0)
    X-SHIFT=(         E22.15       ,  I4) (DEFAULT=0.0)
    Y-SHIFT=(         E22.15       ,  I4) (DEFAULT=0.0)
    Z-SHIFT=(         E22.15       ,  I4) (DEFAULT=0.0)
    """

    def __init__(self, label, material, surfaces=[], bodies=[], modules=[], comment="", **kwargs):
        super().__init__(label, comment, **kwargs)
        self.material=int(material)
        self.surfaces=surfaces
        self.bodies=bodies
        self.modules=modules
        
    def __str__(self):
        s="0000000000000000000000000000000000000000000000000000000000000000\n"
        s+="MODULE  ({0}) {1}\n".format(self.label, self.comment)
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
        # rotation and translation
        if self.rotation!=[0,0,0] or self.translation!=[0,0,0]:
            s+="\n1111111111111111111111111111111111111111111111111111111111111111"
        # rotation
        s+=self.representation_rotation()
        # translation
        s+=self.representation_translation()
        return s
