# 🐍 Шпаргалка: Асинхронность, ThreadPool, ProcessPool в Python

---

## ⚡ Общий обзор

| Механизм               | Принцип работы                                                      | Когда использовать?                               |
|------------------------|---------------------------------------------------------------------|---------------------------------------------------|
| **`async/await`**      | Один поток (event loop). Задачи уступают управление друг другу.     | Много I/O (сеть, файлы), UI, не блокирует поток. |
| **ThreadPoolExecutor** | Несколько потоков в одном процессе, общая память (GIL).             | I/O-bound задачи, когда нужен параллелизм ожидания. |
| **ProcessPoolExecutor**| Несколько процессов, каждый со своим GIL. Настоящий параллелизм.    | CPU-bound задачи, вычисления, обработка больших массивов. |

---

## 🔎 Отличия по параллельности

| Механизм         | Реальный параллелизм?      | Особенности                                     |
|------------------|----------------------------|-------------------------------------------------|
| **async**        | Нет, один поток            | Задачи чередуются, не блокируя UI.              |
| **ThreadPool**   | Почти, но GIL мешает       | Хорош для I/O, не ускоряет CPU.                 |
| **ProcessPool**  | Да, разные процессы        | Настоящий многопроцессный параллелизм.          |

---

## 🚀 Ключевые моменты

✅ **`async/await`**  
- Корутину нужно «оживить» через `await` или `asyncio.run`.  
- Работает с `asyncio`, `aiohttp` и другими асинхронными библиотеками.

✅ **ThreadPool**  
- `executor.submit()` сразу запускает задачу (не нужно `await`).  
- Общая память — нужно быть осторожным (использовать `Lock` и т.д.).  
- Отлично подходит для задач с сетью, файлами (например, загрузка веб-страниц).

✅ **ProcessPool**  
- `executor.submit()` запускает задачу в **новом процессе**.  
- Процессы изолированы, данные сериализуются (`pickle`).  
- Отлично подходит для тяжёлых вычислений (ML, анализ больших данных).

---

## 🧩 Примеры кода

### 1️⃣ `async/await`

```python
import asyncio

async def main():
    print("Start")
    await asyncio.sleep(1)
    print("End")

asyncio.run(main())
