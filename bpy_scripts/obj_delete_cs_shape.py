# [as_exec]
import bpy
def main():
    bpy.ops.object.select_pattern(pattern="cs_*")
    bpy.ops.object.delete(use_global=False)
main()
