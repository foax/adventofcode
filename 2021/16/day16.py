import fileinput
from functools import reduce
from pprint import pprint


def load_input(iterator):
    input = next(iterator).strip()
    for _ in iterator:
        pass
    return input


def convert_to_bits(input):
    '''Converts a string of hex to bits.'''
    for x in input:
        yield int(x, 16)


def next_bits(input):
    '''A generator that returns the number of bits asked for via send.'''
    x = 0
    available_bits = 0
    bit_iterator = convert_to_bits(input)
    bits = None

    while True:
        wanted_bits = yield bits
        while available_bits < wanted_bits:
            x = (x << 4) + next(bit_iterator)
            available_bits += 4
        available_bits -= wanted_bits
        bits = x >> available_bits
        x = x - (bits << available_bits)


def parse_packet(bit_gen):
    packet = {'bit_count': 0}
    packet['version'] = bit_gen.send(3)
    packet['bit_count'] += 3
    packet['type_id'] = bit_gen.send(3)
    packet['bit_count'] += 3

    if packet['type_id'] == 4:
        # Raw value
        value = 0
        cont = 1
        while cont:
            bits = bit_gen.send(5)
            packet['bit_count'] += 5
            cont = bits & 16
            value = (value << 4) + (bits & 15)
        packet['value'] = value
        return packet

    # Operator packet
    packet['values'] = []
    packet['length_type_id'] = bit_gen.send(1)
    packet['bit_count'] += 1
    packet['sub_packets'] = []

    if packet['length_type_id'] == 0:
        # Length specified by number of bits
        length = bit_gen.send(15)
        packet['bit_count'] += 15
        while length > 0:
            sub_packet = parse_packet(bit_gen)
            packet['values'].append(sub_packet['value'])
            packet['bit_count'] += sub_packet['bit_count']
            packet['sub_packets'].append(sub_packet)
            length = length - sub_packet['bit_count']

    else:
        # Length specified by operator count
        op_count = bit_gen.send(11)
        packet['bit_count'] += 11
        for _ in range(op_count):
            sub_packet = parse_packet(bit_gen)
            packet['values'].append(sub_packet['value'])
            packet['bit_count'] += sub_packet['bit_count']
            packet['sub_packets'].append(sub_packet)

    if packet['type_id'] == 0:
        packet['value'] = sum(packet['values'])
    elif packet['type_id'] == 1:
        packet['value'] = reduce(lambda x, y: x*y, packet['values'])
    elif packet['type_id'] == 2:
        packet['value'] = min(packet['values'])
    elif packet['type_id'] == 3:
        packet['value'] = max(packet['values'])
    elif packet['type_id'] == 5:
        packet['value'] = int(packet['values'][0] > packet['values'][1])
    elif packet['type_id'] == 6:
        packet['value'] = int(packet['values'][0] < packet['values'][1])
    elif packet['type_id'] == 7:
        packet['value'] = int(packet['values'][0] == packet['values'][1])

    return packet


def sum_packet_version(packet):
    version_sum = packet['version']
    if 'sub_packets' in packet:
        for p in packet['sub_packets']:
            version_sum += sum_packet_version(p)
    return version_sum


def main():
    bits = load_input(fileinput.input())
    bit_gen = next_bits(bits)
    next(bit_gen)
    packet = parse_packet(bit_gen)
    version_sum = sum_packet_version(packet)
    print(f'Version sum: {version_sum}; Value: {packet["value"]}')


if __name__ == '__main__':
    main()
