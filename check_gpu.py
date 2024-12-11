#!/usr/bin/env python
# -*- coding: utf-8 -*-


import torch

def check_gpu():
    print("PyTorch 是否支持 CUDA:", torch.cuda.is_available())
    if torch.cuda.is_available():
        print("GPU 数量:", torch.cuda.device_count())
        print("当前 GPU 设备索引:", torch.cuda.current_device())
        print("当前 GPU 名称:", torch.cuda.get_device_name(torch.cuda.current_device()))
        print("CUDA 版本:", torch.version.cuda)
        print("GPU 设备内存:")
        for i in range(torch.cuda.device_count()):
            total_memory = torch.cuda.get_device_properties(i).total_memory
            print(f" - GPU {i} 总内存: {total_memory / 1024 ** 3:.2f} GB")
    else:
        print("未检测到支持 CUDA 的 GPU，请检查驱动和环境配置。")

if __name__ == "__main__":
    check_gpu()

