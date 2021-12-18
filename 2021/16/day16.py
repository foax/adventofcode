import fileinput


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
            value = (value << 4) + (bits ^ 16)
            print(f'new value is {value} ({bin(value)})')
        # waste_bits = 4 - (bit_count % 4)
        # print(f'Number of waste bits: {waste_bits}')
        # bit_gen.send(waste_bits)
        # bit_count += waste_bits
    else:
        parsed_version, bit_count = parse_length(bit_gen, bit_count)
        version += parsed_version

    return version, bit_count


def parse_length(bit_gen, bit_count):
    version = 0
    length_type_id = bit_gen.send(1)
    print(f'Length type: {length_type_id}')
    bit_count += 1
    if length_type_id == 0:
        length = bit_gen.send(15)
        bit_count += 15
        print(f'Length in bits: {length} ({length:015b})')
        while length > 0:
            parsed_version, new_bit_count = parse_packet(bit_gen, bit_count)
            length = length - (new_bit_count - bit_count)
            bit_count = new_bit_count
            version += parsed_version

    else:
        op_count = bit_gen.send(11)
        bit_count += 11
        print(f'Length in op count: {op_count} ({op_count:011b})')
        for _ in range(op_count):
            parsed_version, bit_count = parse_packet(bit_gen, bit_count)
            version += parsed_version
            print(f'Parsed op count {op_count}')

    return version, bit_count


def main():
    bits = load_input(fileinput.input())
    bit_gen = next_bits(bits)
    next(bit_gen)
    version, bit_count = parse_packet(bit_gen, 0)
    print(version, bit_count)


if __name__ == '__main__':
    main()
