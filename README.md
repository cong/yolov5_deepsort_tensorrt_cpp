# yolov5_deepsort_tensorrt_cpp

## Introduction

This repo is a C++ version of **[yolov5_deepsort_tensorrt](https://github.com/cong/yolov5_deepsort_tensorrt)**. 

And packing all C++ programs into .so files, using Python script to call C++ programs further.

The entire project file size totals 40MB

**NVIDIA Jetson Xavier NX**  and the *X86* architecture works all be ok. 

Since this project is being used in a science and technology major project, we just temporarily provide a test example.

## Environments

All platforms：
- CUDA and cuDNN latest
- Python 3.7
- OpenCV-Python latest (we use 4.2)


## Speed

The speeds of DeepSort depend on the target number in the picture.

The following data are tested in the case of single target and 100+ targets with 720p USB camera.


| Platforms         | Single target         | 100+ targets           |
| :---------------- | --------------------- | ---------------------- |
| GTX 2080Ti        | 8ms / 125FPS / 1247M  | 31ms /  32FPS / 1247M  |
| Jetson Xavier NX  | -ms / -FPS / -M  | -ms /  -FPS / -M  |

## Inference

1. Clone this repo

   ```shell
   git clone https://github.com/cong/yolov5_deepsort_tensorrt_cpp.git
   ```

2. Run

   ```
   python demo.py
   ```

## Customize

1. Training your own model.
2. Convert your own model to engine.
3. Replace the `***.engine` file.

## Optional setting

- Your likes are my motivation to update the project, if you feel that it is helpful to you, please give me a star. Thx!  :)
- For more information you can visit the [Blog](http://wangcong.net).
