
__author__ = "Antonio Serrano"
__email__ = "toni.sm91@gmail.com"
__version__ = "0.0.2"
__license__ = "MIT License"

__all__ = ["GeometryDefinition"]


import blocks

# GEOMETRY-DEFINITION MANAGER

class GeometryDefinition():
    def __init__(self, description=""):
        self.definition=[]
        self.description=description
        self.void_inner_volume_factor=1
 
    # surfaces
    def surface(self, label, indices=(1,1,1,1,1), starred=False, comment="", **kwargs):
        self.definition.append(blocks.Surface(label, indices, starred, comment, **kwargs))
        return self.definition[-1]
        
    def surface_implicit_form(self, label, indices=(0,0,0,0,0), starred=False, comment="", **kwargs):
        self.definition.append(blocks.Surface(label, indices, starred, comment, **kwargs))
        return self.definition[-1]

    def surface_plane(self, label, indices=(0,0,0,1,-1), starred=False, comment="", **kwargs):
        self.definition.append(blocks.Surface(label, indices, starred, comment, **kwargs))
        return self.definition[-1]
            
    def surface_sphere(self, label, indices=(1,1,1,0,-1), starred=False, comment="", **kwargs):
        self.definition.append(blocks.Surface(label, indices, starred, comment, **kwargs))
        return self.definition[-1]

    def surface_cylinder(self, label, indices=(1,1,0,0,-1), starred=False, comment="", **kwargs):
        self.definition.append(blocks.Surface(label, indices, starred, comment, **kwargs))
        return self.definition[-1]
            
    def surface_hyperbolic_cylinder(self, label, indices=(1,-1,0,0,-1), starred=False, comment="", **kwargs):
        self.definition.append(blocks.Surface(label, indices, starred, comment, **kwargs))
        return self.definition[-1]
            
    def surface_cone(self, label, indices=(1,1,-1,0,0), starred=False, comment="", **kwargs):
        self.definition.append(blocks.Surface(label, indices, starred, comment, **kwargs))
        return self.definition[-1]

    def surface_one_sheet_hyperboloid(self, label, indices=(1,1,-1,0,-1), starred=False, comment="", **kwargs):
        self.definition.append(blocks.Surface(label, indices, starred, comment, **kwargs))
        return self.definition[-1]
            
    def surface_two_sheet_hyperboloid(self, label, indices=(1,1,-1,0,1), starred=False, comment="", **kwargs):
        self.definition.append(blocks.Surface(label, indices, starred, comment, **kwargs))
        return self.definition[-1]

    def surface_paraboloid(self, label, indices=(1,1,0,-1,0), starred=False, comment="", **kwargs):
        self.definition.append(blocks.Surface(label, indices, starred, comment, **kwargs))
        return self.definition[-1]
            
    def surface_parabolic_cylinder(self, label, indices=(1,0,0,-1,0), starred=False, comment="", **kwargs):
        self.definition.append(blocks.Surface(label, indices, starred, comment, **kwargs))
        return self.definition[-1]
            
    def surface_hyperbolic_paraboloid(self, label, indices=(1,-1,0,-1,0), starred=False, comment="", **kwargs):  
        self.definition.append(blocks.Surface(label, indices, starred, comment, **kwargs))
        return self.definition[-1]

    # body
    def body(self, label, material, comment="", **kwargs):
        self.definition.append(blocks.Body(label, material, comment, **kwargs))
        return self.definition[-1]

    # module
    def module(self, label, material, comment="", **kwargs):
        self.definition.append(blocks.Module(label, material, comment, **kwargs))
        return self.definition[-1]
        
    # clone
    def clone(self, label, module, comment="", **kwargs):
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
        
    def show_void_inner_volumes(self, status=True):
        if status:
            self.void_inner_volume_factor=-1
        else:
            self.void_inner_volume_factor=1
        
    def __str__(self):
        s=""
        if self.description:
            s="\n"+self.description+"\n"
        for definition in self.definition:
            s+="\n"+str(definition)
        try:
            if type(self.definition[-1])!=blocks.End:
                s+="\n"+str(blocks.End())
        except IndexError:
            return ""
        return s




if __name__=="__main__":
    
    g=GeometryDefinition("The pythonic champagne glass")
    
    s1=g.surface("S1", starred=True)
    s2=g.surface("S2", indices=(1,0,1,0,1), scale=(2,3,4), rotation=(5,6,7), translation=(8,9,1))
    s3=g.surface("S3", indices=(1,0,1,0,1), xscale=20, yscale=30, zscale=40, omega=50, theta=60, phi=70, xshift=80, yshift=90, zshift=100, angle="rad")
    
    b1=g.body("B1", 1, comment="body number 1")
    b2=g.body("B2", 2, surfaces=[("S1", 1), ("S2", -1)], bodies=["B1"], modules=["M1"], comment="body number 2")
    
    m1=g.module("M1", 3, surfaces=[("S1", 1), ("S2", -1), ("S3", 1)], bodies=["B2"], modules=["M2"], scale=(2,3,4), rotation=(5,6,7), translation=(8,9,1), angle="rad", comment="module number 1")
    m2=g.module("M2", 4, surfaces=[("S1", 1), ("S2", -1), ("S3", 1)], bodies=["B2"], modules=["M2"], xscale=20, yscale=30, zscale=40, omega=50, theta=60, phi=70, xshift=80, yshift=90, zshift=100, comment="module number 2")
    m3=g.module("M3", 5, comment="module number 3")
    
    c1=g.clone("C1", "M1", comment="clone number 1")
    c2=g.clone("C2", "M2", scale=(2,3,4), rotation=(5,6,7), translation=(8,9,1), comment="clone number 2")
    c3=g.clone("C1", "M3", xscale=20, yscale=30, zscale=40, omega=50, theta=60, phi=70, xshift=80, yshift=90, zshift=100, angle="rad", comment="clone number 3")
    
    f1=g.include("filename1.test", comment="non starred file")
    f2=g.include("filename2.test", starred=True, comment="starred file")
    
    e=g.end()
    
    print(g)
    g.export_definition("test")
    