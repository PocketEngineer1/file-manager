import os

from functions import *
import UIFramework as UI

def GUI(args):
    ui = UI.UI(1200, 800, 'Not Mark\'s File Manager')

    def FileDisplaySection(fileName: str, x, y, path, width=ui.width, fileType='File'):
        def GoButtonClickHandeler():
            if os.path.isdir(path):
                PathTextInput.text = path
                Update(path)
        
        GoButton = UI.Button('FileDisplaySection:GoButton/' + fileName, x, y, 50, 30, text='Go!', click_handler=GoButtonClickHandeler)
        FileNameText = UI.Text('FileDisplaySection:FileNameText/' + fileName, x + 60, y + 9, fileName)
        FileTypeBackground = UI.Rectangle('FileDisplaySection:FileTypeBackground/' + fileName, width - 260, y, 255, 30, (200, 200, 200))
        FileTypeText = UI.Text('FileDisplaySection:FileTypeText/' + fileName, width - 250, y + 9, fileType)
        ui.add_element(GoButton)
        ui.add_element(FileNameText)
        ui.add_element(FileTypeBackground)
        ui.add_element(FileTypeText)

    def Update(path):
        ui.clear_elements()
        ui.add_element(PathTextInput)
        j = 40
        if os.path.exists(path):
            for i in os.listdir(path):
                if os.path.isfile(path + '/' + i):
                    Type = os.path.splitext(i)[1]
                    Type = Type.lower()
                    if Type == '.py':
                        Type = 'Python Script'
                    elif Type == '.pyc':
                        Type = 'Compiled Python Script'
                    elif Type == '.txt':
                        Type = 'Plain Text File'
                    elif Type == '.log':
                        Type = 'Log File'
                    elif Type == '.deb':
                        Type = 'Deb Package'
                    elif Type == '.jar':
                        Type = 'Java Archive'
                    elif Type == '.zip':
                        Type = 'Zipped Folder'
                    elif Type == '.7z':
                        Type = '7-Zip Archive'
                    elif Type == '.pixi':
                        Type = 'Pixi Document'
                    elif Type == '.pixil':
                        Type = 'Pixilart Project'
                    elif Type == '.png':
                        Type = 'PNG Image'
                    elif Type == '.jpeg' or Type == '.jpg':
                        Type = 'JPEG Image'
                    elif Type == '.gif':
                        Type = 'GIF Image'
                    elif Type == '.bin' or Type == '.binary':
                        Type = 'Generic Binary File'
                    elif Type == '.dat':
                        Type = 'Data File'
                    elif Type == '.vm':
                        Type = 'Voxel Master World'
                    elif Type == '.json':
                        Type = 'JSON File'
                    elif Type == '.json5':
                        Type = 'JSON5 File'
                    elif Type == '.xcf':
                        Type = 'GIMP Image'
                    elif Type == '.ipv':
                        Type = 'ibis Paint Artwork'
                    elif Type == '.php':
                        Type = 'PHP Source Code'
                    elif Type == '.phtm' or Type == '.phtml':
                        Type = 'PHP Web Page'
                    elif Type == '.htm' or Type == '.html':
                        Type = 'HTML Document'
                    elif Type == '.md' or Type == '.markdown':
                        Type = 'Markdown Document'
                    elif Type == '.css':
                        Type = 'Cascading Style Sheet'
                    elif Type == '.blend':
                        Type = 'Blender Project'
                    elif Type == '.wick':
                        Type = 'Wick Editor Project'
                    elif Type == '.wick':
                        Type = 'Wick Editor Project'
                    elif Type == '.bbmodel':
                        Type = 'Blockbench Model'
                    elif Type == '.vrm':
                        Type = 'Virtual Reality Model'
                    elif Type == '.vroid':
                        Type = 'VRoid Studio Avatar'
                    elif Type == '.vox':
                        Type = 'Magica Voxel Model'
                    elif Type == '.js':
                        Type = 'JavaScript File'
                    elif Type == '.pal':
                        Type = 'JASC Color Palette'
                    elif Type == '.ttf':
                        Type = 'TrueType Font'
                    elif Type == '.otf':
                        Type = 'OpenType Font'
                    elif Type == '.odt':
                        Type = 'OpenDocument Text Document'
                    elif Type == '.ods':
                        Type = 'OpenDocument Spreadsheet'
                    elif Type == '.odp':
                        Type = 'OpenDocument Presentation'
                    elif Type == '.odg':
                        Type = 'OpenDocument Graphic'
                    elif Type == '.odf':
                        Type = 'OpenDocument Formula'
                    elif Type == '.odb':
                        Type = 'OpenDocument Database'
                    elif Type == '.odm':
                        Type = 'OpenDocument Master Document'
                    elif Type == '.docx':
                        Type = 'Microsoft Word Document'
                    elif Type == '.xlsx':
                        Type = 'Microsoft Excel Spreadsheet'
                    elif Type == '.pptx':
                        Type = 'Microsoft PowerPoint Presentation'
                    elif Type == '.cs':
                        Type = 'C Sharp Script'
                    elif Type == '':
                        Type = 'File'
                    else:
                        Type = 'Unknown File Type'
                    FileDisplaySection(i, 5, j, fileType=Type, path=path + '/' + i)
                if os.path.isdir(path + '/' + i):
                    FileDisplaySection(i, 5, j, fileType='Folder', path=path + '/' + i)
                j += 35
    
    PathTextInput = UI.TextInput('PathTextInput', 5, 5, 1190, 30, on_change=Update, placeholder='Path to view')

    Update('./')
    ui.run()
