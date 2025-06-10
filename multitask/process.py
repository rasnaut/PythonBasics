from concurrent.futures import ProcessPoolExecutor
import os
import time

def worker(task_id, sleep_time):
    print(f"[Worker {task_id}] PID={os.getpid()} start")
    time.sleep(sleep_time)
    print(f"[Worker {task_id}] PID={os.getpid()} end after {sleep_time}s")
    return f"Result from task {task_id}"

def main():
    print(f"[Main process] PID={os.getpid()}")

    # Создаем пул процессов (максимум 2 параллельных процесса)
    with ProcessPoolExecutor(max_workers=2) as executor:
        # Отправляем задачи в пул
        futures = [
            executor.submit(worker, "A", 2),
            executor.submit(worker, "B", 3),
            executor.submit(worker, "C", 1),
            executor.submit(worker, "D", 2),
        ]

        # Основной поток может что-то делать
        print("[Main process] Doing other stuff while workers run...")

        # Ждем и собираем результаты
        for future in futures:
            result = future.result()  # Блокирует до завершения
            print("[Main process] Got:", result)

    print("[Main process] All tasks done!")

if __name__ == "__main__":
    main()
