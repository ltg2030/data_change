import pydivert

with pydivert.WinDivert("tcp and tcp.PayloadLength > 0") as w:
    
    for packet in w:
        
        if packet.is_inbound == True:
            origin_payload = packet.tcp.payload
            modify_payload = origin_payload.replace(b'Michael', b'Gilbert')
            packet.tcp.payload = data
            
        if packet.is_outbound == True:
            data = packet.tcp.payload
            print datar
            data = data.replace(b'Accept-Encoding: gzip', b'Accept-Encoding:     ')
            packet.tcp.payload = data
            
        w.send(packet, recalculate_checksum=True)
