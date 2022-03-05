#[as_exec]

def main():
    def export_tex():
        #合并tex到源分层文件
        pass
    def create_layersets():
        # psd group模板
        # /source
        # /textures
        #   |tex.xxx_D
        #   |tex.xxx_
        pass
    def load_ps2(img_arr):
        import os
        # 加载选中node链接的图片到psd里面的source layerset
        # 
        import win32com.client
        # opens ps
        psApp = win32com.client.Dispatch("Photoshop.Application")
        # opens file
        psApp.Open(r"C:\\tmp\\1k.psd")

        # doc = psApp.Application.ActiveDocument
        js = r"""
        var doc = app.activeDocument;
        """
        js += r"""
        function SavePNG(saveFile){
            var pngOpts = new ExportOptionsSaveForWeb; 
            pngOpts.format = SaveDocumentType.PNG
            pngOpts.PNG8 = false; 
            pngOpts.transparency = true; 
            pngOpts.interlaced = false; 
            pngOpts.quality = 100;
            activeDocument.exportDocument(new File(saveFile),ExportType.SAVEFORWEB,pngOpts); 
        }
        """
        # folder path:
        textures_path = os.path.dirname(img_arr[0][1])
        textures_path = textures_path.replace("\\", "/")+'/'
        # print("textures_path",textures_path)
        js += r"""var tex_folder = '"""+textures_path+r"""';"""
        js += r"""
        // if (layer.typename == 'LayerSet'){}
        var layerSets = doc.layerSets['textures'].layerSets
        var tex_layerSet_arr = []
        function hide_all() {
            for(var i = 0; i <layerSets.length; i++){
                var layerSet = layerSets[i];
                var name = layerSet.name+"";
                //alert("tex layer:"+name);
                if(name.search("tex.")>-1){
                    tex_layerSet_arr.push(layerSet);
                    layerSet.visible = false;
                }
            }
        };
        hide_all();
        for(var j= 0;j<tex_layerSet_arr.length;j++)
        {
            var layerSet = tex_layerSet_arr[j];
            layerSet.visible = true;
            var saveFile = new File("tex_folder"+layerSet.name+".png");
            SavePNG(saveFile);
            layerSet.visible = false;
        }
        """

        js += r"""

        //doc.close();
        app.activeDocument.close(SaveOptions.DONOTSAVECHANGES);
        """
        # doc.save()
        # doc.Close()
        # com = r"""alert("done")"""
        psApp.DoJavaScript(js)

    def find_link_node(mat, socket):
        for node in mat.node_tree.nodes:
            if node.type == 'TEX_IMAGE' and node.image:
                for output in node.outputs:
                    for link in output.links:
                        if link.to_socket == socket:
                            print('find node')
                            return node

    # for addon
    # mat= bpy.context.material
    mat = bpy.context.active_object.material_slots[0].material
    node_group = [node for node in mat.node_tree.nodes if node.select][0]

    print(node_group.name)
    img_arr = []
    for i in range(0, len(node_group.inputs)):
        input = node_group.inputs[i]
        psd_node_tree = node_group.node_tree
        socket = psd_node_tree.inputs[i]
        print(socket.name)
        layer_name = socket.name
        image_node = find_link_node(mat, input)
        if image_node:
            filepath = image_node.image.filepath
            img_arr.append([layer_name, filepath])
            print(image_node.name)
            print(filepath)

    load_ps2(img_arr)


main()
