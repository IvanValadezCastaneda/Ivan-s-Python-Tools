import bpy

title_name = "Luminaria"

for obj in bpy.data.objects:
    
    if obj.name.find(title_name) != -1:
     
        obj.select_set(True)
 
        bpy.ops.object.delete()

