from scanner import scan_port
from utils import print_open_port, print_scan_start, print_scan_result, get_user_input
from config import THREAD_COUNT
import concurrent.futures
import time


def main():
    # 获取用户输入的IP和端口范围
    target_ip, start_port, end_port = get_user_input()

    print_scan_start(target_ip)
    start_time = time.time()

    # 存储开放端口的列表
    open_ports = []

    # 使用线程池执行扫描任务
    with concurrent.futures.ThreadPoolExecutor(max_workers=THREAD_COUNT) as executor:
        # 提交所有扫描任务到线程池
        future_to_port = {executor.submit(scan_port, target_ip, port): port for port in range(start_port, end_port + 1)}

        # 处理完成的任务
        for future in concurrent.futures.as_completed(future_to_port):
            port = future_to_port[future]
            try:
                # 获取扫描结果
                result = future.result()
                if result:
                    open_ports.append(port)
                    print_open_port(port)
            except Exception as e:
                print(f"扫描端口{port}时发生错误: {e}")

    # 计算扫描耗时
    end_time = time.time()
    elapsed_time = end_time - start_time

    # 打印扫描结果统计
    print_scan_result(target_ip, start_port, end_port, open_ports, elapsed_time)


if __name__ == "__main__":
    main()
