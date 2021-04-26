class Shelf:
    PENDING = "PENDING"
    DONE = "DONE"

    def __init__(self):
        self.shelf = {}

    def add_job(self, id: str):
        self.shelf[id] = self.PENDING

    def finish_job(self, id: str):
        self.shelf[id] = self.DONE

    def get_job_status(self, id: str) -> str:
        try:
            return self.shelf[id]
        except:
            return ""
