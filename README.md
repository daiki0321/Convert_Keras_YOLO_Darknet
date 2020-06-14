# Convert_Keras_YOLO_Darknet

Keras Yolo annotation is required like as below.

Row format: image_file_path box1 box2 ... boxN;  
Box format: x_min,y_min,x_max,y_max,class_id (no space).  

data_for_training.json 
~~~ 
/home/guest/train_imgs_rgb_yuv/0.jpg 256,205,267,212,0 266,194,277,258,1 
~~~

On the other hand, darkent required another formant,  
\<object-class> \<x> \<y> \<width> \<height>  

train_data/signate2/20200613/labels/train_imgs_rgb_yuv/00000.txt 
~~~ 
0 0.628606 0.501202 0.026442 0.016827  
1 0.652644 0.543269 0.026442 0.153846  
1 0.912260 0.545673 0.021635 0.076923  
~~~
  
So we need to convert the format from keras-yolov3 to darknet format. 
