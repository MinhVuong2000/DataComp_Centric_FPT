import os


def check_same_files(path1, path2):
    files_path1 = set(map(lambda file: file[:-4],os.listdir(path1)))
    files_path2 = set(map(lambda file: file[:-4],os.listdir(path2)))
    diff_p1_p2 = set(map(lambda name: name+'.jpg',files_path1-files_path2))
    print(f"Files in {path1} but not in {path2}: \n{diff_p1_p2}")
    diff_p2_p1 = set(map(lambda name: name+'.txt',files_path2-files_path1))
    print(f"Files in {path2} but not in {path1}: \n{diff_p2_p1}")
    return diff_p1_p2, diff_p2_p1 

def remove_diff(path, diff_files):
    for item in diff_files:
        os.remove(os.path.join(path, item))
    

if __name__ == '__main__':
    root_path = "/Users/vuongnguyenthiminh/Downloads/OneDrive_1_11-26-2021/dataset/"
    img_path = "/Users/vuongnguyenthiminh/Downloads/OneDrive_1_11-26-2021/dataset/images/"
    lbl_path = '/Users/vuongnguyenthiminh/Downloads/OneDrive_1_11-26-2021/dataset/labels/'
    #delete private file
    for path in [root_path,img_path,lbl_path]:
        for item in os.listdir(path):
            if '.' in item:
                os.remove(os.path.join(path, item))
    for path in os.listdir(lbl_path):
        path1 = os.path.join(img_path, path)
        path2 = os.path.join(lbl_path, path)
        diff_p1_p2, diff_p2_p1 = check_same_files(path1, path2)
        # remove_diff(path1, diff_p1_p2)
        # remove_diff(path2, diff_p2_p1)
        # print("Delete diff be done")
        # #check again
        # check_same_files(path1, path2)
        print("\n")
        
        