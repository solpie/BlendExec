# version 2021-1-27 
import mset
mset.newScene()
baker = None

baker = mset.BakerObject("Default")


def set_color_value():
    materials = mset.getAllMaterials()
    for mat in materials:
        print('mat:', mat.getSubroutine(
            'albedo').getField("Color"))
        mat.getSubroutine('albedo').setField("Color", [1.0, 1.0, 1.0])
    pass


# Bake:
if baker != None:
    # Setting up the baker
    baker.outputPath = "MyBake.psd"
    baker.outputBits = 8
    baker.outputSamples = 16
    baker.edgePadding = "Custom"
    baker.edgePaddingSize = 16
    baker.outputSoften = 0
    baker.useHiddenMeshes = True
    baker.ignoreTransforms = True
    baker.smoothCage = True
    baker.ignoreBackfaces = True
    baker.multipleTextureSets = False

    # These settings only apply if texture sets aren't enabled:
    baker.outputWidth = 2048
    baker.outputHeight = 2048

    # If Texture Sets are enabled, then you can set them up as follows:
    #baker.setTextureSetWidth("My Texture Set Name", 256)
    # Or...
    #baker.setTextureSetWidth(0, 256)

    # baker.loadPreset("Default")

    normalMap = baker.getMap("Normals")
    normalMap.enabled = False

    albedoMap = baker.getMap("Albedo")
    albedoMap.enabled = True

    baker.importModel('f:/tmp/bake_low.fbx')
    baker.importModel('f:/tmp/bake_high.fbx')
    # set mat color
    set_color_value()
else:
    print("Could not find baker!")
