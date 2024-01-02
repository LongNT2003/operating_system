
def lru(pages, frames):
    memory, faults, mem_states = [], 0, []
    # Dùng dictionary để lưu vị trí sử dụng cuối cùng của các trang
    last_used = {}
    for i, page in enumerate(pages):
        if page not in memory:
            if len(memory) < frames:
                memory.append(page)
            else:
                # Tìm trang nào là LRU dựa trên vị trí sử dụng cuối cùng
                lru_page = min(memory, key=lambda x: last_used[x])
                memory.remove(lru_page)
                memory.append(page)
            faults += 1
        # Cập nhật vị trí sử dụng cuối cùng cho trang này
        last_used[page] = i
        mem_states.append(list(memory))  # Sao chép trạng thái hiện tại của bộ nhớ
    return faults, mem_states

# Sửa lại cài đặt cho thuật toán OPT để tránh lỗi khi trang không xuất hiện lại trong chuỗi
def optimal(pages, frames):
    memory, faults, mem_states = [], 0, []
    for i in range(len(pages)):
        if pages[i] not in memory:
            if len(memory) < frames:
                memory.append(pages[i])
            else:
                # Tìm trang không xuất hiện trong tương lai hoặc xuất hiện xa nhất
                furthest = -1
                to_replace = None
                for mem_page in memory:
                    if mem_page not in pages[i+1:]:
                        to_replace = mem_page
                        break
                    else:
                        next_use = pages[i+1:].index(mem_page)
                        if next_use > furthest:
                            furthest = next_use
                            to_replace = mem_page
                memory.remove(to_replace)
                memory.append(pages[i])
            faults += 1
        mem_states.append(list(memory))  # Sao chép trạng thái hiện tại của bộ nhớ
    return faults, mem_states

# Chuỗi truy cập trang và kích thước bộ nhớ
pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
# pages = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
frames = 3

# Chạy lại mô phỏng cho từng giải thuật
opt_faults, opt_states = optimal(pages, frames)
lru_faults, lru_states = lru(pages, frames)

print("OPT", opt_faults, opt_states)
print("LRU", lru_faults, lru_states)
