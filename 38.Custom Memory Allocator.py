# -----------------------------
# Memory Block Class
# -----------------------------
class MemoryBlock:

    def __init__(self, start, size, free=True):
        self.start = start
        self.size = size
        self.free = free

    def __str__(self):
        status = "Free" if self.free else "Allocated"
        return f"Start: {self.start}, Size: {self.size}, Status: {status}"


# -----------------------------
# Custom Memory Allocator
# -----------------------------
class MemoryAllocator:

    def __init__(self, total_memory):

        self.total_memory = total_memory
        self.blocks = [MemoryBlock(0, total_memory, True)]

    # -----------------------------
    # Allocate Memory (First Fit)
    # -----------------------------
    def malloc(self, size):

        for block in self.blocks:

            if block.free and block.size >= size:

                start_address = block.start

                # Split block
                new_block = MemoryBlock(block.start + size,
                                        block.size - size,
                                        True)

                block.size = size
                block.free = False

                if new_block.size > 0:
                    self.blocks.insert(self.blocks.index(block) + 1, new_block)

                print(f"Allocated {size} bytes at address {start_address}")
                return start_address

        print("Memory allocation failed")
        return None

    # -----------------------------
    # Free Memory
    # -----------------------------
    def free(self, address):

        for block in self.blocks:

            if block.start == address:

                block.free = True
                print(f"Freed memory at address {address}")
                self.merge()
                return

        print("Invalid address")

    # -----------------------------
    # Merge Adjacent Free Blocks
    # -----------------------------
    def merge(self):

        i = 0

        while i < len(self.blocks) - 1:

            if self.blocks[i].free and self.blocks[i+1].free:

                self.blocks[i].size += self.blocks[i+1].size
                self.blocks.pop(i+1)

            else:
                i += 1

    # -----------------------------
    # Display Memory State
    # -----------------------------
    def show_memory(self):

        print("\nMemory Blocks:\n")

        for block in self.blocks:
            print(block)

        print()


# -----------------------------
# Main Program
# -----------------------------
def main():

    allocator = MemoryAllocator(100)

    while True:

        print("\nCustom Memory Allocator")
        print("1. Allocate Memory")
        print("2. Free Memory")
        print("3. Show Memory")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":

            size = int(input("Enter size: "))
            allocator.malloc(size)

        elif choice == "2":

            address = int(input("Enter address to free: "))
            allocator.free(address)

        elif choice == "3":

            allocator.show_memory()

        elif choice == "4":

            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
