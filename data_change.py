import pydivert

with pydivert.WinDivert("tcp and tcp.PayloadLength > 0") as w:
    
    for packet in w:
        
        if packet.is_inbound:
            origin_data = packet.tcp.payload
            modify_data = origin_data.replace('Michael', 'Gilbert')
            packet.tcp.payload = modify_data
        if packet.is_outbound:
            data = packet.tcp.payload
            if data.find('\x0d\x0a\x0d\x0a') != -1:
                head = data.split('\x0d\x0a\x0d\x0a')[0]
                body = data.split('\x0d\x0a\x0d\x0a')[1]
                head = head.replace('Accept-Encoding: gzip', 'Accept-Encoding:     ')
                packet.tcp.payload = head+'\x0d\x0a\x0d\x0a'+body
            
        w.send(packet, recalculate_checksum=True)
