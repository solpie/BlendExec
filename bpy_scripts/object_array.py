#[as_exec]
# keywords 弹框 dialog
import bpy


def main():
    def ObjectArrangeB(self, ofsX, ofsY, ofsZ):
        def order(sels, isX, isY, isZ, ofsX=0, ofsY=0, ofsZ=0):
            if len(sels[:]) > 1:
                # VARIABLES
                dif = sels[-1].location - sels[0].location
                chunkglobal = dif / (len(sels[:]) - 1)
                chunkx = 0
                chunky = 0
                chunkz = 0
                deltafst = sels[0].location

                # ORDENA
                for idx in range(0, len(sels)):
                    obj = sels[idx]
                    if isX:
                        obj.location.x = deltafst[0] + chunkx
                    if isY:
                        obj.location.y = deltafst[1] + chunky
                    if isZ:
                        obj.location.z = deltafst[2] + chunkz
                    if ofsX:
                        chunkx += ofsX
                    else:
                        chunkx += chunkglobal[0]
                    if ofsY:
                        chunky += ofsY
                    else:
                        chunky += chunkglobal[1]
                    if ofsZ:
                        chunkz += ofsZ
                    else:
                        chunkz += chunkglobal[2]
            else:
                self.report({'ERROR'}, "Selection is only 1!")

        sels = bpy.context.selected_objects
        isX = not ofsX == 0.0
        isY = not ofsY == 0.0
        isZ = not ofsZ == 0.0
        if isX:
            order(sorted(sels, key=lambda obj: obj.location.x),
                  isX, False, False, ofsX=ofsX)
        if isY:
            order(sorted(sels, key=lambda obj: obj.location.y),
                  False, isY, False, ofsY=ofsY)
        if isZ:
            order(sorted(sels, key=lambda obj: obj.location.z),
                  False, False, isZ, ofsZ=ofsZ)

    class WM_OT_Array(bpy.types.Operator):
        bl_label = "Array Object"
        bl_idname = "wm.array"
        bl_options = {'REGISTER', 'UNDO'}

        xyz : bpy.props.FloatVectorProperty(name="XYZ:", default=(0, 0, 0))

        def execute(self, context):
            xyz = self.xyz
            ObjectArrangeB(self, xyz[0], xyz[1], xyz[2])
            return {'FINISHED'}

        def invoke(self, context, event):
            
            return context.window_manager.invoke_props_dialog(self)
    # if bpy.ops.wm.array:
    #     print("class reged")
    # else:
    bpy.utils.register_class(WM_OT_Array)
    bpy.ops.wm.array('INVOKE_DEFAULT')


main()
