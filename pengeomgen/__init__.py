
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
        
    def surface_implicit_form(self, label, indices=(0,0,0,0,0), starred=False, comment="", **kwargs):
        self.definition.append(blocks.Surface(label, indices, starred, comment, **kwargs))

    def surface_plane(self, label, indices=(0,0,0,1,-1), starred=False, comment="", **kwargs):
        self.definition.append(blocks.Surface(label, indices, starred, comment, **kwargs))
            
    def surface_sphere(self, label, indices=(1,1,1,0,-1), starred=False, comment="", **kwargs):
        self.definition.append(blocks.Surface(label, indices, starred, comment, **kwargs))

    def surface_cylinder(self, label, indices=(1,1,0,0,-1), starred=False, comment="", **kwargs):
        self.definition.append(blocks.Surface(label, indices, starred, comment, **kwargs))
            
    def surface_hyperbolic_cylinder(self, label, indices=(1,-1,0,0,-1), starred=False, comment="", **kwargs):
        self.definition.append(blocks.Surface(label, indices, starred, comment, **kwargs))
            
    def surface_cone(self, label, indices=(1,1,-1,0,0), starred=False, comment="", **kwargs):
        self.definition.append(blocks.Surface(label, indices, starred, comment, **kwargs))

    def surface_one_sheet_hyperboloid(self, label, indices=(1,1,-1,0,-1), starred=False, comment="", **kwargs):
        self.definition.append(blocks.Surface(label, indices, starred, comment, **kwargs))
            
    def surface_two_sheet_hyperboloid(self, label, indices=(1,1,-1,0,1), starred=False, comment="", **kwargs):
        self.definition.append(blocks.Surface(label, indices, starred, comment, **kwargs))

    def surface_paraboloid(self, label, indices=(1,1,0,-1,0), starred=False, comment="", **kwargs):
        self.definition.append(blocks.Surface(label, indices, starred, comment, **kwargs))
            
    def surface_parabolic_cylinder(self, label, indices=(1,0,0,-1,0), starred=False, comment="", **kwargs):
        self.definition.append(blocks.Surface(label, indices, starred, comment, **kwargs))
            
    def surface_hyperbolic_paraboloid(self, label, indices=(1,-1,0,-1,0), starred=False, comment="", **kwargs):  
        self.definition.append(blocks.Surface(label, indices, starred, comment, **kwargs))

    # body
    def body(self, label, material, surfaces=[], bodies=[], modules=[], comment="", **kwargs):
        self.definition.append(blocks.Body(label, material, surfaces, bodies, modules, comment, **kwargs))

    # module
    def module(self, label, material, surfaces=[], bodies=[], modules=[], comment="", **kwargs):
        self.definition.append(blocks.Module(label, material, surfaces, bodies, modules, comment, **kwargs))
        
    # clone
    def clone(self, label, module, comment="", **kwargs):
        self.definition.append(blocks.Clone(label, module, comment, **kwargs))
    
    # include
    def include(self, filename, starred=False, comment=""):
        self.definition.append(blocks.Include(filename, starred, comment))
        
    # end
    def end(self):
        self.definition.append(blocks.End())
        
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
    
    g.surface_plane("S1", zscale=9)
    g.surface_plane("S2", zscale=7)
    g.surface("S4", indices=( 0, 0, 0, 1, 0), zshift=-6)
    g.surface("S5", indices=( 0, 0, 0, 1, 0), zshift=-6.4)
    g.surface("S6", indices=( 0, 0, 0, 1, 0), zshift=-6.8)

    g.surface_paraboloid("S7")
    g.surface_paraboloid("S8", scale=(0.98, 0.98, 1), translation=(0, 0, 0.35))

    g.surface_cone("S9", scale=(0.012, 0.012, 1), translation=(0, 0, -20))
    g.surface_cone("S10", scale=(3.7, 3.7, 1), translation=(0, 0, -6))
    g.surface_cone("S11", scale=(5.1, 5.1, 1), translation=(0, 0, -6.35))

    g.body("B1", 2, surfaces=[("S1",-1), ("S7",-1), ("S8", 1)], comment="cup body")
    g.body("B2", 1, surfaces=[("S8",-1), ("S2",-1)], comment="liquid")
    g.body("B3", 2, surfaces=[("S5", 1), ("S9",-1), ("S7", 1)], comment="trunk")
    g.body("B4", -10, surfaces=[("S5",-1), ("S6", 1), ("S11",-1)], comment="foot hole")
    g.body("B5", 2, surfaces=[("S4",-1), ("S6", 1), ("S10",-1)], bodies=["B3", "B4"], comment="foot body")
    g.body("B5", 2, surfaces=[("S4",-1), ("S6", 1), ("S10",-1)], bodies=["B3", "B4"], comment="foot body")
    
    g.end()
    g.include("lorem.ipsum", True, "test")
    
    g.body("B5", 2, surfaces=[("S4",-1), ("S6", 1), ("S10",-1)], bodies=["B3", "B4"], comment="foot body", translation=(0, 0, -6))
    g.module("B5", 2, surfaces=[("S4",-1), ("S6", 1), ("S10",-1)], bodies=["B3", "B4"], comment="foot body", xshift=10)
    
    g.clone("A", "B", phi=20)
    
    g.show_void_inner_volumes(True)
    
    print(g)
    g.export_definition("test")
    