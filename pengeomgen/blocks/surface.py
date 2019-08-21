from . import base

class Surface(base.Element):
    """
    Creation of quadric surfaces (reduced form by default) according to the next formatted text lines
    
    # REDUCED FORM
    0000000000000000000000000000000000000000000000000000000000000000
    SURFACE (    ) reduced form
    INDICES=( 1, 1, 1, 1, 1)
    X-SCALE=(+1.000000000000000E+00,   0) (DEFAULT=1.0)
    Y-SCALE=(+1.000000000000000E+00,   0) (DEFAULT=1.0)
    Z-SCALE=(+1.000000000000000E+00,   0) (DEFAULT=1.0)
      OMEGA=(+0.000000000000000E+00,   0) DEG (DEFAULT=0.0)
      THETA=(+0.000000000000000E+00,   0) DEG (DEFAULT=0.0)
        PHI=(+0.000000000000000E+00,   0) RAD (DEFAULT=0.0)
    X-SHIFT=(+0.000000000000000E+00,   0) (DEFAULT=0.0)
    Y-SHIFT=(+0.000000000000000E+00,   0) (DEFAULT=0.0)
    Z-SHIFT=(+0.000000000000000E+00,   0) (DEFAULT=0.0)
    
    
    # IMPLICIT FORM
    0000000000000000000000000000000000000000000000000000000000000000
    SURFACE (    ) implicit form
    INDICES=( 0, 0, 0, 0, 0)
        AXX=(+0.000000000000000E+00,   0) (DEFAULT=0.0)
        AXY=(+0.000000000000000E+00,   0) (DEFAULT=0.0)
        AXZ=(+0.000000000000000E+00,   0) (DEFAULT=0.0)
        AYY=(+0.000000000000000E+00,   0) (DEFAULT=0.0)
        AYZ=(+0.000000000000000E+00,   0) (DEFAULT=0.0)
        AZZ=(+0.000000000000000E+00,   0) (DEFAULT=0.0)
         AX=(+0.000000000000000E+00,   0) (DEFAULT=0.0)
         AY=(+0.000000000000000E+00,   0) (DEFAULT=0.0)
         AZ=(+0.000000000000000E+00,   0) (DEFAULT=0.0)
         A0=(+0.000000000000000E+00,   0) (DEFAULT=0.0)
    1111111111111111111111111111111111111111111111111111111111111111
      OMEGA=(+0.000000000000000E+00,   0) DEG (DEFAULT=0.0)
      THETA=(+0.000000000000000E+00,   0) DEG (DEFAULT=0.0)
        PHI=(+0.000000000000000E+00,   0) RAD (DEFAULT=0.0)
    X-SHIFT=(+0.000000000000000E+00,   0) (DEFAULT=0.0)
    Y-SHIFT=(+0.000000000000000E+00,   0) (DEFAULT=0.0)
    Z-SHIFT=(+0.000000000000000E+00,   0) (DEFAULT=0.0)
   
    filename (string): absolute or relative path of the geometry definition file to be included
    starred (boolean): if True its allow the included file to be considered as if it were part of the main file
    comment (string): short text description
    """

    def __init__(self, label, indices, starred=False, comment="", **kwargs):
        super().__init__(label, comment, **kwargs)
        self.indices=indices
        self.starred=starred
        
        # implicit form
        self.AXX=kwargs.get("AXX", 0)
        self.AXY=kwargs.get("AXY", 0)
        self.AXZ=kwargs.get("AXZ", 0)
        self.AYY=kwargs.get("AYY", 0)
        self.AYZ=kwargs.get("AYZ", 0)
        self.AZZ=kwargs.get("AZZ", 0)
        self.AX=kwargs.get("AX", 0)
        self.AY=kwargs.get("AY", 0)
        self.AZ=kwargs.get("AZ", 0)
        self.A0=kwargs.get("A0", 0)
        
    def __str__(self):
        s="0000000000000000000000000000000000000000000000000000000000000000\n"
        s+="SURFACE{0}({1}) {2}\n".format("*" if self.starred else " ", self.label, self.comment)
        s+="INDICES=({0})".format(",".join([str(i) if i<0 else " "+str(i) for i in self.indices]))
        # reduced form
        if self.indices!=(0,0,0,0,0):            
            s+=self.representation_scale()
        # implicit form
        else:
            if self.AXX:
                s+="\n    AXX=({0},   0)".format(format(self.AXX, "+22.15E"))
            if self.AXY:
                s+="\n    AXY=({0},   0)".format(format(self.AXY, "+22.15E"))
            if self.AXZ:
                s+="\n    AXZ=({0},   0)".format(format(self.AXZ, "+22.15E"))
            if self.AYY:
                s+="\n    AYY=({0},   0)".format(format(self.AYY, "+22.15E"))
            if self.AYZ:
                s+="\n    AYZ=({0},   0)".format(format(self.AYZ, "+22.15E"))
            if self.AZZ:
                s+="\n    AZZ=({0},   0)".format(format(self.AZZ, "+22.15E"))
            if self.AX:
                s+="\n     AX=({0},   0)".format(format(self.AX, "+22.15E"))
            if self.AY:
                s+="\n     AY=({0},   0)".format(format(self.AY, "+22.15E"))
            if self.AZ:
                s+="\n     AZ=({0},   0)".format(format(self.AZ, "+22.15E"))
            if self.A0:
                s+="\n     A0=({0},   0)".format(format(self.A0*self.unit_multiplication_factor, "+22.15E"))
            # rotation and translation
            if self.rotation!=[0,0,0] or self.translation!=[0,0,0]:
                s+="\n1111111111111111111111111111111111111111111111111111111111111111"
        # rotation
        s+=self.representation_rotation()
        # translation
        s+=self.representation_translation()
        return s
