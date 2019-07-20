# PENGEOMGEN

Python library for easy generation of PENELOPE PENGEOM geometry-definition file.

PENGEOM can describe any material system consisting of homogeneous bodies limited by quadric surfaces. Its geometry definition file is a strictly formatted text lines that define blocks of elements \[1\]. Write manually a geometry description file can be a long and hard task (for example, a medium complex material system may have thousands of very strictly formatted lines).

PenGeom.jar (a Java GUI application which is not part of the PENELOPE distribution package) allows the definition of the geometry and its visualization \[2\] through a visual interface.  

**pengeomgen** provide a simple, light and very customizable object-oriented API for create and export the strictly formatted geometry definition file for work with PENELOPE PENGEOM. A single class allows the definition of all basic and others predefined elements.
 
References:

> \[1\] F. Salvat. *PENELOPE, a code system for Monte Carlo simulation of electron and photon transport*. Workshop Proceedings, Barcelona, Spain. NEA/MBDAV/R(2019)1.

> \[2\] Almansa, J., F. Salvat-Pujol, G. Díaz-Londoño, A. Carnicer, A. M. Lallena, and F. Salvat. *PENGEOM, A general-purpose geometry package for Monte Carlo simulation of radiation transport in complex material structures*. Comput. Phys. Commun. 199. (2016).

## Setup

```bash
$ pip3 install pengeomgen
```

## Example of usage

```python
import pengeomgen

g=pengeomgen.GeometryDefinition("The pythonic champagne glass")
    
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

# export the geometry definition file
g.export_definition("glass")
```

## Usage and API

The main name provided by the pengeomgen package is **GeometryDefinition**. This is a class name for manage the block of elements in a geometry definition file. Through its interface (methods), we can define surfaces, bodies, modules using easy numeric notation and others features. Also, we can do operations like: clone, include external geometry definition, etc. 

```python
import pengeomgen

g=pengeomgen.GeometryDefinition("optional text description")
```

For export the constructed geometry definition to a file, we can call the **export_definition** method. This method has as only parameter the absolute or relative path of the output file. 

```python
g.export_definition("output_file_path")
```

The methods for describe a material system using quadric surfaces, bodies and modules and make others operations are detailed in the next sections.

### Surfaces

The method **surface** allows the creation of quadric surfaces (reduced form by default) according to the next formatted text lines for the reduced form and implicit form respectively.

Reduced form:
```
0000000000000000000000000000000000000000000000000000000000000000
SURFACE (  A4) comment: reduced form
INDICES=(I2,I2,I2,I2,I2)
X-SCALE=(         E22.15       ,  I4) (DEFAULT=1.0)
Y-SCALE=(         E22.15       ,  I4) (DEFAULT=1.0)
Z-SCALE=(         E22.15       ,  I4) (DEFAULT=1.0)
  OMEGA=(         E22.15       ,  I4) DEG (DEFAULT=0.0)
  THETA=(         E22.15       ,  I4) DEG (DEFAULT=0.0)
    PHI=(         E22.15       ,  I4) DEG (DEFAULT=0.0)
X-SHIFT=(         E22.15       ,  I4) (DEFAULT=0.0)
Y-SHIFT=(         E22.15       ,  I4) (DEFAULT=0.0)
Z-SHIFT=(         E22.15       ,  I4) (DEFAULT=0.0)
```

Implicit form:
```
0000000000000000000000000000000000000000000000000000000000000000
SURFACE (  A4) comment: implicit form
INDICES=( 0, 0, 0, 0, 0)
    AXX=(         E22.15       ,  I4) (DEFAULT=0.0)
    AXY=(         E22.15       ,  I4) (DEFAULT=0.0)
    AXZ=(         E22.15       ,  I4) (DEFAULT=0.0)
    AYY=(         E22.15       ,  I4) (DEFAULT=0.0)
    AYZ=(         E22.15       ,  I4) (DEFAULT=0.0)
    AZZ=(         E22.15       ,  I4) (DEFAULT=0.0)
     AX=(         E22.15       ,  I4) (DEFAULT=0.0)
     AY=(         E22.15       ,  I4) (DEFAULT=0.0)
     AZ=(         E22.15       ,  I4) (DEFAULT=0.0)
     A0=(         E22.15       ,  I4) (DEFAULT=0.0)
1111111111111111111111111111111111111111111111111111111111111111
  OMEGA=(         E22.15       ,  I4) DEG (DEFAULT=0.0)
  THETA=(         E22.15       ,  I4) DEG (DEFAULT=0.0)
    PHI=(         E22.15       ,  I4) DEG (DEFAULT=0.0)
X-SHIFT=(         E22.15       ,  I4) (DEFAULT=0.0)
Y-SHIFT=(         E22.15       ,  I4) (DEFAULT=0.0)
Z-SHIFT=(         E22.15       ,  I4) (DEFAULT=0.0)
```

Method and arguments:

```python
surface(label, indices=(1,1,1,1,1), scale=(1,1,1), 
        rotation=(0,0,0), translation=(0,0,0), starred=False, comment="", **kwargs)
```

* label (string): user label of the element (maximum 4 characters)
* indices (tuple): coefficients for the reduced form of the surface representation (I1, I2, I3, I4, I5)
* scale (tuple): scale factors for the X, Y and Z axes (X-SCALE, Y-SCALE, Z-SCALE) 
* rotation (tuple): rotation values defined through the Euler angles (OMEGA, THETA, PHI)
* translation (tuple): translation values for the X, Y and Z axes (X-SHIFT, Y-SHIFT, Z-SHIFT) 
* starred (boolean): if True its allow to define fixed surfaces, which will not be affected by possible translations or rotations in subsequent stages of the geometry definition
* comment (string): short text description

> Also, we can use the assignment of a single parameter for specify the value of one compressed item in the tuples referred to the scaling, rotation and translation. The single parameters are: xscale (X-SCALE), yscale (Y-SCALE), zscale (Z-SCALE), omega (OMEGA), theta (THETA), phi (PHI), xshift (X-SHIFT), yshift (Y-SHIFT) and zshift (Z-SHIFT). In that case, the value of the single parameter overwrites the value of its respective item in the tuple, when both parameters are present.

Custom surfaces:

For grant an easy, agile and fast construction of the geometry definitions of a material system the class GeometryDefinition includes several methods that map custom and predefined reduced quadric surfaces. These surfaces are defined in the next table, with its coefficients and its method names respectively. All methods are reimplementation of the generic **surface** method, they just set the value of the coefficients (indices) according to the representation.

Surface               | Coefficients     | Method of the class (API)
--------------------- | ---------------- | -----------------------------
Plane                 | ( 0, 0, 0, 1,-1) | surface_plane
Sphere                | ( 1, 1, 1, 0,-1) | surface_sphere
Cylinder              | ( 1, 1, 0, 0,-1) | surface_cylinder
Hyperbolic cylinder   | ( 1,-1, 0, 0,-1) | surface_hyperbolic_cylinder
Cone                  | ( 1, 1,-1, 0, 0) | surface_cone
One sheet hyperboloid | ( 1, 1,-1, 0,-1) | surface_one_sheet_hyperboloid
Two sheet hyperboloid | ( 1, 1,-1, 0, 1) | surface_two_sheet_hyperboloid
Paraboloid            | ( 1, 1, 0,-1, 0) | surface_paraboloid
Parabolic cylinder    | ( 1, 0, 0,-1, 0) | surface_parabolic_cylinder
Hyperbolic paraboloid | ( 1,-1, 0,-1, 0) | surface_hyperbolic_paraboloid

Surfaces in implicit form:

We can use the method **surface** for create surfaces in implicit form setting all items of the tuple of the coefficients (indices) to zero. However, the method **surface_implicit_form** do this for us. There is a set of single parameters for specify the geometry of this surface: AXX, AXY, AXZ, AYY, AYZ, AZZ, AX, AY, AZ, A0 according to the model. We can set the useful values for our implementation; the others take as default value zero.

For this implementation, the values of the scale are ignored in anyone of this representation (tuple or single parameter).

### Body

The method **body** allows the creation of homogeneous bodies limited by quadric surfaces according to the next formatted text lines:

```
0000000000000000000000000000000000000000000000000000000000000000
BODY    (  A4) comment
MATERIAL(  A4)
SURFACE (  A4), SIDE POINTER=(I2)
BODY    (  A4)
MODULE  (  A4)
```

Method and arguments:

```python
body(label, material, surfaces=[], bodies=[], modules=[], comment="")
```
* label (string): user label of the element (maximum 4 characters)
* material (string or integer): number of the material identification conform with the convention adopted in the simulation
* surfaces (list of tuples): boundary surfaces of the current body. Each tuple contains the label of the boundary surface (string) and its surface side pointer (integer: 1 or -1)
* bodies (list of string): boundary bodies of the current body
* modules (list of string): boundary modules of the current body
* comment (string): short text description

### Module

The method **module** allows the creation of modules according to the next formatted text lines:

```
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
```

Method and arguments:

```python
module(label, material, surfaces=[], bodies=[], modules=[], 
       rotation=(0,0,0), translation=(0,0,0), comment="", **kwargs)
```
* label (string): user label of the element (maximum 4 characters)
* material (string or integer): number of the material identification conform with the convention adopted in the simulation
* surfaces (list of tuples): boundary surfaces of the current module. Each tuple contains the label of the boundary surface (string) and its surface side pointer (integer: 1 or -1)
* bodies (list of string): boundary bodies of the current module
* modules (list of string): boundary modules of the current module
* rotation (tuple): rotation values defined through the Euler angles (OMEGA, THETA, PHI)
* translation (tuple): translation values for the X, Y and Z axes (X-SHIFT, Y-SHIFT, Z-SHIFT) 
* comment (string): short text description

> Like the surfaces, we can use the assignment of a single parameter for specify the value of one compressed item in the tuples referred to the rotation and translation. The single parameters are: omega (OMEGA), theta (THETA), phi (PHI), xshift (X-SHIFT), yshift (Y-SHIFT) and zshift (Z-SHIFT). In that case, the value of the single parameter overwrites the value of its respective component in the tuple, when both parameters are present. 

### Clone

The method **clone** allows the conation of modules (bodies cannot be cloned; to clone a body that is limited only by surfaces, define it as a module) according to the next formatted text lines:

```
0000000000000000000000000000000000000000000000000000000000000000
CLONE   (  A4) copies one module and moves it
MODULE  (  A4) original module
1111111111111111111111111111111111111111111111111111111111111111
  OMEGA=(         E22.15       ,  I4) DEG (DEFAULT=0.0)
  THETA=(         E22.15       ,  I4) DEG (DEFAULT=0.0)
    PHI=(         E22.15       ,  I4) DEG (DEFAULT=0.0)
X-SHIFT=(         E22.15       ,  I4) (DEFAULT=0.0)
Y-SHIFT=(         E22.15       ,  I4) (DEFAULT=0.0)
Z-SHIFT=(         E22.15       ,  I4) (DEFAULT=0.0)
```

Method and arguments:

```python
clone(label, module, rotation=(0,0,0), translation=(0,0,0), comment="", **kwargs)
```
* label (string): user label of the element (maximum 4 characters)
* module (string): label of the module to be cloned (maximum 4 characters)
* rotation (tuple): rotation values defined through the Euler angles (OMEGA, THETA, PHI)
* translation (tuple): translation values for the X, Y and Z axes (X-SHIFT, Y-SHIFT, Z-SHIFT) 
* comment (string): short text description

> Like the surfaces and equal to modules, we can use the assignment of a single parameter for specify the value of one compressed item in the tuples referred to the rotation and translation. The single parameters are: omega (OMEGA), theta (THETA), phi (PHI), xshift (X-SHIFT), yshift (Y-SHIFT) and zshift (Z-SHIFT). In that case, the value of the single parameter overwrites the value of its respective component in the tuple, when both parameters are present. 

### Include

The method **include** allows the insertion of other geometry definition files according to the next formatted text lines:

```
0000000000000000000000000000000000000000000000000000000000000000
INCLUDE  comment
   FILE=(filename.ext)
```

Method and arguments:

```python
file(filename, starred=False, comment="")
```
* filename (string): absolute or relative path of the geometry definition file to be included
* starred (boolean): if True its allow the included file to be considered as if it were part of the main file
* comment (string): short text description

### End

The method **end** cancel the reading of geometry data for the PENELOPE PENGEOM application (if this method is called in the middle of a geometry definition of some material system, all elements after this call are ignored for the application). By default this generator includes this element at the end of the geometry definition, then, its call is not mandatory.

```
0000000000000000000000000000000000000000000000000000000000000000
END      0000000000000000000000000000000000000000000000000000000
```

Method and arguments:

```python
end()
```
