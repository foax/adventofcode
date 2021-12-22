import fileinput
import re
from collections import deque


def load_input(iterator):
    scanners = []
    for line in iterator:
        match = re.match('--- scanner (\d+) ---', line.strip())
        if match:
            scanner = {'id': int(match.group(1)),
                       'location': (0, 0, 0), 'beacons': []}
            scanners.append(scanner)
            continue
        if line.strip():
            x, y, z = (int(x) for x in line.strip().split(','))
            scanner['beacons'].append((x, y, z))
    return scanners


def rotate_90(point, axis):
    match axis:
        case 0: return (point[0], -point[2], point[1])
        case 1: return (point[2], point[1], -point[0])
        case 2: return (point[1], -point[0], point[2])


def rotate(point, axis, amount):
    for _ in range(amount):
        point = rotate_90(point, axis)
    return point


def orient_beacons(points):
    for axis, amount in ((0, 0), (0, 2), (2, 1), (2, 3), (0, 1), (0, 3)):
        yield [rotate(p, axis, amount) for p in points]


def rotate_beacons(points):
    for x in range(4):
        yield [rotate(p, 1, x) for p in points]


def relative(a, b):
    return (a[0] - b[0], a[1] - b[1], a[2] - b[2])


def move_point(point, shift):
    return (point[0] + shift[0], point[1] + shift[1], point[2] + shift[2])


def shift_beacons(points, shift):
    return [move_point(p, shift) for p in points]


def check_for_overlap(scanner_a, scanner_b):
    for scanner_b_oriented in orient_beacons(scanner_b):
        for scanner_b_rotated in rotate_beacons(scanner_b_oriented):
            b_rotated = list(scanner_b_rotated)
            for a_root in scanner_a:
                for b_root in b_rotated:
                    b_shift = relative(a_root, b_root)
                    b = shift_beacons(b_rotated, b_shift)
                    matching_beacons = set(scanner_a) & set(b)
                    if len(matching_beacons) >= 12:
                        return b, b_shift
    return None, None


def manhattan(a, b):
    m = 0
    for i in range(3):
        m += abs(a[i] - b[i])
    return m


def main():
    scanners = load_input(fileinput.input())
    checked_scanners = []
    scanner_queue = deque([0])
    while scanner_queue:
        a_idx = scanner_queue.popleft()
        a = scanners[a_idx]
        print(
            f'Checking overlap for scanner {a_idx}; {len(scanner_queue)} waiting in the queue')
        for b_idx, b in enumerate(scanners):
            if a_idx == b_idx or b_idx in checked_scanners or b_idx in scanner_queue:
                continue
            new_beacons, new_shift = check_for_overlap(
                a['beacons'], b['beacons'])
            if new_beacons:
                b['beacons'] = new_beacons
                b['location'] = new_shift
                scanner_queue.append(b_idx)
        checked_scanners.append(a_idx)

    beacons = set()
    for s in scanners:
        beacons |= set(s['beacons'])

    max_dist = 0
    for i, x in enumerate(scanners):
        for y in scanners[i+1:]:
            m = manhattan(x['location'], y['location'])
            if m > max_dist:
                max_dist = m

    print(
        f'Number of beacons: {len(beacons)}; Maximum manhattan distance: {max_dist}')


if __name__ == '__main__':
    main()
