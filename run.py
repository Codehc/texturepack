import os
import shutil
import zipfile

def util(source_dir,target_dir):
    # copying files
    i=0
    list_files=[]
    for root, dirs, files in os.walk(source_dir, topdown=True):
        for file in files:
            if file.endswith(".png"):
                full_file=os.path.join(root,file)
                list_files.append(full_file)
                print(i,full_file)
                i +=1


    print("Select item. E.g. 1")
    temp = input().lower().strip()
    list_files_num=temp.split()
    for c in list_files_num:
        i_c=int(c)
        if i_c<=len(list_files):
            shutil.copy(list_files[i_c],target_dir)
            print("Zipping file",list_files[i_c])
        else:
            print("Skipping invalid file number: Out of range",i_c)





print("starting")
sample_dir=os.path.join(".","samples")
sword_dir=os.path.join(sample_dir,"swords")
wool_dir=os.path.join(sample_dir,"wool")
target_base =  os.path.join(".","target") 
zipfile_name=os.path.join(".","walrus")


# create fresh target
if os.path.exists(target_base):
    shutil.rmtree(target_base, ignore_errors=False, onerror=None)
os.mkdir(target_base,0o777)

# create levels needed for overlay to work
target_dir_temp=os.path.join(target_base,"assets")
os.mkdir(target_dir_temp,0o777)
target_dir_temp=os.path.join(target_dir_temp,"minecraft")
os.mkdir(target_dir_temp,0o777)
target_dir_temp=os.path.join(target_dir_temp,"textures")
os.mkdir(target_dir_temp,0o777)

# add swords
target_dir=os.path.join(target_dir_temp,"items")
os.mkdir(target_dir)
util(sword_dir,target_dir)

# add wool
target_dir=os.path.join(target_dir_temp,"blocks")
os.mkdir(target_dir)
util(wool_dir,target_dir)


# add description
full_file=os.path.join(sample_dir,"pack.mcmeta")
shutil.copy(full_file,target_base)

# add pack image
full_file2=os.path.join(sample_dir,"pack.png")
shutil.copy(full_file2,target_base)
# create a zip file
shutil.make_archive(zipfile_name, 'zip', root_dir=target_base)
print("finished")