#[as_exec]
import bpy


def setup_denoising():
    bpy.context.view_layer.cycles.denoising_store_passes = True

    nodes = bpy.context.scene.node_tree.nodes
    links = bpy.context.scene.node_tree.links
    denoise_type = 'CompositorNodeDenoise'
    if not nodes.get('Denoise'):
        new_node = nodes.new('CompositorNodeDenoise')
        new_node.location = 300, 100
    node_denoise = nodes.get('Denoise')
    # print(node_denoise)
    node_render = nodes.get('Render Layers')
    # print(node_render.outputs)
    # for o in node_denoise.inputs:
    #     print(o)
    links.new(node_render.outputs['Image'], node_denoise.inputs['Image'])
    links.new(node_render.outputs['Denoising Normal'],
              node_denoise.inputs['Normal'])
    links.new(node_render.outputs['Denoising Albedo'],
              node_denoise.inputs['Albedo'])

setup_denoising()
