from datetime import datetime, timedelta
import logging


logging.basicConfig(
    filename='hb_test.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger("LOG EVENT")

time_format = ""

SEEKING_KEY = "Key TSTFEED0300|7E3E|0400"

log_list = []
processed_list = []
format_time_full = "%H:%M:%S"

def open_log(log_file_name):
    with open(log_file_name, "r") as file:
        for key in file:
            if SEEKING_KEY in key:
                log_list.append(key)

def find_diff_between_logs(parsed_log):
    for seek in parsed_log:
        start_index = seek.find("Timestamp")
        time_stmp = seek[start_index+10:start_index+18]
        time_list = datetime.strptime(time_stmp, format_time_full)
        processed_list.append(time_list)

    for i in range(len(processed_list)-1):
        current_elem = processed_list[i]
        next_elem = processed_list[i+1]
        diff = current_elem - next_elem
        final_diff = timedelta.total_seconds(diff)
        if 31 < final_diff < 33:
            logger.warning(f"Heartbeat > 31 sec and < 33, Difference={final_diff} sec, current time= {datetime.strftime(current_elem, format_time_full)}")
        if final_diff >= 33:
            logger.error(f"Heartbeat > 33 sec, Difference={final_diff} sec, current time= {datetime.strftime(current_elem, format_time_full)}")


if __name__ == "__main__":

    open_log("hblog.txt")
    find_diff_between_logs(log_list)