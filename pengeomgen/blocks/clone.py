from . import base

class Clone(base.Element):
    """
    Clonation of modules according to the next formatted text lines

    0000000000000000000000000000000000000000000000000000000000000000
    CLONE   (  A4) comment: copies one module and moves it
    MODULE  (  A4) original module
    1111111111111111111111111111111111111111111111111111111111111111
      OMEGA=(         E22.15       ,  I4) DEG (DEFAULT=0.0)
      THETA=(         E22.15       ,  I4) DEG (DEFAULT=0.0)
        PHI=(         E22.15       ,  I4) DEG (DEFAULT=0.0)
    X-SHIFT=(         E22.15       ,  I4) (DEFAULT=0.0)
    Y-SHIFT=(         E22.15       ,  I4) (DEFAULT=0.0)
    Z-SHIFT=(         E22.15       ,  I4) (DEFAULT=0.0)
    """

    def __init__(self, label, module, comment="", **kwargs):
        super().__init__(label, comment, **kwargs)
        if issubclass(type(module), base.Base):
            self.module=module.label
        else:
            self.module=("    "+module)[-4:]
        
    def __str__(self):
        s="0000000000000000000000000000000000000000000000000000000000000000\n"
        s+="CLONE   ({0}) {1}\n".format(self.label, self.comment)
        s+="MODULE  ({0})".format(self.module)
        # rotation and translation
        if self.rotation!=[0,0,0] or self.translation!=[0,0,0]:
            s+="\n1111111111111111111111111111111111111111111111111111111111111111"
        # rotation
        s+=self.representation_rotation()
        # translation
        s+=self.representation_translation()
        return s
