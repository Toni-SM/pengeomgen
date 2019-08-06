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
        
        self.scale=kwargs.get("scale", (1,1,1))
        self.rotation=kwargs.get("rotation", (0,0,0))
        self.translation=kwargs.get("translation", (0,0,0))
        
        # scale (single parameters)
        self.xscale=kwargs.get("xscale", None)
        self.yscale=kwargs.get("yscale", None)
        self.zscale=kwargs.get("zscale", None)
        
        # rotation (single parameters)
        self.omega=kwargs.get("omega", None)
        self.theta=kwargs.get("theta", None)
        self.phi=kwargs.get("phi", None)
        
        # translation (single parameters)
        self.xshift=kwargs.get("xshift", None)
        self.yshift=kwargs.get("yshift", None)
        self.zshift=kwargs.get("zshift", None)

    @abstractmethod
    def __str__(self):
        pass
        
    def representation_scale(self):
        s=""
        # scale x
        if self.xscale!=None and self.xscale!=1:
            s+="\nX-SCALE=({0},   0)".format(format(self.xscale, "+22.15E"))
        elif self.scale[0]!=1:
            if not self.xscale==1:
                s+="\nX-SCALE=({0},   0)".format(format(self.scale[0], "+22.15E"))
        # scale y
        if self.yscale!=None and self.yscale!=1:
            s+="\nY-SCALE=({0},   0)".format(format(self.yscale, "+22.15E"))
        elif self.scale[1]!=1:
            if not self.yscale==1:
                s+="\nY-SCALE=({0},   0)".format(format(self.scale[1], "+22.15E"))
        # scale z
        if self.zscale!=None and self.zscale!=1:
            s+="\nZ-SCALE=({0},   0)".format(format(self.zscale, "+22.15E"))
        elif self.scale[2]!=1:
            if not self.zscale==1:
                s+="\nZ-SCALE=({0},   0)".format(format(self.scale[2], "+22.15E"))
        return s       
        
    def representation_rotation(self):
        s=""
        # omega
        if self.omega!=None and self.omega!=0:
            s+="\n  OMEGA=({0},   0) DEG".format(format(self.omega, "+22.15E"))
        elif self.rotation[0]:
            if not self.omega==0:
                s+="\n  OMEGA=({0},   0) DEG".format(format(self.rotation[0], "+22.15E"))
        # theta
        if self.theta!=None and self.theta!=0:
            s+="\n  THETA=({0},   0) DEG".format(format(self.theta, "+22.15E"))
        elif self.rotation[1]:
            if not self.theta==0:
                s+="\n  THETA=({0},   0) DEG".format(format(self.rotation[1], "+22.15E"))   
        # phi
        if self.phi!=None and self.phi!=0:
            s+="\n    PHI=({0},   0) DEG".format(format(self.phi, "+22.15E"))
        elif self.rotation[2]:
            if not self.phi==0:
                s+="\n    PHI=({0},   0) DEG".format(format(self.rotation[2], "+22.15E"))
        return s

    def representation_translation(self):
        s=""
        # shift x
        if self.xshift!=None and self.xshift!=0:
            s+="\nX-SHIFT=({0},   0)".format(format(self.xshift, "+22.15E"))
        elif self.translation[0]:
            if not self.xshift==0:
                s+="\nX-SHIFT=({0},   0)".format(format(self.translation[0], "+22.15E"))
        # shift y
        if self.yshift!=None and self.yshift!=0:
            s+="\nY-SHIFT=({0},   0)".format(format(self.yshift, "+22.15E"))
        elif self.translation[1]:
            if not self.yshift==0:
                s+="\nY-SHIFT=({0},   0)".format(format(self.translation[1], "+22.15E"))
        # shift z
        if self.zshift!=None and self.zshift!=0:
            s+="\nZ-SHIFT=({0},   0)".format(format(self.zshift, "+22.15E"))
        elif self.translation[2]:
            if not self.zshift==0:
                s+="\nZ-SHIFT=({0},   0)".format(format(self.translation[2], "+22.15E"))
        return s
