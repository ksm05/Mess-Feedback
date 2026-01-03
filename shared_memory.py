from multiprocessing import shared_memory

SHM_NAME = "mess_feedback_shm"
SHM_SIZE = 3 * 4  # 3 integers

def create_shared_memory():
    try:
        shm = shared_memory.SharedMemory(name=SHM_NAME, create=True, size=SHM_SIZE)
        for i in range(0, SHM_SIZE, 4):
            shm.buf[i:i+4] = (0).to_bytes(4, 'little')
    except FileExistsError:
        shm = shared_memory.SharedMemory(name=SHM_NAME)
    return shm
