import os
import shutil

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

    # it is inclusive, meaning 2 and 5 will be in it
    print("Select the item(s) you want. E.g. 1 3-5 15 ")
    temp_str = input().lower().strip()
    if temp_str=="":
        return
    temp_list=temp_str.split(" ")
    for temp in temp_list:
        if "-" in temp:
            # range
            list_files_num=temp.split("-")
            low=int(list_files_num[0])
            high=int(list_files_num[1])
        else:
            low=int(temp)
            high=low
        if high>=len(list_files):
            print("Invalid: Too high",high)
            return
        for i_c in range(low,high+1):
            shutil.copy(list_files[i_c],target_dir)
                
    sub_message = f"{target_dir} Selected"
    sub_message.title()
    print(sub_message)


print("Please select the items you want in your mashup.")
sample_dir=os.path.join(".","samples")
sword_dir=os.path.join(sample_dir,"swords")
gui_dir=os.path.join(sample_dir,"gui")
wool_dir=os.path.join(sample_dir,"wool")
sky_dir=os.path.join(sample_dir,"sky")
particle_dir=os.path.join(sample_dir,"particles")
gui_dir=os.path.join(sample_dir,"gui")
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

# add sky
target_dir=os.path.join(target_dir_temp,"environment")
os.mkdir(target_dir)
util(sky_dir,target_dir)

# choose particles
target_particle_dir=os.path.join(target_dir_temp,"particle")
os.mkdir(target_dir)
util(particle_dir, target_particle_dir)

# choose gui
target_gui_dir=os.path.join(target_dir_temp,"gui")
os.mkdir(target_gui_dir)
util(particle_dir, target_gui_dir)

# add description
full_file=os.path.join(sample_dir,"pack.mcmeta")
shutil.copy(full_file,target_base)

# add pack image
full_file2=os.path.join(sample_dir,"pack.png")
shutil.copy(full_file2,target_base)

# create a zip file
shutil.make_archive(zipfile_name, 'zip', root_dir=target_base)
print("finished")