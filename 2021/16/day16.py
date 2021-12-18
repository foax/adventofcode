import fileinput
from functools import reduce


def load_input(iterator):
    input = next(iterator).strip()
    for _ in iterator:
        pass
    return input


def convert_to_bits(input):
    for x in input:
        yield int(x, 16)


def next_bits(input):
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


def parse_packet(bit_gen, bit_count=0):
    version = bit_gen.send(3)
    bit_count += 3
    type_id = bit_gen.send(3)
    bit_count += 3
    print(
        f'Version: {version} ({version:03b}), Type ID: {type_id} ({type_id:03b})')

    if type_id == 4:
        value = 0
        cont = 1
        while cont:
            bits = bit_gen.send(5)
            print(f'got bits {bits:05b}')
            bit_count += 5
            cont = bits & 16
            value = (value << 4) + (bits & 15)
            print(f'new value is {value} ({bin(value)})')

    else:
        value, parsed_version, bit_count = parse_length(
            type_id, bit_gen, bit_count)
        version += parsed_version

    return value, version, bit_count


def parse_length(type_id, bit_gen, bit_count):
    values = []
    version = 0
    length_type_id = bit_gen.send(1)
    print(f'Length type: {length_type_id}')
    bit_count += 1
    if length_type_id == 0:
        length = bit_gen.send(15)
        bit_count += 15
        print(f'Length in bits: {length} ({length:015b})')
        while length > 0:
            value, parsed_version, new_bit_count = parse_packet(
                bit_gen, bit_count)
            length = length - (new_bit_count - bit_count)
            bit_count = new_bit_count
            version += parsed_version
            values.append(value)

    else:
        op_count = bit_gen.send(11)
        bit_count += 11
        print(f'Length in op count: {op_count} ({op_count:011b})')
        for _ in range(op_count):
            value, parsed_version, bit_count = parse_packet(bit_gen, bit_count)
            version += parsed_version
            print(f'Parsed op count {op_count}')
            values.append(value)

    print(f'type_id: {type_id}; values: {values}')
    if type_id == 0:
        value = sum(values)
    elif type_id == 1:
        value = reduce(lambda x, y: x*y, values)
    elif type_id == 2:
        value = min(values)
    elif type_id == 3:
        value = max(values)
    elif type_id == 5:
        value = int(values[0] > values[1])
    elif type_id == 6:
        value = int(values[0] < values[1])
    elif type_id == 7:
        value = int(values[0] == values[1])

    return value, version, bit_count


def main():
    bits = load_input(fileinput.input())
    bit_gen = next_bits(bits)
    next(bit_gen)
    value, version, bit_count = parse_packet(bit_gen, 0)
    print(value, version, bit_count)


if __name__ == '__main__':
    main()
