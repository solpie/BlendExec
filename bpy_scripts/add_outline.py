#[as_exec]
import bpy

#objs = bpy.context.selected_objects

for o in bpy.context.selected_objects:
    for m in o.modifiers:
        if m.type == 'SOLIDIFY' and m.material_offset > 0:
            continue
    m = o.modifiers.new('Solidify', 'SOLIDIFY')
    m.thickness = -0.001
    m.use_flip_normals = True
    
    if not any([mat for mat in o.data.materials if mat.name == 'Outline']):
        mat = bpy.data.materials.get('Outline')
        if not mat: continue
        o.data.materials.append(mat)
    
    idx = [i for i, mat in enumerate(o.data.materials) if mat.name == 'Outline'][0]
    #idx = len(o.data.materials) - 1
    
    m.material_offset = idx
    m.material_offset_rim = idx