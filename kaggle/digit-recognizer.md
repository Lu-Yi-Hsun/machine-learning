#Digit Recognizer
https://www.kaggle.com/c/digit-recognizer
三個檔案
sample_submission.csv#讓你看示範上傳檔案#
test.csv#測驗的題目#
train.csv#學習的資料#

使用github的retrain.py當作捲基神經網路核心產生兩個檔案reteained_labels.txt(字串),retrained_graph.pb(訓練核心):
https://github.com/tensorflow/tensorflow/blob/master/tensorflow/examples/image_retraining/retrain.py

當要運行retrain.py的指令:
```bash
python -tt retrain.py --bottleneck_dir=/home/s1003951/Desktop/tf_files/bottlenecks --how_many_training_steps 500 --model_dir=/home/s1003951/Desktop/tf_files/inception --output_graph=/home/s1003951/Desktop/tf_files/retrained_graph.pb --output_labels=/home/s1003951/Desktop/tf_files/reteained_labels.txt --image_dir /home/s1003951/Desktop/tf_files/picture_factory
```

使用label_image.py 辨識
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