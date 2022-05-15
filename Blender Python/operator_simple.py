import bpy
# you can import just the part of the library required
from math import radians
from bpy.props import *
# remove this and others
#def main(context):
#    for ob in context.scene.objects:
#        print(ob)

#renamed class and idname
class MyOperator(bpy.types.Operator):
    bl_idname = "object.my_operator"
    bl_label = "My Operator"
    bl_options = {'REGISTER', 'UNDO'}


    #create properties
    noise_scale : FloatProperty(
        name = "Noise Scale",
        description = "Any description",
        default = 1.0,
        min = 0.0,
        max = 2.0
    )
    #@classmethod
    #def poll(cls, context):
    #    return context.active_object is not None

    def execute(self, context):
        #        main(context)
        #        everything is packaged in here`My

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

        #creat displacement modifier
        mod_displace = so.modifiers.new("My Displacement", 'DISPLACE')

        #create the texture
        #https://docs.blender.org/api/current/bpy.types.Texture.html
        new_tex = bpy.data.textures.new("My Texture", 'DISTORTED_NOISE')

        #change the texture settings - value replaced with property
        new_tex.noise_scale = self.noise_scale 

        #assign the texture to the displacement modifier
        mod_displace.texture = new_tex

        #create the material, note the 'name = ' is just being specific on what you are setting
        new_mat = bpy.data.materials.new(name = "My Material")

        #add material to selected object
        so.data.materials.append(new_mat)

        new_mat.use_nodes = True

        nodes = new_mat.node_tree.nodes

        material_output = nodes.get("Material Output")

        node_emission = nodes.new(type='ShaderNodeEmission')

        #The outup and inputs of material node blocks are arrays
        #with zero being the top input/output and counting up from there

        #set color value, input 0, of the emission shader node to cyan
        #note the last number is the output
        node_emission.inputs[0].default_value = ( 0.0, 0.3, 1.0, 1)

        #increase the strength or intensity of the color
        node_emission.inputs[1].default_value = 500.0

        #link the them together
        links = new_mat.node_tree.links
        new_link = links.new(node_emission.outputs[0], material_output.inputs[0])

        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(MyOperator.bl_idname, text=MyOperator.bl_label)

# Register and add to the "object" menu (required to also use F3 search "Simple Object Operator" for quick access)
def register():
    bpy.utils.register_class(MyOperator)
    bpy.types.VIEW3D_MT_object.append(menu_func)


def unregister():
    bpy.utils.unregister_class(MyOperator)
    bpy.types.VIEW3D_MT_object.remove(menu_func)


if __name__ == "__main__":
    register()

    # test call with rename
    bpy.ops.object.my_operator()
