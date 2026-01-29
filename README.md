# AI Detection for 3D Printing Failures

Dự án sử dụng AI (YOLOv8) để phát hiện các lỗi phổ biến trong quá trình in 3D theo thời gian thực từ camera stream.

## Hướng dẫn sử dụng

Để chạy hệ thống phát hiện lỗi, bạn vui lòng thực hiện theo các bước sau:

### Bước 1: Huấn luyện và Xuất Model
Mở Google Colab và chạy file `train/train3Dfailure.ipynb`. 
- Quá trình này sẽ huấn luyện model và xuất ra file định dạng `.onnx`.
- File này được tối ưu hóa để chạy mượt mà trên nhiều thiết bị khác nhau.

### Bước 2: Thiết lập Model
Sau khi có file `.onnx` từ Google Colab:
- Chép file đó vào thư mục `model/` của dự án.
- Đảm bảo file có tên là `best.onnx` (hoặc bạn có thể chỉnh sửa đường dẫn trong file `main.py`).

### Bước 3: Cài đặt Môi trường
Cài đặt các thư viện cần thiết bằng cách chạy lệnh sau trong terminal:
```bash
pip install -r requirements.txt
```

### Bước 4: Cấu hình Camera Stream
Mở file `main.py` và tìm biến `stream_url` để cấu hình địa chỉ camera của bạn:
```python
# Đường dẫn stream camera (ví dụ: OctoPrint, Klipper hoặc IP Camera)
stream_url = "http://YOUR_CAMERA_IP:PORT/webcam/?action=stream"
```

### Bước 5: Chạy ứng dụng Real-time
Cuối cùng, chạy file `main.py` để khởi động giao diện phát hiện lỗi AI:
```bash
python main.py
```

### Kết quả demo
![AI Detection Result](media/result.gif)

## Các loại lỗi có thể phát hiện
Model hiện tại được cấu hình để nhận diện 5 loại lỗi chính:
- **Blobbing**: Lỗi vón cục nhựa.
- **Warping**: Lỗi cong vênh vật thể.
- **Layer shift**: Lỗi lệch tầng in.
- **Spaghetti**: Lỗi "mì ý" (rối nhựa).
- **Stringing**: Lỗi kéo sợi nhựa.

## Cấu hình bổ sung
Bạn có thể điều chỉnh độ nhạy trong file `model/settings.cfg`:
- `default_conf_threshold`: Ngưỡng tin cậy (mặc định 0.15).
- `use_gpu`: Chuyển sang `true` nếu máy bạn có hỗ trợ GPU và đã cài `onnxruntime-gpu`.