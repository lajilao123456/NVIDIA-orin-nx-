# NVIDIA-orin-nx-
NVIDIA orin nx 环境部署踩坑记录，目前工控机架构为arm64，jetpack版本为5.1.1.1，对应的cuda为11.4，为了能够驱动GPU需要安装pytorch文件，同时如果你和我一样需要使用yolov进行目标检测的，还得安装对应的torchvision版本。
首先需要安装pytorch文件，这个只需要下载whl包就行，但是需要注意的是我们只能安装版本为torch-2.0.0+nv23.05-cp38-cp38-linux_aarch64，下载对应的torch-2.0.0+nv23.05-cp38-cp38-linux_aarch64.whl文件
由于工控机为arm64架构的，所以对与torchvision包不能够使用pip命令安装，否则会一直出现版本问题的提示，导致后面没法使用gpu，我这边对应的安装版本是vision-0.15.1，注意这个需要源码安装，安装完成后可以使用
python check_gpu.py
命令进行检查是否能够驱动cpu
