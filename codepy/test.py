import tkinter as tk

# Tạo cửa sổ tkinter
window = tk.Tk()
window.title("Listview Example")

# Tạo một Listbox widget
listbox = tk.Listbox(window)
listbox.pack(pady=10)

# Thêm một số mục vào Listbox
list_items = ['Giới hạn tốc độ (20 km/giờ)',
           'Giới hạn tốc độ (30 km/giờ)',
           'Giới hạn tốc độ (50 km/giờ)',
           'Giới hạn tốc độ (60 km/giờ)', 
           'Giới hạn tốc độ (70 km/giờ)',
           'Giới hạn tốc độ (80 km/giờ)',
           'Hết tốc độ giới hạn (80km/h)', 
           'Giới hạn tốc độ (100km/h)',
           'Giới hạn tốc độ (120km/h)',
           'Không được vượt qua',
           'Cấm vượt xe quá 3,5 tấn',
           'Quyền ưu tiên tại ngã tư',
           'Đường ưu tiên',
           'Năng suất',
           'Dừng lại',
           'Cấm xe cộ', 
           'Cấm xe cộ > 3,5 tấn',
           'Cấm vào',
           'Thận trọng chung',
           'Bên trái khúc cua nguy hiểm', 
           'Đường cong nguy hiểm bên phải',
           'Đường cong đôi',
           'Con đường gập ghềnh',
           'Đường trơn', 
           'Đường bị thu hẹp bên phải',
           'Làm đường',
           'Tín hiệu giao thông',
           'Người đi bộ', 
           'Trẻ em băng qua đường',
           'Băng qua đường bằng xe đạt',
           'Coi chừng băng/tuyết',
           'Động vật hoang dã băng qua', 
           'Tốc độ cuối + giới hạn vượt',
           'Rẽ phải về phía trước',
           'Rẽ trái phía trước',
           'Chỉ ở phía trước', 
           'Đi thẳng hoặc sang phải',
           'Đi thẳng hoặc sang trái',
            'Giữ bên phải',
           'Tiếp tục rời đi', 
           'Bùng binh bắt buộc',
           'Kết thúc không vượt qua',
           'cấm vượt xe > 3,5 tấn']
for item in list_items:
    listbox.insert(tk.END, item)

image_label = tk.Label(window)
image_label.pack(pady=10)

def on_select(event):
    # Lấy chỉ số của mục được chọn
    index = listbox.curselection()[0]
    # Lấy tên của hình ảnh tương ứng với mục được chọn
    image_name = listbox.get(index)
    # Load hình ảnh
    image_path = image_name
    selected_image = Image.open(image_path)
    selected_image.thumbnail((200, 200))  # Resize hình ảnh
    # Tạo một PhotoImage từ hình ảnh đã chọn
    selected_photo = ImageTk.PhotoImage(selected_image)
    # Hiển thị hình ảnh mới
    image_label.configure(image=selected_photo)
    image_label.image = selected_photo
window.mainloop()
