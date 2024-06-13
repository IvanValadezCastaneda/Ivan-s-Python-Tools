from pymodbus.client import ModbusTcpClient
import struct

# Ensure you're using the correct port and timeout
client = ModbusTcpClient("client", port=502, timeout=20)

if client.connect():
    response = client.read_holding_registers(143,2)

    if response.isError() or not response.registers:
        print("Error reading registers or insufficient data")
    else:
        reg1 = response.registers[0]
        reg2 = response.registers[1]
        hex1 = f'{reg1:04x}'
        hex2 = f'{reg2:04x}'

        # Combine to form a 32-bit float (Big-endian)
        combined_bytes = bytes.fromhex(hex1 + hex2)
        big_endian_float = struct.unpack('>f', combined_bytes)[0]

        # Combine to form a 32-bit float (Little-endian)
        combined_bytes = bytes.fromhex(hex2 + hex1)
        little_endian_float = struct.unpack('<f', combined_bytes)[0]

        print("Big-endian float:", big_endian_float)
        print("Little-endian float:", little_endian_float)
else:
    print("Failed to connect to the Modbus server")
