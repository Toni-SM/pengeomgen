
__author__ = "Antonio Serrano"
__email__ = "toni.sm91@gmail.com"
__version__ = "0.0.3"
__license__ = "MIT License"

__all__ = ["GeometryDefinition"]

import os
try:
    from . import blocks
except:
    import blocks

# GEOMETRY-DEFINITION MANAGER

class GeometryDefinition():
    def __init__(self, description="", unit="cm", angle="DEG"):
        self.definition=[]
        self.description=description
        self.unit=unit
        self.angle=angle
        self.void_inner_volume_factor=1
        
        self._sm_characters=[120, 97, 97, 96]
 
    # surfaces
    def surface(self, label=None, indices=(1,1,1,1,1), starred=False, comment="", **kwargs):
        kwargs["unit"]=kwargs.get("unit", self.unit)
        kwargs["angle"]=kwargs.get("angle", self.angle)
        if label is None:
            label=self._sm_label()
        self.definition.append(blocks.Surface(label, indices, starred, comment, **kwargs))
        return self.definition[-1]
        
    def surface_implicit_form(self, label=None, indices=(0,0,0,0,0), starred=False, comment="", **kwargs):
        kwargs["unit"]=kwargs.get("unit", self.unit)
        kwargs["angle"]=kwargs.get("angle", self.angle)
        if label is None:
            label=self._sm_label()
        self.definition.append(blocks.Surface(label, indices, starred, comment, **kwargs))
        return self.definition[-1]

    def surface_plane(self, label=None, indices=(0,0,0,1,0), starred=False, comment="", **kwargs):
        kwargs["unit"]=kwargs.get("unit", self.unit)
        kwargs["angle"]=kwargs.get("angle", self.angle)
        if label is None:
            label=self._sm_label()
        self.definition.append(blocks.Surface(label, indices, starred, comment, **kwargs))
        return self.definition[-1]
            
    def surface_sphere(self, label=None, indices=(1,1,1,0,-1), starred=False, comment="", **kwargs):
        kwargs["unit"]=kwargs.get("unit", self.unit)
        kwargs["angle"]=kwargs.get("angle", self.angle)
        if label is None:
            label=self._sm_label()
        self.definition.append(blocks.Surface(label, indices, starred, comment, **kwargs))
        return self.definition[-1]

    def surface_cylinder(self, label=None, indices=(1,1,0,0,-1), starred=False, comment="", **kwargs):
        kwargs["unit"]=kwargs.get("unit", self.unit)
        kwargs["angle"]=kwargs.get("angle", self.angle)
        if label is None:
            label=self._sm_label()
        self.definition.append(blocks.Surface(label, indices, starred, comment, **kwargs))
        return self.definition[-1]
            
    def surface_hyperbolic_cylinder(self, label=None, indices=(1,-1,0,0,-1), starred=False, comment="", **kwargs):
        kwargs["unit"]=kwargs.get("unit", self.unit)
        kwargs["angle"]=kwargs.get("angle", self.angle)
        if label is None:
            label=self._sm_label()
        self.definition.append(blocks.Surface(label, indices, starred, comment, **kwargs))
        return self.definition[-1]
            
    def surface_cone(self, label=None, indices=(1,1,-1,0,0), starred=False, comment="", **kwargs):
        kwargs["unit"]=kwargs.get("unit", self.unit)
        kwargs["angle"]=kwargs.get("angle", self.angle)
        if label is None:
            label=self._sm_label()
        self.definition.append(blocks.Surface(label, indices, starred, comment, **kwargs))
        return self.definition[-1]

    def surface_one_sheet_hyperboloid(self, label=None, indices=(1,1,-1,0,-1), starred=False, comment="", **kwargs):
        kwargs["unit"]=kwargs.get("unit", self.unit)
        kwargs["angle"]=kwargs.get("angle", self.angle)
        if label is None:
            label=self._sm_label()
        self.definition.append(blocks.Surface(label, indices, starred, comment, **kwargs))
        return self.definition[-1]
            
    def surface_two_sheet_hyperboloid(self, label=None, indices=(1,1,-1,0,1), starred=False, comment="", **kwargs):
        kwargs["unit"]=kwargs.get("unit", self.unit)
        kwargs["angle"]=kwargs.get("angle", self.angle)
        if label is None:
            label=self._sm_label()
        self.definition.append(blocks.Surface(label, indices, starred, comment, **kwargs))
        return self.definition[-1]

    def surface_paraboloid(self, label=None, indices=(1,1,0,-1,0), starred=False, comment="", **kwargs):
        kwargs["unit"]=kwargs.get("unit", self.unit)
        kwargs["angle"]=kwargs.get("angle", self.angle)
        if label is None:
            label=self._sm_label()
        self.definition.append(blocks.Surface(label, indices, starred, comment, **kwargs))
        return self.definition[-1]
            
    def surface_parabolic_cylinder(self, label=None, indices=(1,0,0,-1,0), starred=False, comment="", **kwargs):
        kwargs["unit"]=kwargs.get("unit", self.unit)
        kwargs["angle"]=kwargs.get("angle", self.angle)
        if label is None:
            label=self._sm_label()
        self.definition.append(blocks.Surface(label, indices, starred, comment, **kwargs))
        return self.definition[-1]
            
    def surface_hyperbolic_paraboloid(self, label=None, indices=(1,-1,0,-1,0), starred=False, comment="", **kwargs):  
        kwargs["unit"]=kwargs.get("unit", self.unit)
        kwargs["angle"]=kwargs.get("angle", self.angle)
        if label is None:
            label=self._sm_label()
        self.definition.append(blocks.Surface(label, indices, starred, comment, **kwargs))
        return self.definition[-1]

    # body
    def body(self, label=None, material=0, comment="", **kwargs):
        kwargs["unit"]=kwargs.get("unit", self.unit)
        kwargs["angle"]=kwargs.get("angle", self.angle)
        if label is None:
            label=self._sm_label()
        self.definition.append(blocks.Body(label, material, comment, **kwargs))
        return self.definition[-1]

    # module
    def module(self, label=None, material=0, comment="", **kwargs):
        kwargs["unit"]=kwargs.get("unit", self.unit)
        kwargs["angle"]=kwargs.get("angle", self.angle)
        if label is None:
            label=self._sm_label()
        self.definition.append(blocks.Module(label, material, comment, **kwargs))
        return self.definition[-1]
        
    # clone
    def clone(self, label=None, module="", comment="", **kwargs):
        kwargs["unit"]=kwargs.get("unit", self.unit)
        kwargs["angle"]=kwargs.get("angle", self.angle)
        if label is None:
            label=self._sm_label()
        self.definition.append(blocks.Clone(label, module, comment, **kwargs))
        return self.definition[-1]
    
    # include
    def include(self, filename, starred=False, comment=""):
        self.definition.append(blocks.Include(filename, starred, comment))
        return self.definition[-1]
        
    # end
    def end(self):
        self.definition.append(blocks.End())
        return self.definition[-1]
        
    def export_definition(self, filename):
        with open(file=filename, mode='w') as file_object:
            s=""
            if self.description:
                s="\n"+self.description+"\n"
            for definition in self.definition:
                definition.set_void_inner_volume_factor(self.void_inner_volume_factor)
                s+="\n"+str(definition)
            try:
                if type(self.definition[-1])!=blocks.End:
                    s+="\n"+str(blocks.End())
                s+="\n"
            except IndexError:
                s="EMPTY GEOMETRY-DEFINITION"
            file_object.write(s)
        
    def show_void_inner_volumes(self, show=True):
        if show:
            self.void_inner_volume_factor=-1
        else:
            self.void_inner_volume_factor=1

    def _sm_label(self):
        # 52728 labels from 'XAAA' to 'ZZZZ'
        self._sm_characters[3]+=1
        if self._sm_characters[3]>122:
            self._sm_characters[3]=97
            self._sm_characters[2]+=1
            if self._sm_characters[2]>122:
                self._sm_characters[2]=97
                self._sm_characters[1]+=1
                if self._sm_characters[1]>122:
                    self._sm_characters[1]=97
                    self._sm_characters[0]+=1
                    if self._sm_characters[0]>122:
                        self._sm_characters[0]=120
        return "".join([chr(c).upper() for c in self._sm_characters])
        
    def __str__(self):
        s=""
        if self.description:
            s="\n"+self.description+"\n"
        for definition in self.definition:
            definition.set_void_inner_volume_factor(self.void_inner_volume_factor)
            s+="\n"+str(definition)
        try:
            if type(self.definition[-1])!=blocks.End:
                s+="\n"+str(blocks.End())
        except IndexError:
            return ""
        return s




if __name__=="__main__":
    
    g=GeometryDefinition("The pythonic champagne glass", unit="inch", angle="rad")
    
    s1=g.surface(starred=True)
    s2=g.surface(indices=(1,0,1,0,1), scale=(2,3,4), rotation=(5,6,7), translation=(8,9,1))
    s3=g.surface(indices=(1,0,1,0,1), xscale=20, yscale=30, zscale=40, omega=50, theta=60, phi=70, xshift=80, yshift=90, zshift=100, angle="deg")
    
    b1=g.body("B1", material=-100, comment="body number 1")
    b2=g.body("B2", material=-200, surfaces=[(s1, 1), (s2, -1)], bodies=[b1], comment="body number 2")
    
    m1=g.module(material=3, surfaces=[(s1, 1), (s2, -1), (s3, 1)], bodies=["B2"], modules=["M2"], scale=(2,3,4), rotation=(5,6,7), translation=(8,9,1), angle="deg", comment="module number 1")
    m2=g.module("M2", material=4, surfaces=[(s1, 1), (s2, -1), (s3, 1)], bodies=[b2], modules=[m1], xscale=20, yscale=30, zscale=40, omega=50, theta=60, phi=70, xshift=80, yshift=90, zshift=100, comment="module number 2")
    m3=g.module("M3", material=5, comment="module number 3")
    
    c1=g.clone("C1", m1, comment="clone number 1")
    c2=g.clone("C2", m2, scale=(2,3,4), rotation=(5,6,7), translation=(8,9,1), comment="clone number 2")
    c3=g.clone("C3", "M3", xscale=20, yscale=30, zscale=40, omega=50, theta=60, phi=70, xshift=80, yshift=90, zshift=100, unit="cm", angle="rad", comment="clone number 3")
    
    f1=g.include("filename1.test", comment="non starred file")
    f2=g.include("filename2.test", starred=True, comment="starred file")
    
    e=g.end()
    
    g.show_void_inner_volumes(False)
    
    print(g)
    g.export_definition("test")
    