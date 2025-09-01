from http.server import HTTPServer, BaseHTTPRequestHandler

content = '''
<!doctype html>
<html>
<head>
<title>My Web Server</title>
</head>
<body align="center">
<h1> TCP/IP Protocol</h1>

<table border="1" align="center" cellpadding="0.5" cellspacing="0" bgcolor="pink">
  <tr>
    <th>S.NO</th>
    <th>Name of the Layer</th>
    <th>Name of the Protocols</th>
  </tr>

  <tr>
    <td><b>1</b></td>
    <td><b>Application Layer</b></td>
    <td><b>HTTP, HTTPS, FTP, SMTP, POP3, IMAP, DNS, Telnet, SSH</b></td>
  </tr>

  <tr>
    <td><b>2</b></td>
    <td><b>Transport Layer</b></td>
    <td><b>TCP (Transmission Control Protocol), UDP (User Datagram Protocol)</b></td>
  </tr>

  <tr>
    <td><b>3</b></td>
    <td><b>Network Layer (Internet Layer in TCP/IP)</b></td>
    <td><b>IP (IPv4, IPv6), ICMP, IGMP, ARP, RARP</b></td>
  </tr>

  <tr>
    <td><b>4</b></td>
    <td><b>Link Layer (Network Access Layer in TCP/IP)</b></td>
    <td><b>Ethernet</b></td>
  </tr>
</table>
</body>
</html>'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("GET request received...")
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(content.encode("utf-8"))

print("This is my webserver, running at http://localhost:5000/")
server_address = ('', 5000)
httpd = HTTPServer(server_address, MyServer)
httpd.serve_forever()