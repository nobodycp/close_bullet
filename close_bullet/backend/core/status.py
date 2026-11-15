import threading

from close_bullet.backend.coloramas import Fore, Style


class Status:
    valid = 0
    invalid = 0
    retry = []
    Bad_to_file = []
    _lock = threading.Lock()

    def add_valid(self):
        with self._lock:
            self.valid += 1

    def add_invalid(self):
        with self._lock:
            self.invalid += 1

    def append_retry(self, item):
        with self._lock:
            self.retry.append(item)

    def print_res(self, q_size):
        with self._lock:
            valid, invalid, retry_unique = self.valid, self.invalid, len(set(self.retry))
        print(
            f"{Style.RESET_ALL}\r {Fore.BLUE}{q_size}{Style.RESET_ALL} | "
            f"{Fore.GREEN}✔️ {valid}{Style.RESET_ALL} | "
            f"{Fore.RED}✘ {invalid}{Style.RESET_ALL} | "
            f"{Fore.YELLOW + Style.BRIGHT}♺ {retry_unique}{Style.RESET_ALL} ",
            end="",
            flush=True,
        )

    def save_bad_data(self):
        with self._lock:
            bad_rows = list(self.Bad_to_file)
        with open("bad_retry.txt", "a") as bad_data:
            for bad in bad_rows:
                bad_data.write(f"{bad}\n")

    def check_bad(self, data):
        with self._lock:
            if data in self.Bad_to_file:
                return 1
            if self.retry.count(data) >= 5:
                self.Bad_to_file.append(data)
                self.invalid += 1
                for _ in range(5):
                    try:
                        self.retry.remove(data)
                    except ValueError:
                        pass
                return 1
            return 0