from abc import ABC, abstractmethod

class Base(ABC):
    def __init__(self, comment=""):
        self.comment=comment
        
    @abstractmethod
    def __str__(self):
        pass
        
    # TODO: delete
    void_inner_volume_factor=1
    def set_void_inner_volume_factor(self, *k):
        pass
        
class Element(Base):
    def __init__(self, label, comment="", **kwargs):
        Base.__init__(self, comment)
        self.label=("    "+label)[-4:]
        
        self.scale=list(kwargs.get("scale", [1,1,1]))
        self.rotation=list(kwargs.get("rotation", [0,0,0]))
        self.translation=list(kwargs.get("translation", [0,0,0]))
        
        # scale (single parameters)
        self.scale[0]=kwargs.get("xscale", self.scale[0])
        self.scale[1]=kwargs.get("yscale", self.scale[1])
        self.scale[2]=kwargs.get("zscale", self.scale[2])
        
        # rotation (single parameters)
        self.rotation[0]=kwargs.get("omega", self.rotation[0])
        self.rotation[1]=kwargs.get("theta", self.rotation[1])
        self.rotation[2]=kwargs.get("phi", self.rotation[2])
        
        # translation (single parameters)
        self.translation[0]=kwargs.get("xshift", self.translation[0])
        self.translation[1]=kwargs.get("yshift", self.translation[1])
        self.translation[2]=kwargs.get("zshift", self.translation[2])
        
        # angle unit
        self.angle=kwargs.get("angle", "DEG").upper()[:3]
        if self.angle!="RAD":
            self.angle="DEG"

    @abstractmethod
    def __str__(self):
        pass
        
    def representation_scale(self):
        s=""
        # scale x
        if self.scale[0]!=1:
            s+="\nX-SCALE=({0},   0)".format(format(self.scale[0], "+22.15E"))
        # scale y
        if self.scale[1]!=1:
            s+="\nY-SCALE=({0},   0)".format(format(self.scale[1], "+22.15E"))
        # scale z
        if self.scale[2]!=1:
            s+="\nZ-SCALE=({0},   0)".format(format(self.scale[2], "+22.15E"))
        return s       
        
    def representation_rotation(self):
        s=""
        # omega
        if self.rotation[0]:
            s+="\n  OMEGA=({0},   0) {1}".format(format(self.rotation[0], "+22.15E"), self.angle)
        # theta
        if self.rotation[1]:
            s+="\n  THETA=({0},   0) {1}".format(format(self.rotation[1], "+22.15E"), self.angle)   
        # phi
        if self.rotation[2]:
            s+="\n    PHI=({0},   0) {1}".format(format(self.rotation[2], "+22.15E"), self.angle)
        return s

    def representation_translation(self):
        s=""
        # shift x
        if self.translation[0]:
            s+="\nX-SHIFT=({0},   0)".format(format(self.translation[0], "+22.15E"))
        # shift y
        if self.translation[1]:
            s+="\nY-SHIFT=({0},   0)".format(format(self.translation[1], "+22.15E"))
        # shift z
        if self.translation[2]:
            s+="\nZ-SHIFT=({0},   0)".format(format(self.translation[2], "+22.15E"))
        return s
