from concurrent.futures import ThreadPoolExecutor

class ThreadPoolManager:
    """
    A class to manage multiple threads for concurrent processing.
    """

    def __init__(self, max_workers=5):
        """
        Initializes the Thread Pool Manager.

        :param max_workers: Maximum number of worker threads.
        """
        self.executor = ThreadPoolExecutor(max_workers=max_workers)

    def submit_task(self, task, *args, **kwargs):
        """
        Submits a task to the thread pool.

        :param task: Task function to execute.
        :param args: Positional arguments for the task.
        :param kwargs: Keyword arguments for the task.
        :return: A Future object representing the task.
        """
        return self.executor.submit(task, *args, **kwargs)
