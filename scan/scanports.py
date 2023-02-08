from scan import testip


def scan(host, ports):
    result = []
    for port in ports:
        result.append({
            'host': host,
            'port': port,
            'result': testip.test_ip_port(host, port)
        })
    return result
