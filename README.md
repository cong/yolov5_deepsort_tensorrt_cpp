# yolov5_deepsort_tensorrt_cpp

## Introduction

This repo is a C++ version of **[yolov5_deepsort_tensorrt](https://github.com/cong/yolov5_deepsort_tensorrt)**. 

packing all C++ programs into .so files, using Python script to call C++ programs further.

The entire project file size totals 40MB

**NVIDIA Jetson Xavier NX**  and the *X86* architecture works all be ok. 



## Environments

All platforms：
- CUDA and cuDNN latest
- Python 3.7
- OpenCV-Python latest (we use 4.2)


## Speed

The speeds of DeepSort depend on the target number in the picture.

The following data are tested in the case of single target in the picture.


