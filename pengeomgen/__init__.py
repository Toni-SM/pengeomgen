
__author__ = "Antonio Serrano"
__email__ = "toni.sm91@gmail.com"
__version__ = "0.0.1"
__license__ = "MIT License"

__all__ = ["GeometryDefinition"]

# PENGEOM GEOMETRY-DEFINITION

class End():
    def __str__(self):
        """
        0000000000000000000000000000000000000000000000000000000000000000
        END      0000000000000000000000000000000000000000000000000000000
        """
        s="0000000000000000000000000000000000000000000000000000000000000000\n"
        s+="END      0000000000000000000000000000000000000000000000000000000"
        return s
        
class Include():
    def __init__(self, filename, starred=False, comment=""):
        self.comment=comment
        self.filename=filename
        self.starred=starred
        
    def __str__(self):
        """
        0000000000000000000000000000000000000000000000000000000000000000
        INCLUDE
           FILE=(filename.ext)
        """
        s="0000000000000000000000000000000000000000000000000000000000000000\n"
        s+="INCLUDE{0} {1}\n".format("*" if self.starred else " ", self.comment)
        s+="   FILE={0}".format(self.filename)
        return s

class Surface():
    def __init__(self, label, indices=(1,1,1,1,1), scale=(1,1,1), rotation=(0,0,0), translation=(0,0,0), starred=False, comment="", **kwargs):
        self.comment=comment
        self.label=("    "+label.upper())[-4:]
        self.starred=starred
        self.indices=indices
        self.scale=scale
        self.rotation=rotation
        self.translation=translation
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
        # single parameters
        self.xscale=kwargs.get("xscale", None)
        self.yscale=kwargs.get("yscale", None)
        self.zscale=kwargs.get("zscale", None)
        self.omega=kwargs.get("omega", None)
        self.theta=kwargs.get("theta", None)
        self.phi=kwargs.get("phi", None)
        self.xshift=kwargs.get("xshift", None)
        self.yshift=kwargs.get("yshift", None)
        self.zshift=kwargs.get("zshift", None)

    def __str__(self):
        """
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
        """
        s="0000000000000000000000000000000000000000000000000000000000000000\n"
        s+="SURFACE{0}({1}) {2}\n".format("*" if self.starred else " ", self.label, self.comment)
        s+="INDICES=({0})".format(",".join([str(i) if i<0 else " "+str(i) for i in self.indices]))
        # reduced form
        if self.indices!=(0,0,0,0,0):
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
                s+="\n     A0=({0},   0)".format(format(self.A0, "+22.15E"))
            # rotation and translation
            if self.rotation!=(0,0,0) or self.translation!=(0,0,0):
                s+="\n1111111111111111111111111111111111111111111111111111111111111111"
        # rotation
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
        # translation
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

class Body():
    def __init__(self, label, material, surfaces=[], bodies=[], modules=[], comment=""):
        self.comment=comment
        self.label=("    "+label.upper())[-4:]
        self.material=("    "+str(material).upper())[-4:]
        self.surfaces=surfaces
        self.bodies=bodies
        self.modules=modules

    def __str__(self):
        """
        0000000000000000000000000000000000000000000000000000000000000000
        BODY    (    ) text
        MATERIAL(    )
        SURFACE (    ), SIDE POINTER=( 1)
        BODY    (    )
        MODULE  (    )
        """
        s="0000000000000000000000000000000000000000000000000000000000000000\n"
        s+="BODY    ({0}) {1}\n".format(self.label, self.comment)
        s+="MATERIAL({0})".format(self.material)
        # surfaces
        for surface in self.surfaces:
            s+="\nSURFACE ({0}), SIDE POINTER=({1})".format(("    "+surface[0].upper())[-4:], str(surface[1]) if surface[1]<0 else " "+str(surface[1]))
        # bodies
        for body in self.bodies:
            s+="\nBODY    ({0})".format(("    "+body.upper())[-4:])
        # modules
        for module in self.modules:
            s+="\nMODULE  ({0})".format(("    "+module.upper())[-4:])
        return s

class Module():
    def __init__(self, label, material, surfaces=[], bodies=[], modules=[], rotation=(0,0,0), translation=(0,0,0), comment="", **kwargs):
        self.comment=comment
        self.label=("    "+label.upper())[-4:]
        self.material=("    "+str(material).upper())[-4:]
        self.surfaces=surfaces
        self.bodies=bodies
        self.modules=modules
        self.rotation=rotation
        self.translation=translation
        # single parameters
        self.omega=kwargs.get("omega", None)
        self.theta=kwargs.get("theta", None)
        self.phi=kwargs.get("phi", None)
        self.xshift=kwargs.get("xshift", None)
        self.yshift=kwargs.get("yshift", None)
        self.zshift=kwargs.get("zshift", None)

    def __str__(self):
        """
        0000000000000000000000000000000000000000000000000000000000000000
        MODULE  (    ) text
        MATERIAL(    )
        SURFACE (    ), SIDE POINTER=( 1)
        BODY    (    )
        MODULE  (    )
        1111111111111111111111111111111111111111111111111111111111111111
          OMEGA=(+0.000000000000000E+00,   0) DEG (DEFAULT=0.0)
          THETA=(+0.000000000000000E+00,   0) DEG (DEFAULT=0.0)
            PHI=(+0.000000000000000E+00,   0) RAD (DEFAULT=0.0)
        X-SHIFT=(+0.000000000000000E+00,   0) (DEFAULT=0.0)
        Y-SHIFT=(+0.000000000000000E+00,   0) (DEFAULT=0.0)
        Z-SHIFT=(+0.000000000000000E+00,   0) (DEFAULT=0.0)
        """
        s="0000000000000000000000000000000000000000000000000000000000000000\n"
        s+="MODULE  ({0}) {1}\n".format(self.label, self.comment)
        s+="MATERIAL({0})".format(self.material)
        # surfaces
        for surface in self.surfaces:
            s+="\nSURFACE ({0}), SIDE POINTER=({1})".format(("    "+surface[0].upper())[-4:], str(surface[1]) if surface[1]<0 else " "+str(surface[1]))
        # bodies
        for body in self.bodies:
            s+="\nBODY    ({0})".format(("    "+body.upper())[-4:])
        # modules
        for module in self.modules:
            s+="\nMODULE  ({0})".format(("    "+module.upper())[-4:])    
        # rotation and translation
        if self.rotation!=(0,0,0) or self.translation!=(0,0,0):   
            s+="\n1111111111111111111111111111111111111111111111111111111111111111"
            # rotation
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
            # translation
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

class Clone():
    def __init__(self, label, module, rotation=(0,0,0), translation=(0,0,0), comment="", **kwargs):
        self.comment=comment
        self.label=("    "+label.upper())[-4:]
        self.module=("    "+module.upper())[-4:]
        self.rotation=rotation
        self.translation=translation
        # single parameters
        self.omega=kwargs.get("omega", None)
        self.theta=kwargs.get("theta", None)
        self.phi=kwargs.get("phi", None)
        self.xshift=kwargs.get("xshift", None)
        self.yshift=kwargs.get("yshift", None)
        self.zshift=kwargs.get("zshift", None)

    def __str__(self):
        """
        0000000000000000000000000000000000000000000000000000000000000000
        CLONE   (    ) copies one module and moves it
        MODULE  (    ) original module
        1111111111111111111111111111111111111111111111111111111111111111
          OMEGA=(+0.000000000000000E+00,   0) DEG (DEFAULT=0.0)
          THETA=(+0.000000000000000E+00,   0) DEG (DEFAULT=0.0)
            PHI=(+0.000000000000000E+00,   0) RAD (DEFAULT=0.0)
        X-SHIFT=(+0.000000000000000E+00,   0) (DEFAULT=0.0)
        Y-SHIFT=(+0.000000000000000E+00,   0) (DEFAULT=0.0)
        Z-SHIFT=(+0.000000000000000E+00,   0) (DEFAULT=0.0)
        """
        s="0000000000000000000000000000000000000000000000000000000000000000\n"
        s+="CLONE   ({0}) {1}\n".format(self.label, self.comment)
        s+="MODULE  ({0})".format(self.module)
        # rotation and translation
        if self.rotation!=(0,0,0) or self.translation!=(0,0,0):
            s+="\n1111111111111111111111111111111111111111111111111111111111111111"
            # rotation
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
            # translation
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


# GEOMETRY-DEFINITION MANAGER

class GeometryDefinition():
    def __init__(self, description=""):
        self.definition=[]
        self.description=description
 
    # surfaces
    def surface(self, label, indices=(1,1,1,1,1), scale=(1,1,1), rotation=(0,0,0), translation=(0,0,0), 
                    starred=False, comment="", **kwargs):
        self.definition.append(Surface(label, indices, scale, rotation, translation, starred, comment, **kwargs))
        
    def surface_implicit_form(self, label, indices=(0,0,0,0,0), scale=(1,1,1), rotation=(0,0,0), translation=(0,0,0), 
                                  starred=False, comment="", **kwargs):
        self.definition.append(Surface(label, indices, scale, rotation, translation, starred, comment, **kwargs))

    def surface_plane(self, label, indices=(0,0,0,1,-1), scale=(1,1,1), rotation=(0,0,0), translation=(0,0,0), 
                          starred=False, comment="", **kwargs):
        self.definition.append(Surface(label, indices, scale, rotation, translation, starred, comment, **kwargs))
            
    def surface_sphere(self, label, indices=(1,1,1,0,-1), scale=(1,1,1), rotation=(0,0,0), translation=(0,0,0), 
                           starred=False, comment="", **kwargs):
        self.definition.append(Surface(label, indices, scale, rotation, translation, starred, comment, **kwargs))

    def surface_cylinder(self, label, indices=(1,1,0,0,-1), scale=(1,1,1), rotation=(0,0,0), translation=(0,0,0), 
                             starred=False, comment="", **kwargs):
        self.definition.append(Surface(label, indices, scale, rotation, translation, starred, comment, **kwargs))
            
    def surface_hyperbolic_cylinder(self, label, indices=(1,-1,0,0,-1), scale=(1,1,1), rotation=(0,0,0), translation=(0,0,0), 
                                        starred=False, comment="", **kwargs):
        self.definition.append(Surface(label, indices, scale, rotation, translation, starred, comment, **kwargs))
            
    def surface_cone(self, label, indices=(1,1,-1,0,0), scale=(1,1,1), rotation=(0,0,0), translation=(0,0,0), 
                         starred=False, comment="", **kwargs):
        self.definition.append(Surface(label, indices, scale, rotation, translation, starred, comment, **kwargs))

    def surface_one_sheet_hyperboloid(self, label, indices=(1,1,-1,0,-1), scale=(1,1,1), rotation=(0,0,0), translation=(0,0,0), 
                                        starred=False, comment="", **kwargs):
        self.definition.append(Surface(label, indices, scale, rotation, translation, starred, comment, **kwargs))
            
    def surface_two_sheet_hyperboloid(self, label, indices=(1,1,-1,0,1), scale=(1,1,1), rotation=(0,0,0), translation=(0,0,0), 
                                          starred=False, comment="", **kwargs):
        self.definition.append(Surface(label, indices, scale, rotation, translation, starred, comment, **kwargs))

    def surface_paraboloid(self, label, indices=(1,1,0,-1,0), scale=(1,1,1), rotation=(0,0,0), translation=(0,0,0), 
                               starred=False, comment="", **kwargs):
        self.definition.append(Surface(label, indices, scale, rotation, translation, starred, comment, **kwargs))
            
    def surface_parabolic_cylinder(self, label, indices=(1,0,0,-1,0), scale=(1,1,1), rotation=(0,0,0), translation=(0,0,0), 
                                       starred=False, comment="", **kwargs):
        self.definition.append(Surface(label, indices, scale, rotation, translation, starred, comment, **kwargs))
            
    def surface_hyperbolic_paraboloid(self, label, indices=(1,-1,0,-1,0), scale=(1,1,1), rotation=(0,0,0), translation=(0,0,0), 
                                          starred=False, comment="", **kwargs):  
        self.definition.append(Surface(label, indices, scale, rotation, translation, starred, comment, **kwargs))

    # body
    def body(self, label, material, surfaces=[], bodies=[], modules=[], comment=""):
        self.definition.append(Body(label, material, surfaces, bodies, modules, comment))

    # module
    def module(self, label, material, surfaces=[], bodies=[], modules=[], rotation=(0,0,0), translation=(0,0,0), comment="", **kwargs):
        self.definition.append(Module(label, material, surfaces, bodies, modules, rotation, translation, comment, **kwargs))
        
    # clone
    def clone(self, label, module, rotation=(0,0,0), translation=(0,0,0), comment="", **kwargs):
        self.definition.append(Clone(label, module, rotation, translation, comment, **kwargs))
    
    # include
    def include(self, filename, starred=False, comment=""):
        self.definition.append(Include(filename, starred, comment))
        
    # end
    def end(self):
        self.definition.append(End())
        
    def export_definition(self, filename):
        with open(file=filename, mode='w') as file_object:
            s=""
            if self.description:
                s="\n"+self.description+"\n"
            for definition in self.definition:
                s+="\n"+str(definition)
            try:
                if type(self.definition[-1])!=End:
                    s+="\n"+str(End())
                s+="\n"
            except IndexError:
                s="EMPTY GEOMETRY-DEFINITION"
            file_object.write(s)
        
    def __str__(self):
        s=""
        if self.description:
            s="\n"+self.description+"\n"
        for definition in self.definition:
            s+="\n"+str(definition)
        try:
            if type(self.definition[-1])!=End:
                s+="\n"+str(End())
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
    g.body("B4", 0, surfaces=[("S5",-1), ("S6", 1), ("S11",-1)], comment="foot hole")
    g.body("B5", 2, surfaces=[("S4",-1), ("S6", 1), ("S10",-1)], bodies=["B3", "B4"], comment="foot body")
    
    print(g)
    g.export_definition("glass")
    