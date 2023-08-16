# Sử dụng một hình ảnh cơ bản Python
FROM python:3.10

# Đặt thư mục làm thư mục làm việc
WORKDIR /CameraAI

# Sao chép tệp requirements.txt vào thư mục làm việc
COPY requirements.txt .

# Cài đặt các gói từ requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép tất cả mã nguồn vào thư mục làm việc trong hình ảnh
COPY . .

# Expose cổng mà ứng dụng của bạn chạy trên
EXPOSE 5000

# Chạy ứng dụng
CMD [ "python", "app.py" ]
