import asyncio

async def task_one():
  for i in range(3):
    print(f"[task_one] Step {i+1}/3: start")
    await asyncio.sleep(1)  # «Долгая» работа
    print(f"[task_one] Step {i+1}/3: end")
    return 42

async def task_two():
  for i in range(5):
    print(f"[task_two] I'm alive! {i+1}")
    await asyncio.sleep(0.5)

async def main():
  # Заряжаем две задачи параллельно
  task1 = asyncio.create_task(task_one())
  task2 = asyncio.create_task(task_two())

  print("Tasks started!")

  await task1
  await task2

  print("Part 1 Done!")

  await asyncio.gather(task_one(), task_two()) # Запускаем задачи параллельно (псевдо-параллельно)

  print("All tasks done!")

# Запускаем event loop
asyncio.run(main())