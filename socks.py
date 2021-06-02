import socks

def headers(): # Socket headers send metod...

    headers = ""
    headers += "GET /ip HTTP/1.1\r\n"
    headers += "Host: httpbin.org\r\n"
    headers += "User-Agent: Mozilla/5.0 (Windows NT 6.1; rv:82.0) Gecko/20100101 Firefox/82.0\r\n"
    headers += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\n"
    headers += "Accept-Language: ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3\r\n"
    headers += "Accept-Encoding: gzip, deflate\r\n"
    headers += "Connection: keep-alive\r\n"
    headers += "Upgrade-Insecure-Requests: 1\r\n"
    headers += "Cache-Control: max-age=0\r\n\r\n"

    return headers.encode()

def connect(ipaddress, ipport): # Check proxy metod...

    try:
        c = socks.socksocket()
        c.set_proxy(socks.SOCKS5, ipaddress, int(ipport))
        c.connect(("httpbin.org", 80))
        c.send(headers())
        response = c.recv(4096).decode("iso-8859-1")
        print(response)

    except Exception as error:
        print(error)

ipaddress = "118.140.253.210"
ipport = 1080
connect(ipaddress, ipport)