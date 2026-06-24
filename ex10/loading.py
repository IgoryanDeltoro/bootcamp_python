import time
import sys


def ft_progress(lst):
    total = len(lst)
    if total == 0:
        return

    alpha = 0.3
    ema_speed = None
    second = 1.0
    
    start_time = time.time()
    last_time = start_time

    for i, item in enumerate(lst):
        yield item
        
        current_time = time.time()
        iter_time = current_time - last_time
        if iter_time <= 0:
            iter_time = 0.000001
            
        current_speed = second / iter_time
        last_time = current_time

        if ema_speed is None:
            ema_speed = current_speed
        else:
            ema_speed = (alpha * current_speed) + ((1 - alpha) * ema_speed)


        remaining_items = total - (i + 1)
        if ema_speed > 0:
            eta = remaining_items / ema_speed
        else:
            eta = 0

        elapsed = current_time - start_time

        current = i + 1
        percent = (current / total) * 100
        bar_length = 20
        filled_length = int(bar_length * current // total)
        bar = '=' * filled_length + '>' + ' ' * (bar_length - filled_length - 1)

        sys.stderr.write(
            f"\rETA: {eta:.2f}s [{int(percent)}%]|[{bar}]| {current}/{total} {elapsed:.2f}s  "
        )
        sys.stderr.flush()


def main():
    """
    A custom progress bar generator similar to tqdm.
    """

    lst = range(100)
    ft_progress(lst)
    ret = 0
    for elem in ft_progress(lst):
        ret += elem
        time.sleep(0.05)
    print()
    print(ret)

if __name__ == "__main__":
    main()