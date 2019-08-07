from abc import ABC, abstractmethod


class Base(ABC):
    def __init__(self, comment=""):
        self.comment=comment
        self.void_inner_volume_factor=1
        
    @abstractmethod
    def __str__(self):
        pass
    
    def set_void_inner_volume_factor(self, factor):
        self.void_inner_volume_factor=factor
      
      
class Element(Base):
    def __init__(self, label, comment="", **kwargs):
        super().__init__(comment)
        self.label=("    "+label)[-4:]
        
        # length unit
        self.unit_multiplication_factor=1
        self.unit=kwargs.get("unit", "cm").lower()
        self.compute_unit_multiplication_factor()
        
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

    def compute_unit_multiplication_factor(self):
        if self.unit.lower() in ["mm", "millimeter", "millimeters"]:
            self.unit_multiplication_factor=0.1
        elif self.unit.lower() in ["cm", "centimeter", "centimeters"]:
            self.unit_multiplication_factor=1
        elif self.unit.lower() in ["dm", "decimeter", "decimeters"]:
            self.unit_multiplication_factor=10
        elif self.unit.lower() in ["m", "meter", "meters"]:
            self.unit_multiplication_factor=100
        elif self.unit.lower() in ["in", "inch", "inches"]:
            self.unit_multiplication_factor=2.54
        elif self.unit.lower() in ["ft", "foot", "feet"]:
            self.unit_multiplication_factor=30.479
        
        
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
            s+="\nX-SHIFT=({0},   0)".format(format(self.translation[0]*self.unit_multiplication_factor, "+22.15E"))
        # shift y
        if self.translation[1]:
            s+="\nY-SHIFT=({0},   0)".format(format(self.translation[1]*self.unit_multiplication_factor, "+22.15E"))
        # shift z
        if self.translation[2]:
            s+="\nZ-SHIFT=({0},   0)".format(format(self.translation[2]*self.unit_multiplication_factor, "+22.15E"))
        return s


class AdvancedElement(Element):
    def __init__(self, label, material, comment="", **kwargs):
        super().__init__(label, comment, **kwargs)
        self.material=int(material)
        self.surfaces=kwargs.get("surfaces", [])
        self.bodies=kwargs.get("bodies", [])
        self.modules=kwargs.get("modules", [])
        
    @abstractmethod
    def __str__(self):
        pass
        
    def representation_elements(self):
        s=""
        for surface in self.surfaces:
            if issubclass(type(surface[0]), Base):
                s+="\nSURFACE ({0}), SIDE POINTER=({1})".format(surface[0].label, str(surface[1]) if surface[1]<0 else " "+str(surface[1]))
            else:
                s+="\nSURFACE ({0}), SIDE POINTER=({1})".format(("    "+surface[0])[-4:], str(surface[1]) if surface[1]<0 else " "+str(surface[1]))
        # bodies
        for body in self.bodies:
            if issubclass(type(body), Base):
                s+="\nBODY    ({0})".format(body.label)
            else:
                s+="\nBODY    ({0})".format(("    "+body)[-4:])
        # modules
        for module in self.modules:
            if issubclass(type(module), Base):
                s+="\nMODULE  ({0})".format(module.label)
            else:
                s+="\nMODULE  ({0})".format(("    "+module)[-4:])
        return s       
        