# backend/app/services/dealer_service.py

# Dữ liệu mẫu
MOCK_DEALER = [
  {"name": "An Phát", "city": "TPHCM", "rating": 4.5, "type": "pesticide"},
  {"name": "Bình Minh", "city": "Hà Nội", "rating": 4.8, "type": "fertilizer"},
  {"name": "Phước Lộc", "city": "TPHCM", "rating": 3.9, "type": "pesticide"},
  {"name": "Vĩnh Cửu", "city": "TPHCM", "rating": 4.1, "type": "fertilizer"}
]

# Hàm LỌC ĐẠI LÝ (Dùng **kwargs)
def find_dealer(search_criteria: dict = None ):
  # Nếu không có tiêu chí tìm kiếm, trả về tất cả
  if search_criteria is None:
    return MOCK_DEALER
  
  # Bắt đầu với danh sách gốc
  filtered_dealer = MOCK_DEALER
  
  # Vòng lặp qua các tiêu chí
  for key, value in search_criteria.items():
    # LOGIC QUAN TRỌNG: Lọc lại filtered_dealer dựa trên tiêu chí key=value
    # DÙNG LIST COMPREHENSION Ở ĐÂY
    if key == "city":
      filtered_dealer = [
        dealer for dealer in find_dealer if dealer['city'] == value
      ]