#Tensorflow
優點:
    * python支援使得語法簡易
    * 支援多GPU/CPU運算
    * GITHUB使用人數多,所以問題能快速解決
    
    
# tensorflow(easy way) 
```sh

sudo apt-get install libcupti-dev
sudo apt-get install python3-pip python3-dev python3-virtualenv
sudo pip3 install -U setuptools
sudo pip3 install --upgrade pip
sudo pip3 install tensorflow-gpu 

```
# install tensorlfow as source(best performence way)
### 1.get tensorflow source
```
git clone https://github.com/tensorflow/tensorflow 
cd tensorflow
git checkout
```
### 2.install Bazel
```
sudo apt-get install openjdk-8-jdk
echo "deb [arch=amd64] http://storage.googleapis.com/bazel-apt stable jdk1.8" | sudo tee /etc/apt/sources.list.d/bazel.list
curl https://bazel.build/bazel-release.pub.gpg | sudo apt-key add -
sudo apt-get update && sudo apt-get install bazel
```

### 3.for python3
```
sudo apt-get install python3-numpy python3-dev python3-pip python3-wheel
sudo apt-get install libcupti-dev 
sudo pip3 install -U setuptools
```
### 4. configure
```
cd tensorflow
./configure

##### 
WARNING: Running Bazel server needs to be killed, because the startup options are different.
Please specify the location of python. [Default is /usr/bin/python]: /usr/bin/python3
Found possible Python library paths:
/usr/local/lib/python2.7/dist-packages
/usr/lib/python2.7/dist-packages

Please input the desired Python library path to use.  Default is /usr/local/lib/python2.7/dist-packages/usr/local/lib/python3.5/dist-packages/
Do you wish to build TensorFlow with jemalloc as malloc support? [Y/n]: y
jemalloc as malloc support will be enabled for TensorFlow.

Do you wish to build TensorFlow with Google Cloud Platform support? [y/N]: n
No Google Cloud Platform support will be enabled for TensorFlow.

Do you wish to build TensorFlow with Hadoop File System support? [y/N]: n
No Hadoop File System support will be enabled for TensorFlow.

Do you wish to build TensorFlow with XLA JIT support? [y/N]: y
XLA JIT support will be enabled for TensorFlow.

Do you wish to build TensorFlow with VERBS support? [y/N]: n
No VERBS support will be enabled for TensorFlow.

Do you wish to build TensorFlow with OpenCL support? [y/N]: n
No OpenCL support will be enabled for TensorFlow.

Do you wish to build TensorFlow with CUDA support? [y/N]: y
CUDA support will be enabled for TensorFlow.

Please specify the CUDA SDK version you want to use, e.g. 7.0. [Leave empty to default to CUDA 8.0]:empty

Please specify the location where CUDA 8.0 toolkit is installed. Refer to README.md for more details. [Default is /usr/local/cuda]:empty
"Please specify the cuDNN version you want to use. [Leave empty to default to cuDNN 6.0]: 5

Please specify the location where cuDNN 5 library is installed. Refer to README.md for more details. [Default is /usr/local/cuda]:empty
 
Please specify a list of comma-separated Cuda compute capabilities you want to build with.
You can find the compute capability of your device at: https://developer.nvidia.com/cuda-gpus.
Please note that each additional compute capability significantly increases your build time and binary size. [Default is: 3.5,5.2]:5.0

Do you want to use clang as CUDA compiler? [y/N]: n
nvcc will be used as CUDA compiler.

Please specify which gcc should be used by nvcc as the host compiler. [Default is /usr/bin/gcc]: empty
Do you wish to build TensorFlow with MPI support? [y/N]: n
No MPI support will be enabled for TensorFlow.

Please specify optimization flags to use during compilation when bazel option "--config=opt" is specified [Default is -march=native]: empty
Add "--config=mkl" to your bazel command to build with MKL support.
Please note that MKL on MacOS or windows is still not supported.
If you would like to use a local MKL instead of downloading, please set the environment variable "TF_MKL_ROOT" every time before build.
Configuration finished
```
### 5.start compiler
##### for cpu version
```
bazel build --config=opt //tensorflow/tools/pip_package:build_pip_package

```
##### for gpu version
```
bazel build --config=opt --config=cuda //tensorflow/tools/pip_package:build_pip_package 
```

### 6.buile whl file for pip
```
bazel-bin/tensorflow/tools/pip_package/build_pip_package /tmp/tensorflow_pkg
```
### 7.install tensorflow
```
sudo pip install /tmp/tensorflow_pkg/tensorflow*
```
# install CUAD AND CUDNN for tensorflow-gpu version
各個版本cuda


https://developer.nvidia.com/cuda-toolkit-archive


download
[CUDA® Toolkit 8.0](https://developer.nvidia.com/compute/cuda/8.0/Prod2/local_installers/cuda-repo-ubuntu1604-8-0-local-ga2_8.0.61-1_amd64-deb)
Linux->x86_64->ubuntu->16.04->deb(local)


cd to download file
```sh
sudo dpkg -i cuda-repo-ubuntu1604-8-0-local-ga2_8.0.61-1_amd64.deb
sudo apt-get update
sudo apt-get install cuda
```

download
[cuDNN v5.1 Library for Linux](https://developer.nvidia.com/compute/machine-learning/cudnn/secure/v5.1/prod_20161129/8.0/cudnn-8.0-linux-x64-v5.1-tgz)
put the file into cuda folder to upgrade
/usr/local/cuda

```
tar -zxvf cudnn-9.0-linux-x64-v7.tgz
sudo cp cuda/include/cudnn.h /usr/local/cuda/include/
sudo cp cuda/lib64/libcudnn* /usr/local/cuda/lib64/
sudo chmod a+r /usr/local/cuda/include/cudnn.h
sudo chmod a+r /usr/local/cuda/lib64/libcudnn*


```



set Environment Variable
```
sudo vim ~/.bashrc
```
write 
```

export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:/usr/local/cuda/lib64"
export CUDA_HOME=/usr/local/cuda
```