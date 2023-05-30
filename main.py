import argparse, threading

from functions import *

#region args
parser = argparse.ArgumentParser(prog='File Manager', description='What the program does', epilog='Text at the bottom of help')
args = parser.parse_args()
#endregion

def Main():
    with open('file-manager.log', 'w') as f:
        f.write('')

    from gui import GUI
    ui_thread = threading.Thread(target=GUI, args=[args])
    ui_thread.start()
    ui_thread.join()

if __name__ == '__main__' or 'main':
    Main()
