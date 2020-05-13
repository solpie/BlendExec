import mset
mset.newScene()
baker = None

baker =mset.BakerObject()
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

	baker.loadPreset("Default")

	normalMap = baker.getMap("Normals")
	normalMap.enabled = False

	albedoMap = baker.getMap("Albedo")
	albedoMap.enabled = True
    
	baker.importModel('f:/tmp/bake_low.fbx')
	baker.importModel('f:/tmp/bake_high.fbx')
else:
	print("Could not find baker!")

