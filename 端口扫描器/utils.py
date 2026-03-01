import re
def print_open_port(port):
    print(f"[+] 端口开放:{port}")


def print_scan_start(ip):
    print(f"[*] 开始扫描IP：{ip}")


def print_scan_result(ip, start_port, end_port, open_ports, elapsed_time):
    """打印扫描结果统计信息"""
    print("\n" + "=" * 50)
    print(f"[*] 扫描完成")
    print(f"[*] 目标IP: {ip}")
    print(f"[*] 扫描范围: {start_port} - {end_port}")
    print(f"[*] 开放端口数: {len(open_ports)}")
    if open_ports:
        print(f"[*] 开放端口列表: {sorted(open_ports)}")
    print(f"[*] 扫描耗时: {elapsed_time:.2f}秒")
    print("=" * 50)


def validate_ip(ip):
    """验证IP地址格式是否正确"""
    pattern = r'^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$'
    match = re.match(pattern, ip)
    if not match:
        return False
    # 检查每个段的值是否在0-255之间
    for part in match.groups():
        if not 0 <= int(part) <= 255:
            return False
    return True


def validate_port(port):
    """验证端口号是否在有效范围内（1-65535）"""
    return 1 <= port <= 65535


def get_user_input():
    """获取用户输入的目标IP和端口范围"""
    from config import DEFAULT_TARGET_IP, DEFAULT_START_PORT, DEFAULT_END_PORT

    # 获取目标IP
    while True:
        target_ip = input(f"请输入目标IP地址（默认: {DEFAULT_TARGET_IP}）: ").strip()
        if not target_ip:
            target_ip = DEFAULT_TARGET_IP
            break
        if validate_ip(target_ip):
            break
        else:
            print("IP地址格式错误，请重新输入！")

    # 获取起始端口
    while True:
        start_port_input = input(f"请输入起始端口（默认: {DEFAULT_START_PORT}）: ").strip()
        if not start_port_input:
            start_port = DEFAULT_START_PORT
            break
        try:
            start_port = int(start_port_input)
            if validate_port(start_port):
                break
            else:
                print("端口范围错误，请输入1-65535之间的端口号！")
        except ValueError:
            print("输入错误，请输入有效的数字！")

    # 获取结束端口
    while True:
        end_port_input = input(f"请输入结束端口（默认: {DEFAULT_END_PORT}）: ").strip()
        if not end_port_input:
            end_port = DEFAULT_END_PORT
            break
        try:
            end_port = int(end_port_input)
            if validate_port(end_port) and end_port >= start_port:
                break
            elif end_port < start_port:
                print(f"结束端口必须大于等于起始端口({start_port})！")
            else:
                print("端口范围错误，请输入1-65535之间的端口号！")
        except ValueError:
            print("输入错误，请输入有效的数字！")

    return target_ip, start_port, end_port