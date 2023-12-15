import socket

target_ip = "192.168.47.130"
target_port = 34567

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((target_ip,target_port))

msg = """<?xml version="1.0" encoding="UTF-8"?>
<e:Envelope xmlns:e="http://www.w3.org/2003/05/soap-envelope"
 xmlns:w="http://schemas.xmlsoap.org/ws/2004/08/addressing"
 xmlns:d="http://schemas.xmlsoap.org/ws/2005/04/discovery"
 xmlns:dn="http://www.onvif.org/ver10/network/wsdl">
 <e:Header>
 <w:MessageID>uuid:84ede3de-7dec-11d0-c360-f01234567890</w:MessageID>
 <w:To e:mustUnderstand="true">urn:schemas-xmlsoap-org:ws:2005:04:discovery</w:To>
 <w:Action
a:mustUnderstand="true">http://schemas.xmlsoap.org/ws/2005/04/discovery/Pr
obe</w:Action>
 </e:Header>
 <e:Body>
 <d:Probe>
 <d:Types>dn:NetworkVideoTransmitter</d:Types>
 </d:Probe>
 </e:Body>
</e:Envelope>

"""
socket.sendall(msg.encode(encoding='utf-8'))

data = socket.recv(100)
msg = data.decode() 
print('echo msg:', msg)

socket.close()
