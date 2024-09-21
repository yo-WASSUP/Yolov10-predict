from ultralytics import YOLOv10
import cv2

# 从预训练模型加载YOLOv10
model = YOLOv10.from_pretrained('jameslahm/yolov10n')
# 或者，你可以下载模型权重并从本地加载：
# wget https://github.com/THU-MIG/yolov10/releases/download/v1.1/yolov10{n/s/m/b/l/x}.pt
# model = YOLOv10('weights\yolov10n.pt')

# 打开视频文件
video_path = r'videos\00001.mp4'
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print(f"Error: Unable to open video file '{video_path}'. Please check if the file exists and the path is correct.")
    exit()

# 获取视频的属性
fps = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 创建VideoWriter对象，用于保存处理后的视频
output_path = 'output.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # 对当前帧进行预测
    results = model.predict(source=frame, save=False)

    # 在帧上绘制检测结果
    annotated_frame = results[0].plot()

    # 显示带有检测结果的帧
    cv2.imshow('YOLOv10 Video Detection', annotated_frame)

    # 将带有检测结果的帧写入输出视频
    out.write(annotated_frame)

    # 按 'q' 键退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
out.release()
cv2.destroyAllWindows()

print(f"处理后的视频已保存为 {output_path}")