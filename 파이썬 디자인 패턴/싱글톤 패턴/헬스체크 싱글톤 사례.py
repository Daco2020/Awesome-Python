class HealthCheck:
    _instance = None
    def __new__(cls, *arg, **kwargs):
        if not HealthCheck._instance:
            HealthCheck._instance = super(HealthCheck, \
                cls).__new__(cls, *arg, **kwargs)
        return HealthCheck._instance
    def __init__(self):
        self._servers = []
    def add_servers(self):
        print("서버를 추가합니다.")
        self._servers.append("Server 1")
        self._servers.append("Server 2")
        self._servers.append("Server 3")
        self._servers.append("Server 4")
    def del_server(self):
        print(self._servers.pop()+" 서버를 삭제합니다.")


hc1 = HealthCheck()
hc2 = HealthCheck()


hc1.add_servers()
for server in hc1._servers:
    print(f"hc1={server}")
"""
서버를 추가합니다.
hc1=Server 1
hc1=Server 2
hc1=Server 3
hc1=Server 4
"""

hc2.del_server()  
hc2.del_server()
"""
Server 4 서버를 삭제합니다.
Server 3 서버를 삭제합니다.
"""

for server in hc1._servers:
    print(f"hc1={server}")
print(hc1 is hc2)
"""
hc1=Server 1
hc1=Server 2
True
"""