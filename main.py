import cv2
from ultralytics import YOLO
import os
import configparser

# Đường dẫn stream.
stream_url = "http://YOUR_CAMERA_IP:PORT/webcam/?action=stream"

# Đường dẫn model.
model_path = os.path.join("model", "best.onnx")
config_path = os.path.join("model", "settings.cfg")

def load_config():
    config = configparser.ConfigParser()
    conf_threshold = 0.15
    use_gpu = False
    
    if os.path.exists(config_path):
        try:
            config.read(config_path)
            if 'general' in config:
                conf_threshold = config.getfloat('general', 'default_conf_threshold', fallback=0.15)
                use_gpu = config.getboolean('general', 'use_gpu', fallback=False)
        except Exception as e:
            print(f"Lỗi khi đọc file config: {e}")
            
    return conf_threshold, use_gpu

def main():
    # Load cấu hình
    conf_threshold, use_gpu = load_config()
    print(f"Cấu hình: Threshold={conf_threshold}, GPU={'Bật' if use_gpu else 'Tắt'}")

    # Load model YOLOv8 (ONNX)
    try:
        # Nếu dùng GPU với ONNX, cần onnxruntime-gpu
        device = '0' if use_gpu else 'cpu'
        model = YOLO(model_path, task='detect')
        print(f"Đã load model từ: {model_path}")
    except Exception as e:
        print(f"Không thể load model: {e}")
        return

    # Mở stream video
    cap = cv2.VideoCapture(stream_url)

    if not cap.isOpened():
        print(f"Không thể mở stream URL: {stream_url}")
        print("Vui lòng kiểm tra lại kết nối hoặc địa chỉ camera.")
        return

    window_name = "SepRinder - Camera AI Detect"
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)

    print("Bắt đầu chạy AI camera... Nhấn 'q' để thoát.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Mất kết nối stream hoặc đang chờ dữ liệu...")
            # Thử reconnect hoặc chờ một chút
            cv2.waitKey(1000)
            cap.open(stream_url)
            continue

        # Chạy detection
        # conf xác định ngưỡng tin cậy
        results = model.predict(frame, conf=conf_threshold, device=device, verbose=False)

        # Vẽ kết quả lên frame (sử dụng hàm plot tích hợp của YOLOv8)
        annotated_frame = results[0].plot()

        # Hiển thị cửa sổ
        cv2.imshow(window_name, annotated_frame)

        # Thoát nếu nhấn phím 'q' hoặc đóng cửa sổ
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
        # Kiểm tra nếu cửa sổ bị đóng (tùy thuộc vào backend của OpenCV)
        if cv2.getWindowProperty(window_name, cv2.WND_PROP_VISIBLE) < 1:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()