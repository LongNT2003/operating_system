class FIFOPageReplacement:
    def __init__(self, capacity):
        self.capacity = capacity
        self.pages = []  # Represents the pages currently in memory (page frames)
        self.num_fault=0
        self.process=[]
    def page_fault(self, page):
        if page not in self.pages:
            if len(self.pages) < self.capacity:
                # If there is space in memory, just add the page
                self.pages.append(page)
            else:
                # If memory is full, remove the oldest page (first-in)
                removed_page = self.pages.pop(0)
                print(f"Page fault: Page {removed_page} is replaced by Page {page}")
                self.pages.append(page)
                self.num_fault+=1
        self.process.append(self.pages)

    def print_memory_state(self):
        current_state = [str(page) if page is not None else '_' for page in self.pages]
        print("Current memory state:", current_state)
    def fault_return(self):
        return self.num_fault

if __name__=='__main__':
    # Example usage:
    fifo = FIFOPageReplacement(3)  # Setting capacity to 3 for demonstration purposes

    # Page accesses
    fifo.page_fault(1)
    fifo.print_memory_state()

    fifo.page_fault(2)
    fifo.print_memory_state()

    fifo.page_fault(3)
    fifo.print_memory_state()

    fifo.page_fault(1)
    fifo.print_memory_state()

    fifo.page_fault(4)
    fifo.print_memory_state()
