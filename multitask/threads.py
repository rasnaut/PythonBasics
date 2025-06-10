from concurrent.futures import ThreadPoolExecutor
import time

def worker(task_id, sleep_time):
    print(f"[{task_id}] Start working")
    time.sleep(sleep_time)
    print(f"[{task_id}] Finished after {sleep_time} seconds")
    return f"Result from task {task_id}"

def main():
    with ThreadPoolExecutor(max_workers=3) as executor:
        # Отправляем несколько задач с разной "длительностью"
        futures = [
            executor.submit(worker, "A", 2),
            executor.submit(worker, "B", 3),
            executor.submit(worker, "C", 1),
            executor.submit(worker, "D", 2),
        ]

        # Основной поток делает что-то ещё
        print("Main thread is free to do other things!")

        # Получаем результаты по мере готовности (не обязательно в том же порядке)
        for future in futures:
            result = future.result()  # блокирует для каждого future
            print("Got:", result)

if __name__ == "__main__":
    main()
