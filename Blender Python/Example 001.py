#in preferences you can turn on python tool tips
#then when you hover over items in UI it will show
#the python required to run that

import bby
# you can import just the part of the library required
from math import radians

#create cube and store its name to variable
bpy.ops.mesh.primitive_cube_add()
so = bpy.context.active_object

#move cube 5 units X [0]=X [1]=Y [2]=X
so.location[0] = 5

#rotate about the x axis 45 degrees
#must specify rotation in radians thus the conversion
so.rotation_euler[0] += radians(45)

#in the console you can look at all of the items you
#can look at all of actions that can be done with the 
#active so.  If you make an object active then type
#so = byp.context.active_object
#so.     then press tab the console will give intelisense
#this works in the console after any dot just press tab

#add subsurface modifer to active object
so.modifiers.new("My Modifier", 'SUBSURF')

#change number of viewport to 3 increasing subdivision
so.modifiers["My Modifier"].levels = 3

#or you could save subsurface modifier in a variable
mod_subsur = so.modifiers.new("My Modifier", 'SUBSURF')

mod_subsur.levels = 3

#you can use the blender scripting output window to discover commands
#for example if you select the above, right click, and choose smooth
#the output shows you the below

#smooth the active object
bpy.ops.object.shade_smooth()

#another way to smooth is for loop through all of the active objects polygons
mesh= so.data
for face in mesh.polygons:
        face.use_smooth = True

#creat displacement modifier
mod_displace = so.modifiers.new("My Displacement", 'DISPLACE')

#create the texture
new_text = bpy.data.textures.new("My Texture", 'DISTORTED' )