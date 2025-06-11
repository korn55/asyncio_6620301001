import time
from multiprocessing import Process
from datetime import datetime

def make_burger(student_id):
    start_time = time.time()
    start_str = datetime.now().strftime('%H:%M:%S')
    print(f"[{datetime.now().strftime('%H:%M:%S')}] เริ่มทำเบอร์เกอร์ให้นักเรียนคนที่ {student_id}")
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] 1. ทอดเบอร์เกอร์...")
    time.sleep(5)

    print(f"[{datetime.now().strftime('%H:%M:%S')}] 2. ทอดไก่...")
    time.sleep(5)

    print(f"[{datetime.now().strftime('%H:%M:%S')}] 3. ใส่ผักและชีส...")
    time.sleep(5)

    print(f"[{datetime.now().strftime('%H:%M:%S')}] 4. ห่อเบอร์เกอร์...")
    time.sleep(5)

    end_time = time.time()
    end_str = datetime.now().strftime('%H:%M:%S')
    duration = end_time - start_time

    print(f"[{end_str}] ✅ นักเรียนคนที่ {student_id} เสร็จแล้ว! ใช้เวลา {duration} วินาที")
def main():
    start = time.time()
    start_str = datetime.now().strftime('%H:%M:%S')
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] 🍔 เริ่มกระบวนการทำเบอร์เกอร์ทั้งหมด\n")
    
    processes = []
    for i in range(1, 6):
        p = Process(target=make_burger, args=(i,))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()
    
    end = time.time()
    print(f"[{datetime.now().strftime('%H:%M:%S')}] รวมเวลาทั้งหมด: {end - start:.2f} วินาที")

if __name__ == "__main__":
    main()
