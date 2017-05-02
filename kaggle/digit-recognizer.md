#Digit Recognizer
https://www.kaggle.com/c/digit-recognizer
三個檔案
######sample_submission.csv#讓你看示範上傳檔案#
######test.csv#測驗的題目#
######train.csv#學習的資料#
######底下路徑盡量用絕對路徑比較沒有錯誤
####範例檔案https://www.dropbox.com/s/z3c51a1646nw2c9/ML.zip?dl=0
###訓練(retrain.py)
使用github的retrain.py當作捲基神經網路核心產生兩個檔案reteained_labels.txt(字串),retrained_graph.pb(訓練核心):
https://github.com/tensorflow/tensorflow/blob/master/tensorflow/examples/image_retraining/retrain.py

當要運行retrain.py的指令:
注意事項
* 要注意我的路徑跟你的可能不同!
* 注意--image_dir 該路徑底下可能有多個資料夾以資料夾名稱當作辨識的label(以英文命名不然出錯)
* 照片數量需要超過30張不然會出錯(其實只是程式限制這樣比較精準)
* 只能辨識沒有轉動的照片如果需要連轉動的照片也辨識就要加入訓練的圖庫

![](/assets/ts.PNG)


* --how_many_training_steps 設定學習次數
* --model_dir 設定下載已經先訓練的模型放置位置
* --bottleneck_dir 初始化照片的資訊的位置
* --output_graph 輸出訓練核心的位置
* --output_labels 輸出字串位置
* --image_dir 學習的照片該位置

```bash
python -tt retrain.py --bottleneck_dir=/home/s1003951/Desktop/tf_files/bottlenecks --how_many_training_steps 500 --model_dir=/home/s1003951/Desktop/tf_files/inception --output_graph=/home/s1003951/Desktop/tf_files/retrained_graph.pb --output_labels=/home/s1003951/Desktop/tf_files/reteained_labels.txt --image_dir /home/s1003951/Desktop/tf_files/picture_factory
```

###辨識(label_image.py)
使用label_image.py 辨識
注意reteained_labels.txt,retrained_graph.pb檔案的路徑需要修改
```python
import tensorflow as tf
import sys
# change this as you see fit
image_path = sys.argv[1]

# Read in the image_data
image_data = tf.gfile.FastGFile(image_path, 'rb').read()

# Loads label file, strips off carriage return
label_lines = [line.rstrip() for line 
                   in tf.gfile.GFile("/home/s1003951/Desktop/tf_files/reteained_labels.txt")]

# Unpersists graph from file
with tf.gfile.FastGFile("/home/s1003951/Desktop/tf_files/retrained_graph.pb", 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    _ = tf.import_graph_def(graph_def, name='')

with tf.Session() as sess:
    # Feed the image_data as input to the graph and get first prediction
    softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
    
    predictions = sess.run(softmax_tensor, \
             {'DecodeJpeg/contents:0': image_data})
    
    # Sort to show labels of first prediction in order of confidence
    top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
    
    for node_id in top_k:
        human_string = label_lines[node_id]
        score = predictions[0][node_id]
        print('%s (score = %.5f)' % (human_string, score))

```
#####當要運行label_image.py的bash
此照片路徑根據您的照片位置
```
python label_image.py /home/fig.jpg
```

利用這兩個檔案來訓練kaggle的練習比賽
上述程式是核心,需要改寫一些程式但都是簡單python所以在此不多說
* train.csv的文字檔轉成照片
* 照片餵給train.py並訓練
* 讀取test.csv 並轉成照片
* 利用label_image.py辨識照片
* 答案寫入sample_submission.csv


上傳sample_submission.csv驗證準確度


