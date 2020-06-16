#import libraries
import os
import sys
import cv2

if len(os.sys.argv) != 2:
    print("Need to set keras-yolo anotattion file\n")
    quit()

data_filename = os.sys.argv[1]

train_text = os.path.dirname(data_filename)+'/'+'train.txt'
valid_text = os.path.dirname(data_filename)+'/'+'valid.txt'

train_list_file    = open(train_text, "w")
valid_list_file    = open(valid_text, "w")

with open(data_filename, "r") as f:

    count = 0

    for read_data in f:
        print(read_data.split(' ')[0])
        
        img_name = read_data.split(' ')[0]
        if count % 10 :
            train_list_file.write(img_name+'\n')
        else :
            valid_list_file.write(img_name+'\n')

        annotations = read_data.split(' ')[1:]

        img = cv2.imread(img_name)
        height, width, channel = img.shape

        str_to_write = ""
        for i in range (0, len(annotations)):#here we browse all videos
            
            #print(annotations[i])
            box = annotations[i].split(',')[0:4]
            box[0] = int(box[0])
            box[1] = int(box[1])
            box[2] = int(box[2])
            box[3] = int(box[3])
            #print(box)
            classes = annotations[i].split(',')[4].replace("\n", "")

            str_to_write += str(classes)+' '+str('{:.06f}'.format((box[0] + box[2])/2/width))+' '+str('{:.06f}'.format((box[1] + box[3])/2/height))+' '+str('{:.06f}'.format((box[2] - box[0])/width))+' '+str('{:.06f}'.format((box[3] - box[1])/height))+'\n'

        path_out_file=img_name.replace("/images/", "/labels/").replace(".jpg", ".txt")

        os.makedirs(os.path.dirname(path_out_file), exist_ok=True)

        with open(path_out_file, "w") as out_file:
            #print(path_out_file)
            #print(str_to_write)
            out_file.write(str_to_write)
    
        count += 1
        
train_list_file.close()
valid_list_file.close()

