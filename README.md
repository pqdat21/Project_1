Vấn đề Lập kế hoạch Dự án có Ràng buộc Tài nguyên

Một công ty có một dự án nhỏ bao gồm nhiều công việc nhỏ khác nhau. Mỗi công việc đòi hỏi một số loại tài nguyên. Một danh sách tất cả các tài nguyên cùng với khung thời gian sẵn có của chúng được cung cấp để giúp tiến triển trong dự án.

Chương trình nhận một tệp Excel làm đầu vào và tạo ra biểu đồ Gantt của các công việc, nhiệm vụ và lịch tài nguyên.

Mô tả chi tiết
Đặc điểm chính của Công việc
Yêu cầu Tài nguyên: trong phạm vi hiện tại của dự án, thuộc tính này đề cập đến danh sách các chất lượng mà nhân viên thực hiện công việc này phải đáp ứng
Tiền đề Công việc: danh sách tất cả các công việc khác phải hoàn thành trước khi công việc này kết thúc
Thời gian thực hiện Công việc: độ dài (theo giờ) của công việc

Đặc điểm chính của Tài nguyên
Chất lượng: danh sách tất cả các chất lượng mà một tài nguyên sở hữu, nếu chất lượng này đáp ứng Yêu cầu Tài nguyên của Công việc, tài nguyên này có thể được sử dụng cho công việc đó

Chi phí: Chi phí cho một tài nguyên được tính dựa trên các chất lượng mà tài nguyên đó sở hữu

Đặc điểm chính của Khung thời gian
Loại: có thể là một trong các loại ["Ca sáng", "Ca chiều", "Tăng ca", "Thời gian nghỉ"], mỗi loại cũng định nghĩa chi phí sử dụng một tài nguyên trong Khung thời gian này

Danh sách sẵn có của tất cả các tài nguyên: danh sách tất cả các tài nguyên có sẵn trong Khung thời gian này

Cách sử dụng: 
Chạy tuần tự các đoạn đã được code sẵn, kết quả cần thiết sẽ ở cuối bao gồm,
+ List các công việc đã được giao, chưa được giao, thời gian thực hiện, thời gian kết thúc của từng công việc.
+ Tổng chi phí sau khi thực hiện xong xếp lịch công việc
+ Tỉ lệ các task được giao 
