# ============================================================
# 15. ASYNC PROGRAMMING
# ============================================================
# Note: This file demonstrates async programming concepts.
# To run async code in a regular script, use asyncio.run()

import asyncio
import time

# ------------------------------------------------------------
# WHY ASYNC?
# ------------------------------------------------------------
"""
When your program waits for something (network, file, timer),
async lets other code run during that wait time.

Example: Making 3 API calls:
- Synchronous: 3 seconds (1 + 1 + 1)
- Async: 1 second (all run concurrently)
"""

# ------------------------------------------------------------
# BASIC ASYNC/AWAIT SYNTAX
# ------------------------------------------------------------
print("=== Basic Async/Await ===")

# Regular function


def regular_function():
    return "I'm regular"

# Async function (coroutine)


async def async_function():
    return "I'm async"

# Note: Calling async_function() returns a coroutine, not the result!
# You need to await it


async def demo_basic():
    print("Demo of basic async:")

    # await pauses this function until async_function completes
    result = await async_function()
    print(f"   Result: {result}")

# Run the async function
asyncio.run(demo_basic())

# ------------------------------------------------------------
# ASYNCIO.SLEEP VS TIME.SLEEP
# ------------------------------------------------------------
print("\n=== asyncio.sleep vs time.sleep ===")


async def demo_sleep():
    print("Starting...")

    # asyncio.sleep - allows other tasks to run during wait
    await asyncio.sleep(0.1)  # Non-blocking (for demo, using small delay)

    # time.sleep(1)  # BLOCKING - bad for async code!

    print("Finished!")

asyncio.run(demo_sleep())

# ------------------------------------------------------------
# RUNNING TASKS CONCURRENTLY
# ------------------------------------------------------------
print("\n=== Running Tasks Concurrently ===")


async def task(name, delay):
    """A simple task that waits and returns"""
    print(f"Task {name}: Starting (will take {delay}s)")
    await asyncio.sleep(delay)
    print(f"Task {name}: Done!")
    return f"Result from {name}"


async def demo_concurrent():
    print("Running tasks concurrently with gather():")

    start = time.time()

    # All tasks start at the same time!
    results = await asyncio.gather(
        task("A", 0.3),
        task("B", 0.2),
        task("C", 0.1)
    )

    elapsed = time.time() - start
    print(f"\nAll done in {elapsed:.1f} seconds!")
    print(f"Results: {results}")
    print("(Note: Total ~0.3s, not 0.6s)")

asyncio.run(demo_concurrent())

# ------------------------------------------------------------
# CREATING AND MANAGING TASKS
# ------------------------------------------------------------
print("\n=== Creating Tasks ===")


async def demo_tasks():
    # Create a task (starts running immediately)
    task1 = asyncio.create_task(task("Manual", 0.1))

    # Do other work while task runs
    print("Main: Doing other work...")

    # Wait for task to complete
    result = await task1
    print(f"Main: Got result: {result}")

asyncio.run(demo_tasks())

# ------------------------------------------------------------
# TASKGROUP (PYTHON 3.11+)
# ------------------------------------------------------------
print("\n=== TaskGroup (Python 3.11+) ===")


async def demo_taskgroup():
    """TaskGroup provides better error handling than gather"""
    try:
        async with asyncio.TaskGroup() as tg:
            # All tasks in the group
            task1 = tg.create_task(task("Group1", 0.1))
            task2 = tg.create_task(task("Group2", 0.1))

        # After the 'with' block, all tasks are done
        print(f"Results: {task1.result()}, {task2.result()}")
    except* Exception as eg:
        # Exception group handling
        print(f"Some tasks failed: {eg}")

asyncio.run(demo_taskgroup())

# ------------------------------------------------------------
# ASYNC QUEUES
# ------------------------------------------------------------
print("\n=== Async Queues ===")


async def producer(queue, items):
    """Puts items into the queue"""
    for item in items:
        await queue.put(item)
        print(f"Produced: {item}")
        await asyncio.sleep(0.05)  # Simulate work
    await queue.put(None)  # Signal end


async def consumer(queue, name):
    """Gets items from the queue"""
    while True:
        item = await queue.get()
        if item is None:
            queue.task_done()
            break
        print(f"Consumer {name} consumed: {item}")
        queue.task_done()


async def demo_queue():
    queue = asyncio.Queue()

    # Run producer and consumer concurrently
    await asyncio.gather(
        producer(queue, [1, 2, 3]),
        consumer(queue, "A")
    )

asyncio.run(demo_queue())

# ------------------------------------------------------------
# ASYNC WITH TIMEOUTS
# ------------------------------------------------------------
print("\n=== Timeouts ===")


async def slow_operation():
    """Simulates a slow operation"""
    await asyncio.sleep(5)
    return "Completed!"


async def demo_timeout():
    try:
        # wait_for with timeout
        result = await asyncio.wait_for(slow_operation(), timeout=0.1)
        print(f"Result: {result}")
    except asyncio.TimeoutError:
        print("Operation timed out! (as expected)")

asyncio.run(demo_timeout())

# ------------------------------------------------------------
# TO_THREAD - RUNNING SYNC CODE IN ASYNC
# ------------------------------------------------------------
print("\n=== to_thread - Running Sync Code ===")


def blocking_function():
    """A blocking function (like file I/O or CPU work)"""
    time.sleep(0.1)  # Simulates blocking work
    return "Blocking work done!"


async def demo_to_thread():
    print("Running blocking function in thread:")

    # Run blocking code in a thread pool
    result = await asyncio.to_thread(blocking_function)
    print(f"Result: {result}")
    print("(This didn't block the event loop!)")

asyncio.run(demo_to_thread())

# ------------------------------------------------------------
# ASYNC FOR LOOPS
# ------------------------------------------------------------
print("\n=== Async For Loops ===")


async def async_generator():
    """An async generator"""
    for i in range(3):
        await asyncio.sleep(0.05)
        yield i


async def demo_async_for():
    print("Iterating with async for:")
    async for value in async_generator():
        print(f"   Got: {value}")

asyncio.run(demo_async_for())

# ------------------------------------------------------------
# ASYNC CONTEXT MANAGERS
# ------------------------------------------------------------
print("\n=== Async Context Managers ===")


class AsyncResource:
    async def __aenter__(self):
        print("   Acquiring resource...")
        await asyncio.sleep(0.05)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print("   Releasing resource...")
        await asyncio.sleep(0.05)

    async def do_work(self):
        print("   Doing work...")


async def demo_async_with():
    print("Using async context manager:")
    async with AsyncResource() as resource:
        await resource.do_work()

asyncio.run(demo_async_with())

# ------------------------------------------------------------
# SEMAPHORES - LIMITING CONCURRENCY
# ------------------------------------------------------------
print("\n=== Semaphores (Limiting Concurrency) ===")


async def limited_task(semaphore, task_id):
    async with semaphore:  # Limits how many can run at once
        print(f"Task {task_id}: Working (holding semaphore)")
        await asyncio.sleep(0.1)
        print(f"Task {task_id}: Done")


async def demo_semaphore():
    # Only 2 tasks can run at once
    semaphore = asyncio.Semaphore(2)

    await asyncio.gather(
        limited_task(semaphore, 1),
        limited_task(semaphore, 2),
        limited_task(semaphore, 3),
        limited_task(semaphore, 4)
    )

asyncio.run(demo_semaphore())

# ------------------------------------------------------------
# BEST PRACTICES
# ------------------------------------------------------------
print("\n=== Best Practices ===")

print("""
Async Best Practices:

1. Use asyncio.run() as the main entry point
   asyncio.run(main())

2. Don't use time.sleep() - use asyncio.sleep()
   await asyncio.sleep(1)  # Correct
   # time.sleep(1)  # WRONG - blocks everything

3. Use gather() or TaskGroup for concurrent tasks
   results = await asyncio.gather(task1(), task2())

4. Use to_thread() for blocking operations
   result = await asyncio.to_thread(blocking_func)

5. Always await coroutines
   result = await async_function()  # Correct
   # result = async_function()  # WRONG - returns coroutine

6. Use async with for async context managers
   async with aiohttp.ClientSession() as session:
       ...

7. Handle timeouts gracefully
   try:
       await asyncio.wait_for(task(), timeout=5.0)
   except asyncio.TimeoutError:
       handle_timeout()
""")

# ------------------------------------------------------------
# PATTERN: ASYNC MAIN FUNCTION
# ------------------------------------------------------------
print("=== Pattern: Async Main ===")


async def main():
    """Standard pattern for async programs"""
    print("Starting async program...")

    # Do async work
    await asyncio.sleep(0.05)

    print("Program complete!")

# This is the standard way to run async code
if __name__ == "__main__":
    # asyncio.run(main())  # Uncomment to run
    print("Use: asyncio.run(main())")
