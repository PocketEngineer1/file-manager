import os, sys, shutil

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
        FileTypeBackground = UI.Rectangle('FileDisplaySection:FileTypeBackground/' + fileName, width - 210, y, 205, 30, (200, 200, 200))
        FileTypeText = UI.Text('FileDisplaySection:FileTypeText/' + fileName, width - 200, y + 9, fileType)
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
                    if Type == '.py':
                        Type = 'Python Script'
                    elif Type == '.pyc':
                        Type = 'Compiled Python Script'
                    elif Type == '.txt':
                        Type = 'Plain Text File'
                    elif Type == '.log':
                        Type = 'Log File'
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
