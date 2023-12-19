Discovery.Probe message
<?xml version="1.0" encoding="UTF-8"?>
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

Request device.GetCapabilities
<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://www.w3.org/2003/05/soap-envelope"
 xmlns:tds="http://www.onvif.org/ver10/device/wsdl">
 <SOAP-ENV:Body>
 <tds:GetCapabilities>
 <tds:Category>All</tds:Category>
 </tds:GetCapabilities>
 </SOAP-ENV:Body>
</SOAP-ENV:Envelope>

Request device.SetNetworkInterfaces
<?xml version='1.0' encoding='utf-8'?>
<soapenv:Envelope
 xmlns:soapenv="http://www.w3.org/2003/05/soap-envelope"
 xmlns:tds="http://www.onvif.org/ver10/device/wsdl"
 xmlns:tt="http://www.onvif.org/ver10/schema">
 <soapenv:Body>
 <tds:SetNetworkInterfaces>
 <tds:InterfaceToken>eth0</tds:InterfaceToken>
 <tds:NetworkInterface>
 <tt:Enabled>true</tt:Enabled>
 <tt:IPv4>
 <tt:Enabled>true</tt:Enabled>
 <tt:Manual>
 <tt:Address>192.168.0.200</tt:Address>
 <tt:PrefixLength>24</tt:PrefixLength>
 </tt:Manual>
 <tt:DHCP>false</tt:DHCP>
 </tt:IPv4>
 </tds:NetworkInterface>
 </tds:SetNetworkInterfaces>
 </soapenv:Body>
</soapenv:Envelope> 

Request device.SetNTP
<?xml version="1.0" encoding="UTF-8"?>
<soapenv:Envelope
 xmlns:soapenv="http://www.w3.org/2003/05/soap-envelope"
xmlns:tt="http://www.onvif.org/ver10/schema"
 xmlns:tds="http://www.onvif.org/ver10/device/wsdl">
 <soapenv:Body>
 <tds:SetNTP>
 <tds:FromDHCP>false</tds:FromDHCP>
 <tds:NTPManual>
 <tt:Type>IPv4</tt:Type>
 <tt:IPv4Address>192.168.10.1</tt:IPv4Address>
 </tds:NTPManual>
 </tds:SetNTP>
 </soapenv:Body>
</soapenv:Envelope>

Request device.SetSystemDateAndTime
<?xml version="1.0" encoding="UTF-8"?>
<soapenv:Envelope
 xmlns:soapenv="http://www.w3.org/2003/05/soap-envelope"
xmlns:tt="http://www.onvif.org/ver10/schema"
 xmlns:tds="http://www.onvif.org/ver10/device/wsdl">
 <soapenv:Body>
 <tds:SetSystemDateAndTime>
 <tt:DateTimeType>NTP</tt:DateTimeType>
 <tt:DaylightSavings>false</tt:DaylightSavings>
 </tds:SetSystemDateAndTime>
 </soapenv:Body>
</soapenv:Envelope> 

Reqest device.SetNTP
<?xml version="1.0" encoding="UTF-8"?>
<soapenv:Envelope
 xmlns:soapenv="http://www.w3.org/2003/05/soap-envelope"
xmlns:tt="http://www.onvif.org/ver10/schema"
 xmlns:tds="http://www.onvif.org/ver10/device/wsdl">
 <soapenv:Body>
 <tds:SetNTP>
 <tds:FromDHCP>true</tds:FromDHCP>
 </tds:SetNTP>
 </soapenv:Body>
</soapenv:Envelope>

Request device.SetSystemDateAndTime
<?xml version="1.0" encoding="UTF-8"?>
<soapenv:Envelope
 xmlns:soapenv="http://www.w3.org/2003/05/soap-envelope"
xmlns:tt="http://www.onvif.org/ver10/schema"
 xmlns:tds="http://www.onvif.org/ver10/device/wsdl">
 <soapenv:Body>
 <tds:SetSystemDateAndTime>
 <tt:DateTimeType>NTP</tt:DateTimeType>
 <tt:DaylightSavings>false</tt:DaylightSavings>
 </tds:SetSystemDateAndTime>
 </soapenv:Body>
</soapenv:Envelope>

Request device.RestoreSystem
<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://www.w3.org/2003/05/soap-envelope">
 <SOAP-ENV:Body>
 <tds:RestoreSystem xmlns="http://www.onvif.org/ver10/device/wsdl">
 <BackupFiles>
 <Name xmlns="http://www.onvif.org/ver10/schema">STRING</Name>
<Data xmlns="http://www.onvif.org/ver10/schema"><xop:Include
href="cid:1.633335845875937500@example.org"/>
 </Data>
 </BackupFiles>
 </tds:RestoreSystem>
 </SOAP-ENV:Body>
</SOAP-ENV:Envelope>

REQUEST CreateUsers 
<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:soap12="http://www.w3.org/2003/05/soap-envelope"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:xsd="http://www.w3.org/2001/XMLSchema"
xmlns:tt="http://www.onvif.org/ver10/schema">
 <soap12:Body>
 <CreateUsers xmlns="http://www.onvif.org/ver10/device/wsdl">
 <User>
 <tt:Username>newusername</tt:Username>
 <tt:Password>newuserpassword</tt:Password>
 <tt:UserLevel>Administrator</tt:UserLevel>
 </User>
 </CreateUsers>
 </soap12:Body>
</soap12:Envelope>

REQUEST SetUser 
<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:soap12="http://www.w3.org/2003/05/soap-envelope"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:xsd="http://www.w3.org/2001/XMLSchema"
xmlns:tt="http://www.onvif.org/ver10/schema">
 <soap12:Body>
 <SetUser xmlns="http://www.onvif.org/ver10/device/wsdl">
 <User>
 <tt:Username>username</tt:Username>
 <tt:Password>newpassword</tt:Password>
 <tt:UserLevel>Administrator</tt:UserLevel>
 </User>
 </SetUser>
 </soap12:Body>
</soap12:Envelope>

REQUEST DeleteUsers
<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:soap12="http://www.w3.org/2003/05/soap-envelope"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:xsd="http://www.w3.org/2001/XMLSchema">
 <soap12:Body>
 <DeleteUsers xmlns="http://www.onvif.org/ver10/device/wsdl">
 <Username>deleteusername</Username>
 </DeleteUsers>
 </soap12:Body>
</soap12:Envelope>

REQUEST CreateCertificate
<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:soap12="http://www.w3.org/2003/05/soap-envelope"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:xsd="http://www.w3.org/2001/XMLSchema"
xmlns:tt="http://www.onvif.org/ver10/schema" xmlns:wsse="http://docs.oasisopen.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"
xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility1.0.xsd">
 <soap12:Header>
 <wsse:Security>
 <wsu:Timestamp wsu:Id="Time">
 <wsu:Created>2010-12-15T09:44:53Z</wsu:Created>
 <wsu:Expires>2010-12-15T09:45:03Z</wsu:Expires>
 </wsu:Timestamp>
 <wsse:UsernameToken wsu:Id="User">
 <wsse:Username>admin</wsse:Username>
 <wsse:Password Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wssusername-token-profile-1.0#PasswordDigest">aUn1yvwgh/rm4a/srO8hboMT6ms=</wsse:Password>
 <wsse:Nonce>AE0aDtVhZk6N/VBChMyiCw==</wsse:Nonce>
 <wsu:Created>2010-12-15T09:44:53Z</wsu:Created>
 </wsse:UsernameToken>
 </wsse:Security>
 </soap12:Header>
 <soap12:Body>
 <CreateCertificate xmlns="http://www.onvif.org/ver10/device/wsdl">
 <CertificateID>SelfSigned1</CertificateID>
 <Subject>
 <!-- Vendor specific parameter -->
 </Subject>
 <ValidNotAfter>2020-10-01T09:00:00</ValidNotAfter>
 </CreateCertificate>
 </soap12:Body>
</soap12:Envelope>

<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:soap12="http://www.w3.org/2003/05/soap-envelope"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:xsd="http://www.w3.org/2001/XMLSchema"
xmlns:tt="http://www.onvif.org/ver10/schema" xmlns:wsse="http://docs.oasisopen.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"
xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility1.0.xsd">
 <soap12:Header>
 <wsse:Security>
 <wsu:Timestamp wsu:Id="Time">
 <wsu:Created>2010-12-15T09:44:53Z</wsu:Created>
 <wsu:Expires>2010-12-15T09:45:03Z</wsu:Expires>
 </wsu:Timestamp>
 <wsse:UsernameToken wsu:Id="User">
 <wsse:Username>admin</wsse:Username>
 <wsse:Password Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wssusername-token-profile-1.0#PasswordDigest">aUn1yvwgh/rm4a/srO8hboMT6ms=</wsse:Password>
 <wsse:Nonce>AE0aDtVhZk6N/VBChMyiCw==</wsse:Nonce>
 <wsu:Created>2010-12-15T09:44:53Z</wsu:Created>
 </wsse:UsernameToken>
 </wsse:Security>
 </soap12:Header>
 <soap12:Body>
 <CreateCertificate xmlns="http://www.onvif.org/ver10/device/wsdl">
 <CertificateID>SelfSigned1</CertificateID>
 <Subject>
 <!-- Vendor specific parameter -->
 </Subject>
 <ValidNotAfter>2020-10-01T09:00:00</ValidNotAfter>
 </CreateCertificate>
 </soap12:Body>
</soap12:Envelope>

REQUEST GetCertificatesStatus 
<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:soap12="http://www.w3.org/2003/05/soap-envelope"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:xsd="http://www.w3.org/2001/XMLSchema"
xmlns:tt="http://www.onvif.org/ver10/schema" xmlns:wsse="http://docs.oasisopen.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"
xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility1.0.xsd">
<soap12:Header>
 <wsse:Security>
 <wsu:Timestamp wsu:Id="Time">
 <wsu:Created>2010-12-15T09:52:27Z</wsu:Created>
 <wsu:Expires>2010-12-15T09:52:37Z</wsu:Expires>
 </wsu:Timestamp>
 <wsse:UsernameToken wsu:Id="User">
 <wsse:Username>admin</wsse:Username>
 <wsse:Password Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wssusername-token-profile1.0#PasswordDigest">zt64Tr8gJbjgFhx3uWPQOl0vlCk=</wsse:Password>
 <wsse:Nonce>VmJLgRgKkk6bk7dqMWadEQ==</wsse:Nonce>
 <wsu:Created>2010-12-15T09:52:27Z</wsu:Created>
 </wsse:UsernameToken>
 </wsse:Security>
 </soap12:Header>
 <soap12:Body>
 <GetCertificatesStatus xmlns="http://www.onvif.org/ver10/device/wsdl" />
 </soap12:Body>
</soap12:Envelope> 

REQUEST SetCertificatesStatus
<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:soap12="http://www.w3.org/2003/05/soap-envelope"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:xsd="http://www.w3.org/2001/XMLSchema"
xmlns:tt="http://www.onvif.org/ver10/schema" xmlns:wsse="http://docs.oasisopen.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"
xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility1.0.xsd">
 <soap12:Header>
 <wsse:Security>
 <wsu:Timestamp wsu:Id="Time">
 <wsu:Created>2010-12-15T09:58:36Z</wsu:Created>
 <wsu:Expires>2010-12-15T09:58:46Z</wsu:Expires>
 </wsu:Timestamp>
 <wsse:UsernameToken wsu:Id="User">
 <wsse:Username>admin</wsse:Username>
 <wsse:Password Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wssusername-token-profile-1.0#PasswordDigest">I7sE3LvaAHTyhUPMmHgxrxTmM8E=</wsse:Password>
 <wsse:Nonce>iQySVaOOjE2v+dPWzkUuXg==</wsse:Nonce>
 <wsu:Created>2010-12-15T09:58:36Z</wsu:Created>
 </wsse:UsernameToken>
 </wsse:Security>
 </soap12:Header>
 <soap12:Body>
 <SetCertificatesStatus xmlns="http://www.onvif.org/ver10/device/wsdl">
 <CertificateStatus>
 <tt:CertificateID>SelfSigned1</tt:CertificateID>
 <tt:Status>true</tt:Status>
 </CertificateStatus>
 </SetCertificatesStatus>
 </soap12:Body>
</soap12:Envelope>

REQUEST GetPkcs10Request
<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:soap12="http://www.w3.org/2003/05/soap-envelope"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:xsd="http://www.w3.org/2001/XMLSchema"
xmlns:tt="http://www.onvif.org/ver10/schema" xmlns:wsse="http://docs.oasisopen.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"
xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility1.0.xsd">
 <soap12:Header>
 <wsse:Security>
 <wsu:Timestamp wsu:Id="Time">
 <wsu:Created>2010-12-15T10:11:06Z</wsu:Created>
 <wsu:Expires>2010-12-15T10:11:16Z</wsu:Expires>
 </wsu:Timestamp>
 <wsse:UsernameToken wsu:Id="User">
 <wsse:Username>admin</wsse:Username>
 <wsse:Password Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wssusername-token-profile1.0#PasswordDigest">6QHS1lyd/hkTY+0Px/LonCtwJs0=</wsse:Password>
 <wsse:Nonce>G2bfEGaQ/kivDYt2pWk/Lw==</wsse:Nonce>
 <wsu:Created>2010-12-15T10:11:06Z</wsu:Created>
 </wsse:UsernameToken>
 </wsse:Security>
 </soap12:Header>
 <soap12:Body>
 <GetPkcs10Request xmlns="http://www.onvif.org/ver10/device/wsdl">
 <CertificateID>SelfSigned2</CertificateID>
 <Subject>
 <!-- Vendor specific parameter -->
 </Subject>
 </GetPkcs10Request>
 </soap12:Body>
</soap12:Envelope>

REQUEST LoadCertificates
<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:soap12="http://www.w3.org/2003/05/soap-envelope"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:xsd="http://www.w3.org/2001/XMLSchema"
xmlns:tt="http://www.onvif.org/ver10/schema" xmlns:wsse="http://docs.oasisopen.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"
xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd">
 <soap12:Header>
 <wsse:Security>
 <wsu:Timestamp wsu:Id="Time">
 <wsu:Created>2010-12-15T10:31:07Z</wsu:Created>
 <wsu:Expires>2010-12-15T10:31:17Z</wsu:Expires>
 </wsu:Timestamp>
 <wsse:UsernameToken wsu:Id="User">
 <wsse:Username>admin</wsse:Username>
 <wsse:Password Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wssusername-token-profile1.0#PasswordDigest">NWSuWYhaswddfESWz3p1EFqOVkU=</wsse:Password>
 <wsse:Nonce>0IVhwRSiWkacTRUs3JWm6w==</wsse:Nonce>
 <wsu:Created>2010-12-15T10:31:07Z</wsu:Created>
 </wsse:UsernameToken>
 </wsse:Security>
 </soap12:Header>
 <soap12:Body>
 <LoadCertificates xmlns="http://www.onvif.org/ver10/device/wsdl">
 <NVTCertificate>
 <tt:CertificateID>CASigned1</tt:CertificateID>
 <tt:Certificate>
<tt:Data>MIIEajCCA9OgAwIBAgIQbypes1ZWrRNc6WboYpTs0TANBgkqhkiG9w0BAQUFADCB5zE
LMAkGA1UEBhMCVVMxFzAVBgNVBAoTDlZlcmlTaWduLCBJbmMuMR8wHQYDVQQLExZGT1IgVEVTVCB
QVVJQT1NFUyBPTkxZMR8wHQYDVQQLExZWZXJpU2lnbiBUcnVzdCBOZXR3b3JrMUMwQQYDVQQLEzp
UZXJtcyBvZiB1c2UgYXQgaHR0cHM6Ly93d3cudmVyaXNpZ24uY29tL2Nwcy90ZXN0Y2EvIChjKTA
3MTgwNgYDVQQDEy9WZXJpU2lnbiBDbGFzcyAzIFNlY3VyZSBTZXJ2ZXIgMTAyNC1iaXQgVGVzdCB
DQTAeFw0xMDA2MjIwMDAwMDBaFw0xMDA3MDYyMzU5NTlaMIGjMQswCQYDVQQGEwJKUDERMA8GA1U
ECBMIS2FtYWdhd2ExETAPBgNVBAcUCFlva29oYW1hMRIwEAYDVQQKFAlQYW5hc29uaWMxDTALBgN
VBAsUBFBGREMxOjA4BgNVBAsUMVRlcm1zIG9mIHVzZSBhdCB3d3cudmVyaXNpZ24uY29tL2Nwcy9
0ZXN0Y2EgKGMpMDUxDzANBgNVBAMUBmNhbWVyYTCBnzANBgkqhkiG9w0BAQEFAAOBjQAwgYkCgYE
AtclG+P9Uzj1C0y3y9Hk6jJkgnrjLbCfpsNhOYPIiR/OJQntvREpcw8ktvKjkVKiG7K5MnZVoDdi
KmcYLf5PMVljFnw/dtUEalQXyYK1K6Wpv3pQFNP+G9903Y+w3lYGTUBPn2YuEouJjwfveLTYessC
u21O6jo6Mo3UGgUy5kX0CAwEAAaOCAVcwggFTMAkGA1UdEwQCMAAwCwYDVR0PBAQDAgWgMD0GA1U
dHwQ2MDQwMqAwoC6GLGh0dHA6Ly9jcmwudmVyaXNpZ24uY29tL1NWUjEwMjRUcmlhbDIwMDcuY3J
sMEoGA1UdIARDMEEwPwYKYIZIAYb4RQEHFTAxMC8GCCsGAQUFBwIBFiNodHRwczovL3d3dy52ZXJ
pc2lnbi5jb20vY3BzL3Rlc3RjYTAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwHwYDVR0
jBBgwFoAU6XX2ekWwDNKb42eN0kQT1JHEfXYwbgYIKwYBBQUHAQwEYjBgoV6gXDBaMFgwVhYJaW1
hZ2UvZ2lmMCEwHzAHBgUrDgMCGgQUS2u5KJYGDLvQUjibKaxLB4shBRgwJhYkaHR0cDovL2xvZ28
udmVyaXNpZ24uY29tL3ZzbG9nbzEuZ2lmMA0GCSqGSIb3DQEBBQUAA4GBALdm+PMsUq2zTSpDsUL
aVZtQhyI0P3guVINkypPyxPCKb8MKCHLI8DmEjWeZe8oohJlvX8pyvlIdXzdpqXrFsy+EkgSoykF
GR/EnYN9uZ8HuUNPQqyKy9248FEAFnPheffdXDosFS6jtJIfYaIe6YKQr4WTNWIgCt3h8c+B5t7x
A</tt:Data>
 </tt:Certificate>
 </NVTCertificate>
 </LoadCertificates>
 </soap12:Body>
</soap12:Envelope>

REQUEST GetCertificateInformation
<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:soap12="http://www.w3.org/2003/05/soap-envelope"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:xsd="http://www.w3.org/2001/XMLSchema"
xmlns:tt="http://www.onvif.org/ver10/schema" xmlns:wsse="http://docs.oasisopen.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"
xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurityutility-1.0.xsd">
 <soap12:Header>
 <wsse:Security>
 <wsu:Timestamp wsu:Id="Time">
 <wsu:Created>2010-12-15T10:31:07Z</wsu:Created>
 <wsu:Expires>2010-12-15T10:31:17Z</wsu:Expires>
 </wsu:Timestamp>
 <wsse:UsernameToken wsu:Id="User">
 <wsse:Username>admin</wsse:Username>
 <wsse:Password Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wssusername-token-profile1.0#PasswordDigest">NWSuWYhaswddfESWz3p1EFqOVkU=</wsse:Password>
 <wsse:Nonce>0IVhwRSiWkacTRUs3JWm6w==</wsse:Nonce>
 <wsu:Created>2010-12-15T10:31:07Z</wsu:Created>
 </wsse:UsernameToken>
 </wsse:Security>
 </soap12:Header>
 <soap12:Body>
 <GetCertificateInformation xmlns="http://www.onvif.org/ver10/device/wsdl">
 <CertificateID>CASigned1</CertificateID>
 </GetCertificateInformation>
 </soap12:Body>
</soap12:Envelope>

REQUEST DeleteCertificates
<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:soap12="http://www.w3.org/2003/05/soap-envelope"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:xsd="http://www.w3.org/2001/XMLSchema"
xmlns:tt="http://www.onvif.org/ver10/schema" xmlns:wsse="http://docs.oasisopen.org/wss/2004/01/oasis-200401-wss-wssecurity-secext-1.0.xsd"
xmlns:wsu="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurityutility-1.0.xsd">
 <soap12:Header>
 <wsse:Security>
 <wsu:Timestamp wsu:Id="Time">
 <wsu:Created>2010-12-16T04:14:54Z</wsu:Created>
 <wsu:Expires>2010-12-16T04:15:04Z</wsu:Expires>
 </wsu:Timestamp>
 <wsse:UsernameToken wsu:Id="User">
 <wsse:Username>admin</wsse:Username>
 <wsse:Password Type="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wssusername-token-profile1.0#PasswordDigest">6pm+oKs7OY6DcLRCJBgAGZQ4WfA=</wsse:Password>
 <wsse:Nonce>7yEbAncRKUuT8p3X+9T69A==</wsse:Nonce>
 <wsu:Created>2010-12-16T04:14:54Z</wsu:Created>
 </wsse:UsernameToken>
 </wsse:Security>
 </soap12:Header>
 <soap12:Body>
 <DeleteCertificates xmlns="http://www.onvif.org/ver10/device/wsdl">
 <CertificateID>SelfSigned1</CertificateID>
 </DeleteCertificates>
 </soap12:Body>
</soap12:Envelope>


REQUEST SetNetworkProtocols
<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:soap12="http://www.w3.org/2003/05/soap-envelope"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:xsd="http://www.w3.org/2001/XMLSchema"
xmlns:tt="http://www.onvif.org/ver10/schema">
 <soap12:Body>
 <SetNetworkProtocols xmlns="http://www.onvif.org/ver10/device/wsdl">
 <NetworkProtocols>
 <tt:Name>HTTP</tt:Name>
 <tt:Enabled>true</tt:Enabled>
 <tt:Port>80</tt:Port>
 </NetworkProtocols>
 <NetworkProtocols>
 <tt:Name>RTSP</tt:Name>
 <tt:Enabled>true</tt:Enabled>
 <tt:Port>554</tt:Port>
 </NetworkProtocols>
 <NetworkProtocols>
 <tt:Name>HTTPS</tt:Name>
 <tt:Enabled>true</tt:Enabled>
 <tt:Port>443</tt:Port>
 </NetworkProtocols>
 </SetNetworkProtocols> </soap12:Body>
</soap12:Envelope>

SOAP REQUEST GetStreamURI
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
xmlns:trt="http://www.onvif.org/ver10/media/wsdl"
xmlns:tt="http://www.onvif.org/ver10/schema">
 <soap:Body>
 <trt:GetStreamUri>
 <trt:StreamSetup>
 <tt:Stream>RTP-Unicast</tt:Stream>
 <tt:Transport>
 <tt:Protocol>UDP</tt:Protocol>
 </Transport>
 </trt:StreamSetup>
 <trt:ProfileToken>Profile1</trt:ProfileToken>
 </trt:GetStreamUri>
 </soap:Body>
</soap:Envelope> 

SOAP REQUEST SetVideoEncoderConfiguration
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
 xmlns:trt="http://www.onvif.org/ver10/media/wsdl"
 xmlns:tt="http://www.onvif.org/ver10/schema">
 <soap:Body>
 <trt:SetVideoEncoderConfiguration>
 <trt:Configuration token="video_encoder_config1">
 <tt:Name>video_encoder_config1</tt:Name>
 <tt:UseCount>1</tt:UseCount>
 <tt:Encoding>JPEG</tt:Encoding>
 <tt:Resolution>
 <tt:Width>320</tt:Width>
 <tt:Height>192</tt:Height>
 </tt:Resolution>
 <tt:Quality>1</tt:Quality>
 <tt:RateControl>
 <tt:FrameRateLimit>1</tt:FrameRateLimit>
 <tt:EncodingInterval>1</tt:EncodingInterval>
 <tt:BitrateLimit>384</tt:BitrateLimit>
 </tt:RateControl>
 <tt:Multicast>
 <tt:Address>
 <tt:Type>IPv4</tt:Type>
 <tt:IPv4Address>0.0.0.0</tt:IPv4Address>
 </tt:Address>
 <tt:Port>0</tt:Port>
 <tt:TTL>3</tt:TTL>
 <tt:AutoStart>false</tt:AutoStart>
 </tt:Multicast>
 <tt:SessionTimeout>PT0S</tt:SessionTimeout>
 </trt:Configurations>
 <trt:ForcePersistence>true</trt:ForcePersistence>
 </trt:SetVideoEncoderConfiguration>
 </soap:Body>
</soap:Envelope>

SOAP REQUEST CreateProfile
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
 xmlns:trt="http://www.onvif.org/ver10/media/wsdl">
 <soap:Body>
 <trt:CreateProfile>
 <trt:Name>Test Profile</trt:Name>
 <trt:Token>testprof0</trt:Token>
 </trt:CreateProfile>
 </soap:Body>
</soap:Envelope> 

SOAP REQUEST AddVideoSourceConfiguration
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
 xmlns:trt="http://www.onvif.org/ver10/media/wsdl"
 xmlns:tt="http://www.onvif.org/ver10/schema">
 <soap:Body>
 <trt:AddVideoSourceConfiguration>
 <trt:ProfileToken>testprof0</trt:ProfileToken>
 <trt:ConfigurationToken>video_source_config</trt:ConfigurationToken>
 </trt:AddVideoSourceConfiguration>
 </soap:Body>
</soap:Envelope> 

SOAP REQUEST AddVideoEncoderConfiguration
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
 xmlns:trt="http://www.onvif.org/ver10/media/wsdl">
 <soap:Body>
 <trt:AddVideoEncoderConfiguration>
 <trt:ProfileToken>testprof0</trt:ProfileToken>
 <trt:ConfigurationToken>video_encoder_config1</trt:ConfigurationToken>
 </trt:AddVideoEncoderConfiguration>
 </soap:Body>
</soap:Envelope> 

REQUEST StartMulticastStreaming
<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:soap12="http://www.w3.org/2003/05/soap-envelope"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:xsd="http://www.w3.org/2001/XMLSchema"
xmlns:tt="http://www.onvif.org/ver10/schema">
 <soap12:Body>
 <StartMulticastStreaming xmlns="http://www.onvif.org/ver10/media/wsdl">
 <ProfileToken>profile_1</ProfileToken>
 </StartMulticastStreaming>
 </soap12:Body>
</soap12:Envelope> 

REQUEST StopMulticastStreaming
<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:soap12="http://www.w3.org/2003/05/soap-envelope"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:xsd="http://www.w3.org/2001/XMLSchema"
xmlns:tt="http://www.onvif.org/ver10/schema">
 <soap12:Body>
 <StopMulticastStreaming xmlns="http://www.onvif.org/ver10/media/wsdl">
 <ProfileToken>profile_1</ProfileToken>
 </StopMulticastStreaming>
 </soap12:Body>
</soap12:Envelope>

Request: media.GetMetadataConfiguration
<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://www.w3.org/2003/05/soap-envelope"
 xmlns:media="http://www.onvif.org/ver10/media/wsdl">
<SOAP-ENV:Body>
 <media:GetMetadataConfiguration>
 <media:ConfigurationToken>0</media:ConfigurationToken>
 </media:GetMetadataConfiguration>
 </SOAP-ENV:Body>
</SOAP-ENV:Envelope>

Request: media.SetMetadataConfiguration
<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://www.w3.org/2003/05/soap-envelope"
 xmlns:wsnt="http://docs.oasis-open.org/wsn/b-2"
 xmlns:wstop="http://docs.oasis-open.org/wsn/t-1"
 xmlns:tt="http://www.onvif.org/ver10/schema"
 xmlns:media="http://www.onvif.org/ver10/media/wsdl"
 xmlns:tns1="http://www.onvif.org/ver10/topics"
 xmlns:tnsvendor="http://www.vendor.com/2009/event/topics">
 <SOAP-ENV:Body>
 <media:SetMetadataConfiguration>
 <media:Configuration token="0">
 <tt:Name>metadata</tt:Name>
 <tt:UseCount>1</tt:UseCount>
 <tt:Events>
 <tt:Filter>
 <wsnt:TopicExpression
Dialect="http://www.onvif.org/ver10/tev/topicExpression/ConcreteSet"
>tns1:Device//.</wsnt:TopicExpression>
 </tt:Filter>
 </tt:Events>
 <tt:Multicast>
 <tt:Address>
 <tt:Type>IPv4</tt:Type>
 <tt:IPv4Address>0.0.0.0</tt:IPv4Address>
 </tt:Address>
 <tt:Port>0</tt:Port>
 <tt:TTL>1</tt:TTL>
 <tt:AutoStart>false</tt:AutoStart>
 </tt:Multicast>
 <tt:SessionTimeout>PT60S</tt:SessionTimeout>
 </media:Configuration>
 <media:ForcePersistence>false</media:ForcePersistence>
 </media:SetMetadataConfiguration>
 </SOAP-ENV:Body>
</SOAP-ENV:Envelope>

Request: media.GetProfile
<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://www.w3.org/2003/05/soap-envelope"
 xmlns:SOAP-ENC="http://www.w3.org/2003/05/soap-encoding"
 xmlns:media="http://www.onvif.org/ver10/media/wsdl">
<SOAP-ENV:Body>
 <media:GetProfile>
 <media:ProfileToken>metadata</media:ProfileToken>
 </media:GetProfile>
 </SOAP-ENV:Body>
</SOAP-ENV:Envelope>

Request: media.GetStreamUri
<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://www.w3.org/2003/05/soap-envelope"
 xmlns:tt="http://www.onvif.org/ver10/schema"  xmlns:media="http://www.onvif.org/ver10/media/wsdl">
 <SOAP-ENV:Body>
 <media:GetStreamUri><media:StreamSetup>
 <tt:Stream>RTP-Unicast</tt:Stream>
 <tt:Transport><tt:Protocol>RTSP</tt:Protocol>
 </tt:Transport></media:StreamSetup>
 <media:ProfileToken>metadata</media:ProfileToken>
 </media:GetStreamUri>
 </SOAP-ENV:Body>
</SOAP-ENV:Envelope>

SOAP REQUEST AddPTZConfiguration
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
 xmlns:trt="http://www.onvif.org/ver20/media/wsdl">
 <soap:Body>
 <trt:AddPTZConfiguration>
 <trt:ProfileToken>Profile1</trt:ProfileToken>
 <trt:ConfigurationToken>1</trt:ConfigurationToken>
 </trt:AddPTZConfiguration>
 </soap:Body>
</soap:Envelope>

SOAP REQUEST SetConfiguration
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
 xmlns:tptz="http://www.onvif.org/ver20/ptz/wsdl"
 xmlns:tt="http://www.onvif.org/ver10/schema">
 <soap:Body>
 <tptz:SetConfiguration>
 <tptz:PTZConfiguration token="1">
 <tt:Name>default</tt:Name>
 <tt:UseCount>0</tt:UseCount>
 <tt:NodeToken>1</tt:NodeToken>
 <tt:DefaultAbsolutePantTiltPositionSpace>
http://www.onvif.org/ver10/tptz/PanTiltSpaces/SphericalPositionSpace
</tt:DefaultAbsolutePantTiltPositionSpace>
 <tt:DefaultAbsoluteZoomPositionSpace>
http://www.onvif.org/ver10/tptz/ZoomSpaces/PositionGenericSpace
</tt:DefaultAbsoluteZoomPositionSpace>
 <tt:DefaultRelativePanTiltTranslationSpace>
http://www.onvif.org/ver10/tptz/PanTiltSpaces/TranslationGenericSpace
</tt:DefaultRelativePanTiltTranslationSpace>
 <tt:DefaultRelativeZoomTranslationSpace>
http://www.onvif.org/ver10/tptz/ZoomSpaces/TranslationGenericSpace
</tt:DefaultRelativeZoomTranslationSpace>
 <tt:DefaultContinuousPanTiltVelocitySpace>
http://www.onvif.org/ver10/tptz/PanTiltSpaces/VelocityGenericSpace
</tt:DefaultContinuousPanTiltVelocitySpace>
 <tt:DefaultContinuousZoomVelocitySpace>
http://www.onvif.org/ver10/tptz/ZoomSpaces/VelocityGenericSpace
</tt:DefaultContinuousZoomVelocitySpace>
 <tt:DefaultPTZSpeed>
 <tt:PanTilt
space="http://www.onvif.org/ver10/tptz/PanTiltSpaces/SpeedSpaceDegrees"
 y="90" x="90">
 </tt:PanTilt>
 <tt:Zoom
 space="http://www.onvif.org/ver10/tptz/ZoomSpaces/ZoomGenericSpeedSpace"
 x="1">
 </tt:Zoom>
 </tt:DefaultPTZSpeed>
 <tt:DefaultPTZTimeout>PT60S</tt:DefaultPTZTimeout>
 </tptz:PTZConfiguration>
 <tptz:ForcePersistence>true</tptz:ForcePersistence>
 </tptz:SetConfiguration>
 </soap:Body>
</soap:Envelope>

SOAP REQUEST ContinuousMove 입력 값은 없지만 좌표 설정
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
 xmlns:tptz="http://www.onvif.org/ver20/ptz/wsdl"
 xmlns:tt="http://www.onvif.org/ver10/schema">
 <soap:Body>
 <tptz:ContinuousMove>
 <tptz:ProfileToken>Profile1</tptz:ProfileToken>
 <tptz:Velocity>
 <tt:PanTilt x="1" y="1"/>
 <tt:Zoom x="1"/>
 </tptz:Velocity>
 </tptz:ContinuousMove>
 </soap:Body>
</soap:Envelope>

SOAP REQUEST Stop
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
 xmlns:tptz="http://www.onvif.org/ver20/ptz/wsdl">
 <soap:Body>
 <tptz:Stop>
 <tptz:ProfileToken>Profile1</tptz:ProfileToken>
 <tptz:PanTilt>true</tptz:PanTilt>
 <tptz:Zoom>true</tptz:Zoom>
 </tptz:Stop>
 </soap:Body>
</soap:Envelope>

SOAP REQUEST SetPreset
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
 xmlns:tptz="http://www.onvif.org/ver20/ptz/wsdl">
 <soap:Body>
 <tptz:SetPreset>
 <tptz:ProfileToken>Profile1</tptz:ProfileToken>
 <tptz:PresetName>PresetName1</tptz:PresetName>
 </tptz:SetPreset>
 </soap:Body>
</soap:Envelope>

SOAP REQUEST GetPreset
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
 xmlns:tptz="http://www.onvif.org/ver20/ptz/wsdl">
 <soap:Body>
 <tptz:GetPresets>
 <tptz:ProfileToken>Profile1</tptz:ProfileToken>
 </tptz:GetPresets>
 </soap:Body>
</soap:Envelope>

SOAP REQUEST GotoPreset
<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
 xmlns:tptz="http://www.onvif.org/ver20/ptz/wsdl">
 <soap:Body>
 <tptz:GotoPreset>
 <tptz:ProfileToken>Profile1</tptz:ProfileToken>
 <tptz:PresetToken>Preset1</tptz:PresetToken>
 </tptz:GotoPreset>
 </soap:Body>
</soap:Envelope>

Request events.GetEventProperties
<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://www.w3.org/2003/05/soap-envelope"
 xmlns:wsa="http://www.w3.org/2005/08/addressing"
 xmlns:tev="http://www.onvif.org/ver10/events/wsdl">
 <SOAP-ENV:Header><wsa:Action>
http://www.onvif.org/ver10/events/wsdl/EventPortType/GetEventPropertiesRequest
 </wsa:Action>
 <wsa:To>http://169.254.76.145/onvif/services</wsa:To>
 </SOAP-ENV:Header>
 <SOAP-ENV:Body>
 <tev:GetEventProperties/>
 </SOAP-ENV:Body>
</SOAP-ENV:Envelope> 

Request events.CreatePullPointSubscription 
<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://www.w3.org/2003/05/soap-envelope"
 xmlns:wsa="http://www.w3.org/2005/08/addressing"
 xmlns:wsnt="http://docs.oasis-open.org/wsn/b-2"
 xmlns:tev="http://www.onvif.org/ver10/events/wsdl"
 xmlns:tns1="http://www.onvif.org/ver10/topics"
 xmlns:tnsvendor="http://www.vendor.com/2009/event/topics">
 <SOAP-ENV:Header>
 <wsa:Action>
http://www.onvif.org/ver10/events/wsdl/EventPortType/CreatePullPointSubscriptionRequest
 </wsa:Action>
 <wsa:To>http://169.254.76.145/onvif/services</wsa:To>
 </SOAP-ENV:Header>
 <SOAP-ENV:Body>
 <tev:CreatePullPointSubscription>
 <tev:Filter>
 <wsnt:TopicExpression Dialect="http://www.onvif.org/ver10/tev/topicExpression/C
oncreteSet">tns1:Device/tnsvendor:IO//.|tns1:Device/tnsvendor:Sensor/PIR</wsnt:TopicExpression>
 </tev:Filter>
 <tev:InitialTerminationTime>PT1M</tev:InitialTerminationTime>
 </tev:CreatePullPointSubscription>
 </SOAP-ENV:Body>
</SOAP-ENV:Envelope> 

Request: events.PullMessages
<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://www.w3.org/2003/05/soap-envelope"
 xmlns:wsa="http://www.w3.org/2005/08/addressing"
 xmlns:tev="http://www.onvif.org/ver10/events/wsdl">
 <SOAP-ENV:Header>
 <wsa:Action>http://www.onvif.org/ver10/events/wsdl/PullPointSubscription/PullMessagesRequest</wsa:Action>
 <wsa:To>http://192.168.1.24/onvif/services</wsa:To>
 <dom0:SubscriptionId xmlns:dom0="http://www.example.com/2009/event">6</dom0:SubscriptionId>
 </SOAP-ENV:Header>
 <SOAP-ENV:Body>
 <tev:PullMessages>
 <tev:Timeout>PT5S</tev:Timeout>
 <tev:MessageLimit>1</tev:MessageLimit>
 </tev:PullMessages>
 </SOAP-ENV:Body>
</SOAP-ENV:Envelope>

Request events.Subscribe
<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://www.w3.org/2003/05/soap-envelope"
 xmlns:wsa="http://www.w3.org/2005/08/addressing"
 xmlns:wsnt="http://docs.oasis-open.org/wsn/b-2">
 <SOAP-ENV:Header>
 <wsa:Action>http://docs.oasis-open.org/wsn/bw2/NotificationProducer/SubscribeRequest</wsa:Action>
 <wsa:To>http://169.254.232.42/onvif/services</wsa:To>
 </SOAP-ENV:Header>
 <SOAP-ENV:Body>
 <wsnt:Subscribe>
 <wsnt:ConsumerReference>
<wsa:Address>http://10.96.6.4:8000/consumerinterface?from=192.168.1.16%26serno=00408C1837C1</wsa:Address>
 </wsnt:ConsumerReference>
 <wsnt:InitialTerminationTime>PT1M</wsnt:InitialTerminationTime>
</wsnt:Subscribe>
 </SOAP-ENV:Body>
</SOAP-ENV:Envelope>

Request deviceIO:GetAudioOutputConfiguration
<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://www.w3.org/2003/05/soap-envelope">
 <SOAP-ENV:Body>
 <tmd:GetAudioOutputConfiguration
xmlns:tmd="http://www.onvif.org/onvif/ver10/deviceIO/wsdl">
 <tmd:AudioOutputToken>AudioOut</tmd:AudioOutputToken>
 </tmd:GetAudioOutputConfiguration>
 </SOAP-ENV:Body>
</SOAP-ENV:Envelope>

Request media:AddAudioOutputConfiguration
<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://www.w3.org/2003/05/soap-envelope" >
 <SOAP-ENV:Body>
 <trt:AddAudioOutputConfiguration
xmlns:trt="http://www.onvif.org/ver10/media/wsdl">
 <trt:ProfileToken>Profile0</trt:ProfileToken>
 <trt:ConfigurationToken>AudioOutCfg</trt:ConfigurationToken>
 </trt:AddAudioOutputConfiguration>
 </SOAP-ENV:Body>
</SOAP-ENV:Envelope>

Request media:AddAudioDecoderConfiguration
<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://www.w3.org/2003/05/soap-envelope">
 <SOAP-ENV:Body>
 <trt:AddAudioDecoderConfiguration
xmlns:trt="http://www.onvif.org/ver10/media/wsdl">
 <trt:ProfileToken>Profile0</trt:ProfileToken>
 <trt:ConfigurationToken>AudioDecCfg</trt:ConfigurationToken>
 </trt:AddAudioDecoderConfiguration>
 </SOAP-ENV:Body>
</SOAP-ENV:Envelope>

Request recording:SetRecordingConfiguration
<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://www.w3.org/2003/05/soap-envelope"
xmlns:tt="http://www.onvif.org/ver10/schema">
 <SOAP-ENV:Body>
 <trc:SetRecordingConfiguration xmlns:trc="http://www.onvif.org/recording/wsdl">
 <trc:RecordingToken>Rec0</trc:RecordingToken>
 <trc:RecordingConfiguration>
 <tt:Source>
 <tt:SourceId>Device 1</tt:SourceId>
 <tt:Name>camera PT677X</tt:Name>
 <tt:Location>Room1</tt:Location>
 <tt:Description>continuous recording of room 1</tt:Description>
 <tt:Address>192.168.0.2</tt:Address>
 </tt:Source>
 <tt:Content>Recording from device 1</tt:Content>
 <tt:MaximumRetentionTime>PT0S</tt:MaximumRetentionTime>
 </trc:RecordingConfiguration>
 </trc:SetRecordingConfiguration>
 </SOAP-ENV:Body>
</SOAP-ENV:Envelope>

Request recording:CreateRecordingJob
<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://www.w3.org/2003/05/soap-envelope"
xmlns:tt="http://www.onvif.org/ver10/schema">
 <SOAP-ENV:Body>
 <trc:CreateRecordingJob xmlns:trc="http://www.onvif.org/recording/wsdl">
 <trc:JobConfiguration>
 <tt:RecordingToken>Rec0</tt:RecordingToken>
 <tt:Mode>Active</tt:Mode>
 <tt:Priority>1</tt:Priority>
 <tt:Source>
 <tt:SourceToken Type="http://www.onvif.org/ver10/schema/Profile">
 <tt:Token>Profile1</tt:Token>
 </tt:SourceToken>
 <tt:AutoCreateReceiver>false</tt:AutoCreateReceiver>
 </tt:Source>
 </trc:JobConfiguration>
 </trc:CreateRecordingJob>
 </SOAP-ENV:Body>
</SOAP-ENV:Envelope>

Request search:FindEvents
<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://www.w3.org/2003/05/soap-envelope"
xmlns:tt="http://www.onvif.org/ver10/schema" xmlns:wsnt="http://docs.oasisopen.org/wsn/b-2" xmlns:tns1="http://www.onvif.org/ver10/topics">
 <SOAP-ENV:Body>
 <tse:FindEvents xmlns:tse="http://www.onvif.org/search/wsdl">
 <tse:StartPoint>2010-12-24T08:00:00.0Z</tse:StartPoint>
 <tse:EndPoint>2001-12-17T09:30:47.0Z</tse:EndPoint>
 <tse:Scope>
 	<tt:IncludedRecordings>MyRec</tt:IncludedRecordings>
 </tse:Scope>
 <tse:SearchFilter>
 <wsnt:TopicExpression
Dialect="http://www.onvif.org/ver10/tev/topicExpression/ConcreteSet">
 tns1:RecordingHistory/Track/State
 </wsnt:TopicExpression>
 </tse:SearchFilter>
 <tse:IncludeStartState>false</tse:IncludeStartState>
 <tse:MaxMatches>100</tse:MaxMatches>
 <tse:KeepAliveTime>PT1M</tse:KeepAliveTime>
 </tse:FindEvents>
 </SOAP-ENV:Body>
</SOAP-ENV:Envelope>

Request search:GetRecordingSearchResult
<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://www.w3.org/2003/05/soap-envelope">
 <SOAP-ENV:Body>
 <tse:GetRecordingSearchResults xmlns:tse="http://www.onvif.org/search/wsdl">
 <tse:SearchToken>MySearchToken</tse:SearchToken>
 <tse:WaitTime>PT1M</tse:WaitTime>
 </tse:GetRecordingSearchResults>
 </SOAP-ENV:Body>
</SOAP-ENV:Envelope>

SOAP REQUEST GetPaneConfiguration
<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:tmd="http://www.onvif.org/onvif/ver10/display/wsdl">
<soap:Body>
 <tmd:GetPaneConfiguration>
 <tmd:VideoOutput>VideoOut0</tmd:VideoOutput>
 <tmd:Pane>PaneConfig0</tmd:Pane>
 </tmd:GetPaneConfiguration>
 </soap:Body>
</soap:Envelope>

SOAP REQUEST SetPaneConfiguration
<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:tmd="http://www.onvif.org/onvif/ver10/display/wsdl" xmlns:tt="http://www.onvif.org/ver10/schema">
<soap:Body>
 <tmd:SetPaneConfiguration>
 <tmd:VideoOutput>VideoOutput0</tmd:VideoOutput>
 <tmd:PaneConfiguration>
 <tt:PaneName>PaneName0</tt:PaneName>
 <tt:ReceiverToken>ReceiverToken0</tt:ReceiverToken>
 <tt:Token>PaneToken0</tt:Token>
 </tmd:PaneConfiguration>
 </tmd:SetPaneConfiguration>
 </soap:Body>
</soap:Envelope>

SOAP REQUEST SetReceiverMode
<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:tmd="http://www.onvif.org/onvif/ver10/display/wsdl">
<soap:Body>
 <soap:Body>
 <tmd:SetReceiverMode>
 <tmd:ReceiverToken>ReceiverToken0</tmd:ReceiverToken>
 <tmd:Mode>AlwaysConnect</tmd:Mode>
 </tmd:SetReceiverMode>
 </soap:Body>
 </soap:Body>
</soap:Envelope>

SOAP REQUEST SetReceiverMode
<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:tmd="http://www.onvif.org/onvif/ver10/display/wsdl">
<soap:Body>
 <tmd:GetLayout>
 <tmd:VideoOutput>VideoOutputToken0</tmd:VideoOutput>
 </tmd:GetLayout>
 </soap:Body>
</soap:Envelope>

SOAP REQUEST GetLayout
<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:tmd="http://www.onvif.org/onvif/ver10/display/wsdl">
<soap:Body>
 <tmd:GetDisplayOptions>
 	<tmd:VideoOutput>VideoOutputToken0</tmd:VideoOutput>
 </tmd:GetDisplayOptions>
 </soap:Body>
</soap:Envelope> 

SOAP REQUEST GetDisplayOptions
<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:tmd="http://www.onvif.org/onvif/ver10/display/wsdl" xmlns:tt="http://www.onvif.org/ver10/schema">
<soap:Body>
 <tmd:CreatePaneConfiguration>
 <tmd:VideoOutput>VideoOutputToken0</tmd:VideoOutput>
 <tmd:PaneConfiguration>
 <tt:PaneName>PaneName0</tt:PaneName>
 <tt:ReceiverToken>ReveiverToken0</tt:ReceiverToken>
 <tt:Token>PaneToken0</tt:Token>
 </tmd:PaneConfiguration>
 </tmd:CreatePaneConfiguration>
</soap:Body>
</soap:Envelope>

REQUEST SetLayout
<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:tmd="http://www.onvif.org/onvif/ver10/display/wsdl" xmlns:tt="http://www.onvif.org/ver10/schema">
<soap:Body>
 <tmd:SetLayout>
 <tmd:VideoOutput>?</tmd:VideoOutput>
 <tmd:Layout>
 <tt:PaneLayout>
 <tt:Pane>PaneToken0</tt:Pane>
 <tt:Area bottom="-1.0" top="0.0" right="0.0" left="-1.0"/>
 </tt:PaneLayout>
 <tt:PaneLayout>
 <tt:Pane>PaneToken1</tt:Pane>
 <tt:Area bottom="0.0" top="1.0" right="1.0" left="0.0"/>
 </tt:PaneLayout>
 </tmd:Layout>
 </tmd:SetLayout>
 </soap:Body>
</soap:Envelope>

REQUEST DeletePaneConfiguration
<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:tmd="http://www.onvif.org/onvif/ver10/display/wsdl">
<soap:Body>
 <tmd:DeletePaneConfiguration>
 <tmd:VideoOutput>VideoOut0</tmd:VideoOutput>
 <tmd:PaneToken>Pane0</tmd:PaneToken>
 </tmd:DeletePaneConfiguration>
 </soap:Body>
</soap:Envelope>

Request display:SetLayout
<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:tmd="http://www.onvif.org/onvif/ver10/display/wsdl" xmlns:tt="http://www.onvif.org/ver10/schema">
 <soap:Body>
 <tmd:SetLayout>
 <tmd:VideoOutput>?</tmd:VideoOutput>
 <tmd:Layout>
 <tt:PaneLayout>
 <tt:Pane>PaneToken0</tt:Pane>
 <tt:Area bottom="0.0" top="1.0" right="0.0" left="-1.0" />
 </tt:PaneLayout>
 <tt:PaneLayout>
 <tt:Pane>PaneToken1</tt:Pane>
 <tt:Area bottom="0.0" top="1.0" right="1.0" left="0.0"/>
 </tt:PaneLayout>
 <tt:PaneLayout>
 <tt:Pane>PaneToken2</tt:Pane>
 <tt:Area bottom="-1.0" top="0.0" right="0.0" left="-1.0"/>
 </tt:PaneLayout>
 <tt:PaneLayout>
 <tt:Pane>PaneToken3</tt:Pane>
 <tt:Area bottom="-1.0" top="0.0" right="1.0" left="0.0"/>
 </tt:PaneLayout>
 </tmd:Layout>
 </tmd:SetLayout>
 </soap:Body>
</soap:Envelope>
 
Request receiver:CreateReceiver
<?xml version="1.0" encoding="UTF-8"?>
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:tmd="http://www.onvif.org/ver10/receiver/wsdl" xmlns:tt="http://www.onvif.org/ver10/schema">
 <soap:Body>
 <tmd:CreateReceiver>
 <tmd:Configuration>
 <tt:Mode>NeverConnect</tt:Mode>
 <tt:MediaUri>http://4.5.6.7/media/live</tt:MediaUri>
 <tt:StreamSetup>
 <tt:Stream>UDP-Unicast</tt:Stream>
 <tt:Transport>
 <tt:Protocol>HTTP</tt:Protocol>
 </tt:Transport>
 </tt:StreamSetup>
 </tmd:Configuration>
 </tmd:CreateReceiver>
 </soap:Body>
</soap:Envelope>

