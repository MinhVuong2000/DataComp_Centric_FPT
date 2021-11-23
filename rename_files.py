import os 

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
        
def move_files_in_folder(src_path, dst_path):
    """Moves all files in the source folder into the destination folder. 

    Args:
        src_path (str): [description]
        dst_path (str): [description]
    """
    pass
  
if __name__ == '__main__': 
    path = "/Users/vuongnguyenthiminh/Downloads/Senior/temp/"
    rename(path) 