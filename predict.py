from ultralytics import YOLOv10

# 从预训练模型加载YOLOv10
model = YOLOv10.from_pretrained('jameslahm/yolov10n')
# 或者，你可以下载模型权重并从本地加载：
# wget https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10{n/s/m/b/l/x}.pt
# model = YOLOv10('weights\yolov10n.pt')

# 对指定图像进行预测，并保存结果
results = model.predict(source=r'images\test.jpg', save=True)

# 对指定视频进行预测，并保存结果
# results = model.predict(source=r'videos\00001.mp4', save=True)