# [as_exec]
import bpy
def main():
    import win32com.client
    # opens ps
    psApp = win32com.client.Dispatch("Photoshop.Application")
    # js = r"""var layerSet = app.activeDocument.layerSets.getByName("source");\n"""
    # js += r"""layerSet.remove();\n"""
    # js += r"""var img = new File("C:/1.jpg");\n"""
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

    var sourceFile= new File("C:/tmp/1.jpg");
    load_file1(sourceFile)
    doc.activeLayer.move(group,ElementPlacement.INSIDE)
    """
    # activeDocument.close(SaveOptions.DONOTSAVECHANGES);
    # js += r"""
    # var sourceFile= new File("C:/tmp/1.jpg");
    # load_file1(sourceFile)
    # """

    psApp.DoJavaScript(js)
main()
