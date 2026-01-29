# AI Detection for 3D Printing Failures

[English](#english) | [Tiếng Việt](#tiếng-việt)

---

## English

This project utilizes AI (YOLOv8) to detect common 3D printing failures in real-time from a camera stream.

### Usage Instructions

To run the failure detection system, please follow these steps:

#### Step 1: Training and Exporting the Model
Open Google Colab and run the `train/train3Dfailure.ipynb` file.
- This process will train the model and export it as an `.onnx` file.
- The exported file is optimized to run smoothly across different hardware.

#### Step 2: Model Setup
After obtaining the `.onnx` file from Google Colab:
- Copy the file into the `model/` directory of the project.
- Ensure the file is named `best.onnx` (alternatively, you can modify the model path in `main.py`).

#### Step 3: Environment Setup
Install the required libraries by running the following command in your terminal:
```bash
pip install -r requirements.txt
```

#### Step 4: Camera Stream Configuration
Open `main.py` and update the `stream_url` variable with your camera's address:
```python
# Camera stream URL (e.g., OctoPrint, Klipper, or IP Camera)
stream_url = "http://YOUR_CAMERA_IP:PORT/webcam/?action=stream"
```

#### Step 5: Run the Real-time Application
Launch the AI failure detection interface by running:
```bash
python main.py
```

### Demo Result
![AI Detection Result](media/result.gif)

### Detectable Failure Types
The current model is configured to recognize 5 main types of print failures:
- **Blobbing**: Accumulation of excess plastic.
- **Warping**: Object edges lifting or curling from the bed.
- **Layer shift**: Horizontal misalignment between print layers.
- **Spaghetti**: Disorganized plastic extrusion when the print fails to adhere.
- **Stringing**: Fine whiskers of plastic left between separate parts of the print.

### Additional Configuration
You can fine-tune the detection settings in `model/settings.cfg`:
- `default_conf_threshold`: Confidence threshold (default: 0.15).
- `use_gpu`: Set to `true` if your hardware supports GPU acceleration and `onnxruntime-gpu` is installed.

---

## Tiếng Việt

Dự án sử dụng AI (YOLOv8) để phát hiện các lỗi phổ biến trong quá trình in 3D theo thời gian thực từ camera stream.

### Hướng dẫn sử dụng

Để chạy hệ thống phát hiện lỗi, bạn vui lòng thực hiện theo các bước sau:

#### Bước 1: Huấn luyện và Xuất Model
Mở Google Colab và chạy file `train/train3Dfailure.ipynb`. 
- Quá trình này sẽ huấn luyện model và xuất ra file định dạng `.onnx`.
- File này được tối ưu hóa để chạy mượt mà trên nhiều thiết bị khác nhau.

#### Bước 2: Thiết lập Model
Sau khi có file `.onnx` từ Google Colab:
- Chép file đó vào thư mục `model/` của dự án.
- Đảm bảo file có tên là `best.onnx` (hoặc bạn có thể chỉnh sửa đường dẫn trong file `main.py`).

#### Bước 3: Cài đặt Môi trường
Cài đặt các thư viện cần thiết bằng cách chạy lệnh sau trong terminal:
```bash
pip install -r requirements.txt
```

#### Bước 4: Cấu hình Camera Stream
Mở file `main.py` và tìm biến `stream_url` để cấu hình địa chỉ camera của bạn:
```python
# Đường dẫn stream camera (ví dụ: OctoPrint, Klipper hoặc IP Camera)
stream_url = "http://YOUR_CAMERA_IP:PORT/webcam/?action=stream"
```

#### Bước 5: Chạy ứng dụng Real-time
Cuối cùng, chạy file `main.py` để khởi động giao diện phát hiện lỗi AI:
```bash
python main.py
```

### Kết quả demo
![AI Detection Result](media/result.gif)

### Các loại lỗi có thể phát hiện
Model hiện tại được cấu hình để nhận diện 5 loại lỗi chính:
- **Blobbing**: Lỗi vón cục nhựa.
- **Warping**: Lỗi cong vênh vật thể.
- **Layer shift**: Lỗi lệch tầng in.
- **Spaghetti**: Lỗi "mì ý" (rối nhựa).
- **Stringing**: Lỗi kéo sợi nhựa.

### Cấu hình bổ sung
Bạn có thể điều chỉnh độ nhạy trong file `model/settings.cfg`:
- `default_conf_threshold`: Ngưỡng tin cậy (mặc định 0.15).
- `use_gpu`: Chuyển sang `true` nếu máy bạn có hỗ trợ GPU và đã cài `onnxruntime-gpu`.