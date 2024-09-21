from ultralytics import YOLOv10
import cv2

# 从预训练模型加载YOLOv10
model = YOLOv10.from_pretrained('jameslahm/yolov10n')
# 或者，你可以下载模型权重并从本地加载：
# wget https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10{n/s/m/b/l/x}.pt
# model = YOLOv10('weights\yolov10n.pt')

# 对指定图像进行预测，并保存结果
results = model.predict(source=r'images\test.jpg', save=True)

# 打印每个检测到的对象的类别和坐标
for box in results[0].boxes:
    class_id = int(box.cls)
    class_name = model.names[class_id]
    coordinates = box.xyxy[0].tolist()
    confidence = float(box.conf)
    print(f"类别: {class_name}, 置信度: {confidence:.2f}, 坐标: {coordinates}")

def display_annotated_image(results, fixed_width=800):
    # 获取带有标注的图像
    annotated_image = results[0].plot()
    # 保持原始宽高比调整图像大小
    original_height, original_width = annotated_image.shape[:2]
    aspect_ratio = original_width / original_height
    # 计算相应的高度以保持宽高比
    fixed_height = int(fixed_width / aspect_ratio)
    # 调整标注图像的大小
    annotated_image = cv2.resize(annotated_image, (fixed_width, fixed_height), interpolation=cv2.INTER_AREA)
    # 显示标注后的图像
    cv2.imshow('Annotated Image', annotated_image)
    # 等待用户按键后关闭窗口
    cv2.waitKey(0)

# 调用函数显示标注后的图像
display_annotated_image(results)