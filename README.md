# Yolov10-predict
三行代码yolov10目标检测教程

从结果上看，模型延迟方面有较大的提升，相对于参数来说，AP提升相比v9较为微小，简单来说就是模型更适合端侧部署，因为推理延迟时间低。

！！！重要说明：YOLOv10的代码参考ultralytics （YOLOv8）and RT-DETR，**很多命令都可以复用ultralytics （YOLOv8）的**。

（1）克隆YOLOv10项目地址：
1. 在github上找到项目地址，用git clone 方法
或者2. 下载zip文件再解压

（2）安装运行代码需要的Python环境
四行命令，使用Anaconda安装环境，我试了一下直接用Python的虚拟环境也可以。

conda create -n yolov10 python=3.9
conda activate yolov10
pip install -r requirements.txt
pip install -e .

（图2-6）在Anaconda prompt命令行安装并编译环境。

YOLOv10延续了YOLOv8的方式，将项目封装成命令的方式进行训练和测试。

（3）代码使用

app.py文件是用gradio写了个界面，（图7）运行该脚本，在浏览器打开网址，就能看到界面（图8）。

使用时，不知道什么原因报错，看issue里也没人提这个报错，我也不需要这个界面，就没去debug这个错误。各位可以试试自己的电脑会不会报错。

（图9）3行推理测试代码

支持对图片视频等进行检测。save=True参数是控制保存输出图片的，输出图片或视频会保存到runs\detect\predict路径下。

（图10）代码：提取结果中的检测框类别和坐标，并按固定大小展示检测结果。

（图11）输出结果
