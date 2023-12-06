import tensorflow as tf
import os
os.environ['CUDA_VISIBLE_DEVICES'] = '0'  # Or whichever device ID you want to use

if tf.test.gpu_device_name():
    print('Default GPU Device: {}'.format(tf.test.gpu_device_name()))
else:
    print("Please install GPU version of TF")