# Dữ liệu mẫu (Tạm thời thay cho Database)
MOCK_DEALERS = [
    {"name": "An Phát", "city": "TPHCM", "rating": 4.5, "type": "pesticide"},
    {"name": "Bình Minh", "city": "Hà Nội", "rating": 4.8, "type": "fertilizer"},
    {"name": "Phước Lộc", "city": "TPHCM", "rating": 3.9, "type": "pesticide"},
    {"name": "Vĩnh Cửu", "city": "TPHCM", "rating": 4.1, "type": "fertilizer"}
]

# Hàm LỌC ĐẠI LÝ (dùng **kwargs)
def find_dearlers(search_criteria: dict = None):
  