import fileinput
import re

def probe(x_velocity, y_velocity):
    x, y = 0, 0
    while True:
        x += x_velocity
        y += y_velocity
        x_velocity -= ((x_velocity > 0) - (x_velocity < 0))
        y_velocity -= 1
        yield (x, y)

def get_target_area(line):
    # target area: x=20..30, y=-10..-5
    match = re.match('target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)', line)
    return ((int(match.group(1)), int(match.group(2))), (int(match.group(3)), int(match.group(4))))

def in_target(x, y, target):
    return x >= target[0][0] and x <= target[0][1] and y >= target[1][0] and y <= target[1][1]

def past_target(x, y, target):
    return x > target[0][1] or y < target[1][0]

def test_velocity(x_vel, y_vel, target):
    max_y = None
    x, y = 0, 0
    p = probe(x_vel, y_vel)
    while not past_target(x, y, target):
        old_x, old_y = x, y
        x, y = next(p)
        print(x, y)
        if max_y is None or y > max_y: max_y = y
        if in_target(x, y, target):
            return max_y, (x, y), (x - old_x, y - old_y)
    return False, (x, y), (x - old_x, y - old_y)

def find_x_velocities(target):
    x_list = []
    x_vel = target[0][1]
    # max_iter = None
    
    while x_vel > 0:
        x = 0
        step = x_vel
        iter = 0
        # print(f'x vel: {x_vel}; ', end='')
        while step > 0:
            x += step
            # print(f'{x} ', end='')
            iter += 1
            if x >= target[0][0] and x <= target[0][1]:
                # print(f'HIT after {iter} iterations')
                x_list.append(x_vel)
                # if max_iter is None or iter > max_iter:
                #     max_iter = iter
                break
            if x > target[0][1]:
                # print(f'MISS after {iter} iterations')
                break
            step -= 1
        # if step == 0:
            # print(f'MISS after {iter} iterations')
        x_vel -= 1
    return x_list

# def find_y_velocities(target, max_iter):
#     y_list = []
#     y_vel = target[1][0]
    
#     while True:
#         y = 0
#         step = y_vel
#         iter = 0
#         print(f'y vel: {y_vel}; ', end='')

#         while y >= target[1][0]:
#             y += step
#             print(f'{y} ', end='')
#             iter += 1
#             if iter > max_iter:
#                 print(f'MISS after {iter} iterations')
#                 break
#             if y >= target[1][0] and y <= target[1][1]:
#                 print(f'HIT after {iter} iterations')
#                 y_list.append(y_vel)
#                 break
#             step -= 1
#         if iter > max_iter and y > target[1][1]:
#             break
#         y_vel += 1

#     return y_list
 

def main():
    target = None
    for line in fileinput.input():
        if not target:
            target = get_target_area(line.strip())

    x_vels = find_x_velocities(target)

    max_y = None
    results = []
    for x_vel in x_vels:
        y_vel = target[1][0]
        while True:
            # print(f'velocity: ({x_vel}, {y_vel})')
            result, final_coords, final_velocity = test_velocity(x_vel, y_vel, target)
            # print(result, final_coords, final_velocity)
            if result is not False:
                results.append((x_vel, y_vel))
                if max_y is None or result > max_y:
                    max_y = result
            elif final_coords[0] > target[0][1]:
                break
            elif y_vel > 1000:
                break
            y_vel += 1

    print(max_y)
    print(len(results))
    print(results)


if __name__ == '__main__':
    main()