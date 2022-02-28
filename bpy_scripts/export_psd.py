#[as_exec]

def main():
    def export_tex():
        #合并tex到源分层文件
        pass
    def load_ps2(img_arr):
        # 加载选中node链接的图片到psd里面的source layerset
        # text layer 
        import win32com.client
        # opens ps
        psApp = win32com.client.Dispatch("Photoshop.Application")
        # opens file
        psApp.Open(r"C:\\tmp\\1k.psd")

        # doc = psApp.Application.ActiveDocument
        js = r"""
        var doc = app.activeDocument;
        """
        # load img function
        js += r"""
        function load_file1(file){
            var idPlc = charIDToTypeID( "Plc " );
            var desc3 = new ActionDescriptor();
            var idnull = charIDToTypeID( "null" );
            desc3.putPath( idnull, file);
            var idFTcs = charIDToTypeID( "FTcs" );
            var idQCSt = charIDToTypeID( "QCSt" );
            var idQcsa = charIDToTypeID( "Qcsa" );
            desc3.putEnumerated( idFTcs, idQCSt, idQcsa );
            executeAction( idPlc, desc3, DialogModes.NO );
        };
        """

        js += r"""
        var group;
        try{
            group = doc.layerSets.getByName("source");
            group.remove();
        }
        catch(e){

        }
        group = doc.layerSets.add();
        group.name = "source";
        """

        for img in img_arr:
            print(img[0],img[1])
            js += r"""
            var sourceFile= new File("{1}");
            load_file1(sourceFile);
            doc.activeLayer.move(group,ElementPlacement.INSIDE);
            doc.activeLayer.name = "{0}";
            """.format(img[0],img[1].replace('\\','/'))
        js += r"""
        group.visible = false;
        app.activeDocument.layerSets['source'].visible = true
        doc.save();
        doc.close();
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
    # open csp

main()
