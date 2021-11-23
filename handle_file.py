import os 
import shutil

# Function to rename multiple files 
def rename(path, str_add="blur_"):
    """
    Rename files in folder.
    
    Args:
        - path: path of folder need rename files in this
        - str_add: string need add in name of files, should be name of method apply for generate images
    """ 
    os.chdir(path)
    for filename in os.listdir(os.getcwd()):
        
        dst =''.join([os.getcwd(),"/",str_add,filename])
        print(dst)
        os.rename(filename, dst)
        
def move_files(src_path, dst_path, str_add=''):
    """Moves all files in the source folder into the destination folder. 

    Args:
        src_path (str): path of source folder
        dst_path (str): path of destination folder
        str_add (str): string need add in name of files to rename, should be name of method apply for generate images
"""
    for filename in os.listdir(src_path):
        dst =''.join([dst_path, str_add,filename])
        print(dst)
        os.replace(src_path+filename,dst)
        
def copy_files(src_path, dst_path, str_add=''):
    """Copy all files in the source folder into the destination folder. 

    Args:
        src_path (str): path of source folder
        dst_path (str): path of destination folder
        str_add (str): string need add in name of files to rename, should be name of method apply for generate images
    """
    for filename in os.listdir(src_path):
        dst =''.join([dst_path, str_add,filename])
        print(dst)
        shutil.copy2(src_path+filename, dst)
        
  
if __name__ == '__main__': 
    # example
    path = "/Users/vuongnguyenthiminh/Downloads/Senior/abc/"
    dst_path = "/Users/vuongnguyenthiminh/Downloads/Senior/temp/"
    copy_files(path, dst_path, 'abc_') # combine rename and copy
    copy_files(path, dst_path) # only copy