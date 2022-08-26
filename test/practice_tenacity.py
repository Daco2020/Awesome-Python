import tenacity
from tenacity import stop_after_attempt


@tenacity.retry(
    stop=tenacity.stop_after_attempt(5),
)
def throw_error():
    print("running...")
    raise ValueError("Errors make me stronger")


if __name__ == "__main__":
    throw_error()
