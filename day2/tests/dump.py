import struct

import sys
 
op_names = {
    0: 'LA', 1: 'LV', 2: 'LC', 3: 'LI', 4: 'INT', 5: 'DCT',
    6: 'J', 7: 'FJ', 8: 'HL', 9: 'ST', 10: 'CALL', 11: 'EP',
    12: 'EF', 13: 'RC', 14: 'RI', 15: 'WRC', 16: 'WRI', 17: 'WLN',
    18: 'AD', 19: 'SB', 20: 'ML', 21: 'DV', 22: 'NEG', 23: 'CV',
    24: 'EQ', 25: 'NE', 26: 'GT', 27: 'LT', 28: 'GE', 29: 'LE', 30: 'BP'
}
 
def dump(filename):
    with open(filename, 'rb') as f:
        data = f.read()
    for i in range(0, len(data), 12):
        inst = data[i:i+12]
        if len(inst) < 12:
            break

        op, p, q = struct.unpack('<III', inst)
        name = op_names.get(op, f'OP({op})')
        
        # Compact formatting
        if name in ('INT', 'DCT', 'J', 'FJ', 'LC'):
            print(f'  {name} {q}')
        elif name in ('LA', 'LV', 'CALL'):
            print(f'  {name} {p},{q}')
        else:
            print(f'  {name}')
 
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python dump_code.py <binary_file>')
    else:
        dump(sys.argv[1])

 