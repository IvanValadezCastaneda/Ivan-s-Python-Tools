import bpy

def replace_string_in_object_names(input_string, replacement_string):
    for obj in bpy.data.objects:
        obj.name = obj.name.replace(input_string, replacement_string)

replace_string_in_object_names("í", "i")