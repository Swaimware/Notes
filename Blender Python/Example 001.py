import bby
from math import radians

#create cube and store its name to variable
bpy.ops.mesh.primitive_cube_add()
so = bpy.context.active_object

#move cube 5 units X [0]=X [1]=Y [2]=X
so.location[0] = 5