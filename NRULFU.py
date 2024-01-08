'''
I. NRU (Not Recently Used)
Thuật toán NRU (Not Recently Used) là một chiến lược thay thế trang đơn giản được sử dụng trong quản lý bộ nhớ ảo. Mục tiêu chính của nó là quản lý các trang trong bộ nhớ khi có yêu cầu truy nhập trang mới và không còn không gian trống trong bộ nhớ. Cách thức hoạt động của NRU có thể được mô tả như sau:

Nguyên tắc hoạt động:

1. Khởi tạo: Bắt đầu với một bộ nhớ (frame) rỗng hoặc đã chứa một số trang nhất định.
2. Xử lý truy nhập: Khi một trang mới được truy cập, thuật toán sẽ kiểm tra xem trang đó đã có trong bộ nhớ chưa.
- Nếu trang đã có mặt trong bộ nhớ và được truy cập gần đây, không có lỗi trang nào được ghi nhận và quá trình tiếp tục mà không cần thay đổi gì thêm.
- Nếu trang không có mặt trong bộ nhớ và còn chỗ trống, trang mới này sẽ được thêm vào bộ nhớ mà không cần thay thế trang nào cả.
- Nếu trang không có mặt trong bộ nhớ và không còn chỗ trống, một lỗi trang (page fault) sẽ xảy ra.
3. Thay thế trang: Khi xảy ra lỗi trang, trang được truy cập gần đây nhất (cờ referenced là 0) sẽ được loại bỏ để nhường chỗ cho trang mới. Trong trường hợp có nhiều trang có cùng giá trị của cờ referenced, NRU có thể sử dụng các tiêu chí khác, như trang có ít lần sử dụng nhất (cờ modified là 0) hoặc có ít lần truy cập nhất.
4. Cập nhật hàng đợi: Sau khi thay thế, trang mới được thêm vào cuối hàng đợi. Quá trình này lặp lại mỗi khi có truy cập trang mới.

Ưu điểm:

- Đơn giản: NRU có cấu trúc đơn giản và dễ triển khai so với một số giải thuật phức tạp.
- Hiệu suất tốt trong môi trường đơn giản: NRU có thể hoạt động hiệu quả trong môi trường không đòi hỏi theo dõi chi tiết lịch sử sử dụng của từng trang.

Nhược điểm:

- Khả năng xếp hạng không linh hoạt: NRU có thể không phản ánh chính xác mức độ quan trọng của từng trang trong quyết định thay thế. Việc chỉ sử dụng cờ referenced và cờ modified có thể làm giảm chính xác của thuật toán.
- NRU có thể không đủ linh hoạt để xử lý tốt trong các trường hợp sử dụng bộ nhớ đặc biệt hoặc phức tạp.

II. LFU (Least Frequently Used)
Thuật toán LFU (Least Frequently Used) là một chiến lược thay thế trang dựa trên việc ưu tiên loại bỏ các trang ít được sử dụng nhất. Cứ mỗi lần trang được truy cập, đếm của trang đó sẽ tăng lên. Khi cần thay thế trang, thuật toán sẽ chọn trang có đếm thấp nhất để loại bỏ.

Nguyên tắc hoạt động:

- Khởi tạo: Gán đếm của mỗi trang bằng 0.
- Xử lý truy nhập: Mỗi khi trang được truy cập, đếm của trang đó tăng lên.
- Thay thế trang: Khi cần thay thế, chọn trang có đếm thấp nhất để loại bỏ.

Ưu điểm:

-Ưu tiên loại bỏ các trang ít được sử dụng, giúp giảm lỗi trang.

Nhược điểm:

- Cần duy trì một đếm cho mỗi trang, điều này có thể tốn chi phí.
- Có thể không hiệu quả nếu có những trang được truy cập thường xuyên trong một khoảng thời gian ngắn, sau đó không được truy cập trong thời gian dài (đặc tính không đều về tần suất sử dụng).

Tóm lại, cả NRU và LFU đều là các chiến lược thay thế trang đa dạng, với mục tiêu giảm thiểu lỗi trang và tối ưu hóa việc sử dụng bộ nhớ, mỗi thuật toán đều có ưu và nhược điểm của riêng mình.
'''
def nru(pages, frames):
    memory, faults, mem_states = [], 0, []
    last_accessed = {} 
    is_fault=0
    for page in pages:
        if page not in memory:
            if len(memory) < frames:
                memory.append(page)
            else:
                oldest = max([(last_accessed.get(page, 0), page) for page in memory])  # Use get() to handle missing keys
                memory.remove(oldest[1])
                memory.append(page)
            faults += 1
            is_fault=1
        else:
            is_fault=0
        last_accessed[page] = 0  
        mem_states.append([list(memory),is_fault])
    return faults, mem_states

def lfu(pages, frames):
    memory, faults, mem_states = [], 0, []
    freq = {}
    is_fault=0
    for page in pages:
        if page not in memory:
            if len(memory) < frames:
                memory.append(page)
            else:
                least_recently_used = min([(freq[page], page) for page in memory])
                memory.remove(least_recently_used[1])
                memory.append(page)
            freq[page] = 0
            faults += 1
            is_fault=1
        else:
            is_fault=0
        freq[page] += 1
        mem_states.append([list(memory),is_fault])
    return faults, mem_states
if __name__=='__main__':
    # Input data
    # pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
    pages = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
    frames = 3

    # Run simulations
    nru_faults, nru_states = nru(pages, frames)
    lfu_faults, lfu_states = lfu(pages, frames)

    print("NRU", nru_faults, nru_states)
    print("LFU", lfu_faults, lfu_states)
