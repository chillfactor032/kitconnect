import math
import time

def pack4(n: int):
    out = []
    for i in range(4):
        out.append((n >> 21) & 0x7f)
        n <<= 7
    return out

def unpack4(n: list):
    out = 0
    for x in range(len(n)):
        out += n[x] << ((len(n)-1-x)*7)
    return out

def unpack4_2(n: list):
    m = n.copy()
    m.reverse()
    out = 0
    for x in range(len(m)):
        out += m[x] << (x*7)
    return out

def kit_id_to_addr(kit_id: int):
    base = 4<<21
    step = 2<<14
    return pack4(base + kit_id * step)

def addr_to_kit_id(addr: list):
    base = 4<<21
    step = 2<<14
    return int((unpack(addr) - base) / step)

def list_to_int(lst): 
    result = 0
    for i in lst: 
        result = (result << 7) | i 
    return result 

def unpack(arr: list) -> int:
    out = 0
    for x in arr:
        out = (out << 7) + x
    return out



addr = [0x05, 0x46, 0x00, 0x00]
print(addr)
print(addr_to_kit_id(addr))
print(addr)
print(list_to_int(addr))


for x in range(0,100):
    addr = kit_id_to_addr(x)
    hex_addr = [hex(y) for y in addr]
    calc_kit_id = addr_to_kit_id(addr)
    print(f"kit_id {x}: {hex_addr} ... calculated kit_id: {calc_kit_id}")

