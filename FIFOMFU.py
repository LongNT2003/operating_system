#THUẬT TOÁN THAY THẾ TRANG: FIFO + MFU
#1. FIFO
'''
I) Lý thuyết:
Page-replacement algorthm
-Chọn fram của process sẽ được thay thế trang nhớ
-Mục tiêu: số lương page-fault nhỏ nhất;
-Được đánh giá bằng cách thực thi giải thuật đói với mỗi chuỗi tham chiếu bộ nhớ( memory reference string) và xác định số lần xảy ra page fault.


1. FIFO:
Cần biết được:- Số khung trang, tình trạng ban đầu, chuỗi tham chiếu.
Hướng tiếp cận: Ghi nhận thời điểm một trang được mang vào bộ nhớ chính. Khi cần thay thế trang, trang ở trong bộ nhớ lâu nhất sẽ được chọn.

2. MFU:
Giải thuật thay thế trang được dùng thường xuyên nhất (the most frequently used (MFU) page-replacement algorithm) thay thế trang có giá trị 
đếm lớn nhất, nghĩa là trang được sử dụng nhiều nhất.
'''
from collections import deque
from collections import defaultdict

def fifo_page_replacement(pages, memory_size):
    memory = deque(maxlen=memory_size)
    page_faults = 0
    state=[]
    is_fault=0
    for page in pages:
        if page not in memory:
            page_faults += 1
            if len(memory) == memory_size:
                # If memory is full, remove the oldest page (front of the queue)
                removed_page = memory.popleft()
                

            # Add the new page to the back of the queue (end of the memory)
            memory.append(page)
            is_fault=1
        else:
            is_fault=0
            print(f"Page {page} already in memory.")
        state.append([list(memory),is_fault])
        print(list(memory))
        print(page_faults)

    return page_faults,state

def mfu_page_replacement(pages, memory_size):
    memory = []
    page_frequency = defaultdict(int)
    page_faults = 0
    state=[]
    is_fault=0
    for page in pages:
        page_frequency[page] += 1

        if page not in memory:
            page_faults += 1
            is_fault=1

            if len(memory) == memory_size:
                # If memory is full, find the page with the highest frequency
                replace_page = max(memory, key=lambda x: page_frequency[x])
                memory.remove(replace_page)
                

            # Add the new page to memory
            memory.append(page)
        

        else:
            is_fault=0
            print(f"Page {page} already in memory.")
        state.append([list(memory),is_fault])
        print(memory)
        print(page_faults)

    return page_faults,state
if __name__=='__main__':
    # Example usage for MFU:
    # https://www.geeksforgeeks.org/most-frequently-used-mfu-algorithm-in-operating-system/
    # pages = [7, 0, 1 , 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1]
    # memory_size = 4

    # total_page_faults = mfu_page_replacement(pages, memory_size)
    # print(f"Total number of page faults: {total_page_faults}")

    # Example usage for FIFO:
    #https://www.geeksforgeeks.org/page-replacement-algorithms-in-operating-systems/
    pages = [1, 3, 0, 3, 5, 6, 3]
    memory_size = 3

    total_page_faults,state = fifo_page_replacement(pages, memory_size)
    print(f"Total number of page faults: {total_page_faults}")
    print(state)
