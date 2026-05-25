raw_batch = " LAP-VN-23-001 ; mou-us-24-012 ; KEY-vn-23-abc ; lap-JP-22-045 ; MOn-vn-24-099 "

while True:
    print("===== HỆ THỐNG GIẢI MÃ DỮ LIỆU KHO HÀNG =====")
    print("1. Hiển thị chuỗi mã vạch gốc")
    print("2. Giải mã, làm sạch và in báo cáo kiểm kê")
    print("3. Tra cứu nhanh theo đuôi Serial")
    print("4. Thoát chương trình")
    
    choice = input("Nhập lựa chọn của bạn (1-4): ").strip()
    
    if choice == '1':
        print("--- Chuỗi dữ liệu gốc ---")
        print(raw_batch)
        
    elif choice == '2':
        print("--- Báo cáo kiểm kê ---")
        print(f"{'MÃ SP':<8} | {'XUẤT XỨ':<8} | {'NĂM SX':<8} | {'SERIAL':<8} | {'TRẠNG THÁI'}")
        print("-" * 65)
        
        total_products = 0
        valid_products = 0
      
        start_idx = 0
        while start_idx < len(raw_batch):
            end_idx = raw_batch.find(';', start_idx)
            if end_idx == -1:
                end_idx = len(raw_batch)
         
            item_str = raw_batch[start_idx:end_idx].strip().upper()
          
            if item_str != "":
                idx_dash_1 = item_str.find('-')
                if idx_dash_1 != -1:
                    prod_type = item_str[0:idx_dash_1].strip()
                    
                    idx_dash_2 = item_str.find('-', idx_dash_1 + 1)
                    if idx_dash_2 != -1:
                        country = item_str[idx_dash_1 + 1:idx_dash_2].strip()
                        
                        idx_dash_3 = item_str.find('-', idx_dash_2 + 1)
                        if idx_dash_3 != -1:
                            year_short = item_str[idx_dash_2 + 1:idx_dash_3].strip()
                            year = "20" + year_short
                            
                            serial = item_str[idx_dash_3 + 1:].strip()
                            if serial.isdigit():
                                status = "Pass"
                                valid_products += 1
                            else:
                                status = "Lỗi Serial - Reject"
                                
                            total_products += 1
                            print(f"{prod_type:<8} | {country:<8} | {year:<8} | {serial:<8} | {status}")
            start_idx = end_idx + 1
            
        print("-" * 65)
        print(f"Tổng kết: Đã giải mã thành công {valid_products} sản phẩm hợp lệ / Tổng số {total_products} sản phẩm.")

    elif choice == '3':
        search_query = input("Nhập 2 số cuối của Serial cần tìm: ").strip()
        found = False
        
        print("--- Kết quả tìm kiếm ---")
     
        start_idx = 0
        while start_idx < len(raw_batch):
            end_idx = raw_batch.find(';', start_idx)
            if end_idx == -1:
                end_idx = len(raw_batch)
                
            item_str = raw_batch[start_idx:end_idx].strip().upper()
            
            if item_str != "":
                idx_dash_1 = item_str.find('-')
                if idx_dash_1 != -1:
                    prod_type = item_str[0:idx_dash_1].strip()
                    
                    idx_dash_2 = item_str.find('-', idx_dash_1 + 1)
                    if idx_dash_2 != -1:
                        country = item_str[idx_dash_1 + 1:idx_dash_2].strip()
                        
                        idx_dash_3 = item_str.find('-', idx_dash_2 + 1)
                        if idx_dash_3 != -1:
                            year_short = item_str[idx_dash_2 + 1:idx_dash_3].strip()
                            year = "20" + year_short
                            serial = item_str[idx_dash_3 + 1:].strip()
                            
                            if serial.isdigit():
                                status = "Pass"
                            else:
                                status = "Lỗi Serial - Reject"
                           
                            if serial[-2:] == search_query:
                                print(f"- Loại SP: {prod_type}, Xuất xứ: {country}, Năm SX: {year}, Serial: {serial}, Trạng thái: {status}")
                                found = True
            
            start_idx = end_idx + 1
            
        if found == False:
            print("Không tìm thấy sản phẩm phù hợp.")

    elif choice == '4':
        print("Đóng ca kiểm kho. Chào tạm biệt!")
        break
    else:
        print("Chức năng không tồn tại, vui lòng nhập số từ 1-4!")