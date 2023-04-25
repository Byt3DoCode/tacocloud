# tacocloud
## 1. Phân tích nghiệp vụ
### 1. Phân rã quá trình nghiệp vụ
Các bước thực hiện:
- Nhận mã đơn hàng.
- Khởi tạo quá trình.
- Xác thực quyền vận đơn bằng token.
- Nếu xác thực thất bại, từ chối truy xuất mã đơn hàng.
- Kiểm tra mã đơn hàng tồn tại hay không.
- Nếu không tồn tại, từ chối truy xuất mã đơn hàng.
- Thông báo có vấn đề khi vận đơn.
- Lấy thông tin khách hàng dựa vào token.
- Lấy thông tin đơn hàng.
- Lấy thông tin các mặt hàng.
- Lấy thông tin người giao hàng.
- Lấy các trạng thái của đơn hàng.
- Gửi trả tất cả dữ liệu và kết thúc quá trình.
### 2. Loại bỏ những hành động không cần thiết
- *Nhận mã đơn hàng.*
- Khởi tạo quá trình.
- Xác thực quyền vận đơn bằng token.
- Nếu xác thực thất bại, từ chối truy xuất mã đơn hàng.
- Kiểm tra mã đơn hàng tồn tại hay không.
- Nếu không tồn tại, từ chối truy xuất mã đơn hàng.
- Thông báo có vấn đề khi vận đơn.
- Lấy thông tin khách hàng dựa vào token.
- Lấy thông tin đơn hàng.
- Lấy thông tin các mặt hàng.
- Lấy thông tin người giao hàng.
- Lấy các trạng thái của đơn hàng.
- Gửi trả tất cả dữ liệu và kết thúc quá trình.
### 3. Xác định ứng viên thực thể dịch vụ
Các thực thể:
![image](https://user-images.githubusercontent.com/101212623/231318314-42e0f055-66c5-4c64-8162-6ee3c100e776.png)
Các bước không bất khả tri sẽ được in đậm:  
- *Khởi tạo quá trình.*
- *Xác thực quyền vận đơn bằng token.*
- *Nếu xác thực thất bại, từ chối truy xuất mã đơn hàng.*
- *Kiểm tra mã đơn hàng tồn tại hay không.*
- *Nếu không tồn tại, từ chối truy xuất mã đơn hàng.*
- *Thông báo đơn hàng không tồn tại.*
- Lấy thông tin khách hàng dựa vào token.
- Lấy thông tin đơn hàng.
- Lấy thông tin các mặt hàng.
- Lấy thông tin người giao hàng.
- Lấy các trạng thái của đơn hàng.
- *Gửi trả tất cả dữ liệu và kết thúc quá trình.*

Từ đó ta sẽ có các ứng viên sau:  

![image](https://user-images.githubusercontent.com/66776021/232264184-34121b7d-4f90-4123-8a96-ef8445a11ded.png)

![image](https://user-images.githubusercontent.com/66776021/232264189-b72dd034-2f84-4be1-956c-5890ff4ac42f.png)

![image](https://user-images.githubusercontent.com/66776021/232264196-d9c3e3c8-0ead-4827-adc9-c05c7fbd5979.png)

![image](https://user-images.githubusercontent.com/66776021/232264207-1043adab-36ec-4704-8090-593907809622.png)

![image](https://user-images.githubusercontent.com/66776021/232264223-f013611b-4577-40bb-83c6-8e590285de86.png)

### 4. Xác định logic quy trình cụ thể
Các bước không bất khả tri:  
- Khởi tạo quá trình.
- Xác thực quyền vận đơn bằng token.
- Nếu xác thực thất bại, từ chối truy xuất mã đơn hàng.
- Kiểm tra mã đơn hàng tồn tại hay không.
- Nếu không tồn tại, từ chối truy xuất mã đơn hàng.
- Gửi trả tất cả dữ liệu và kết thúc quá trình.

Ta chọn “Khởi tạo quá trình” là ứng viên năng lực dịch vụ cho ứng viên dịch vụ “TheoDoiTrangThaiDonHang”.
![image](https://user-images.githubusercontent.com/66776021/232264174-bbc3298b-9039-47f3-81ea-94bd3ba70ff8.png)

### 5. Áp dụng hướng dịch vụ
### 6. Xác định ứng viên thành phần dịch vụ
![image](https://user-images.githubusercontent.com/66776021/232264151-7b25acc8-3f95-4e7d-b9c1-23dac785f4ed.png)
### 7. Phân tích yêu cầu xử lý
### 8. Xác định ứng viên dịch vụ tiện tích
Còn lại bước bất trả tri là “Thông báo có vấn đề khi vận đơn”, ta sẽ rút gọn còn “Gửi thông báo qua gmail” và cho vào trong ứng viên dịch vụ tiện ích gọi là “ThongBao”.

![image](https://user-images.githubusercontent.com/66776021/232264261-dda521f9-587f-47ff-a415-0ff91b63fcdc.png)
### 9. Xác định các ứng viên vi dịch vụ
Bước "Xác thực khách hàng".

![image](https://user-images.githubusercontent.com/66776021/232264540-d07c7e68-f4ce-400f-811a-dc3fbeea3d95.png)

### 10. Áp dụng hướng dịch vụ
### 11. Xem xét lại các ứng viên thành phần dịch vụ
![image](https://user-images.githubusercontent.com/66776021/232264531-edc8a69a-11a3-4de1-9b10-7b7e4682f4db.png)
### 12. Xem xét cách thức nhóm ứng viên chức năng

## 2. Công nghệ sử dụng
- IDE: Elipse, Intellji (những IDE này có những chức năng phục vụ cho webservice được tích hợp sẵn)
- Platform: JDK, Javascript (có những công cụ phù hợp cho việc làm web)
- Server: Tomcat Apache Server (Server dễ thiết lập và dễ sửa dụng)
- Framework: Spring Framework (cung cấp một mô hình lập trình và cấu hình toàn diện cho các ứng dụng web dựa trên Java hiện đại)
- Database: MySQL (đơn giản, dễ quản lý, dễ dùng, dễ sửa chữa)
- Test tool: Selenium, Junit
- Microservice: kubernetes, minikube
- Virtual machine: docker desktop, virtualbox
