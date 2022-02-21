#[as_exec]
import bpy


#        fcurve = shape_keys.driver_add('key_blocks["%s"].value' % obj.active_shape_key.name)
#        driver = fcurve.driver
#        driver.type = 'SCRIPTED'
#        driver.expression = "var"
#        var = driver.variables.new()
#        var.name = "var"
#        var.type = 'SINGLE_PROP'
def main():
    obj = bpy.context.view_layer.objects.active
    def add_key_driver(obj,from_key):
        shape_keys = obj.data.shape_keys
        if not shape_keys.animation_data:return
        for drv in shape_keys.animation_data.drivers:
            if drv.data_path.find(from_key.name) > -1:
                print(drv.data_path)
                from_driver = drv.driver
                fcurve = shape_keys.driver_add('key_blocks["%s"].value' % obj.active_shape_key.name)
                # copy param
                driver = fcurve.driver
                driver.type = from_driver.type
                driver.expression = from_driver.expression
                for var in from_driver.variables:
                    new_var = driver.variables.new()
                    new_var.name = var.name
                    new_var.type = var.type
        
                    new_var.targets[0].id = var.targets[0].id
                    
                    new_var.targets[0].bone_target = var.targets[0].bone_target
                    new_var.targets[0].transform_space = var.targets[0].transform_space

    def is_L_R_name(name):
        mirror_name = ['.r','.l','.R','.L']
        for idx,k in enumerate([".l",'.r','.L','.R']):
            print(idx,k)
            if name.find(k) > -1:
                return True, name.replace(k, mirror_name[idx])
                
    def mirror_shape_key(obj):
        from_key = obj.active_shape_key
        is_LR,mirror_name = is_L_R_name(from_key.name)
        if is_LR:
            new_key_name = mirror_name
        bpy.ops.object.shape_key_add(from_mix=True)
        
        obj.active_shape_key.name = new_key_name
        bpy.ops.object.shape_key_mirror(use_topology=False)
        obj.active_shape_key.value = 1
        add_key_driver(obj,from_key)
        
        

        
        for sk in obj.data.shape_keys.key_blocks:
            if sk.name != "Basis" and is_L_R_name(sk.name):
                
                print(sk.name)
    mirror_shape_key(obj)

main()
