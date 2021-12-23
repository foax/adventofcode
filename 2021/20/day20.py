import fileinput


class IeaImage:
    def __init__(self):
        self.iea = None
        self.pixels = set()
        self.bounds = {0: {'min': None, 'max': None},
                       1: {'min': None, 'max': None}}
        self.oob_default = False

    def add_pixel(self, pixel):
        self.pixels |= {pixel}
        self.update_bounds(pixel)

    def update_bounds(self, pixel):
        for i in range(2):
            if self.bounds[i]['min'] is None or pixel[i] < self.bounds[i]['min']:
                self.bounds[i]['min'] = pixel[i]
            if self.bounds[i]['max'] is None or pixel[i] > self.bounds[i]['max']:
                self.bounds[i]['max'] = pixel[i]

    def load(self, iterator):
        y = 0
        for line in iterator:
            line = line.strip()
            if not line:
                continue

            if not self.iea:
                self.iea = {i: x == '#' for i, x in enumerate(line)}
                continue

            for pixel in [(x, y) for x, pixel in enumerate(line) if pixel == '#']:
                self.add_pixel(pixel)

            y += 1

    def in_bounds(self, pixel):
        return pixel[0] >= self.bounds[0]['min'] and pixel[0] <= self.bounds[0]['max'] and pixel[1] >= self.bounds[1]['min'] and pixel[1] <= self.bounds[1]['max']

    def enhance_pixel(self, pixel):
        value = 0
        for y in range(pixel[1]-1, pixel[1]+2):
            for x in range(pixel[0]-1, pixel[0]+2):
                if self.in_bounds((x, y)):
                    new_value = int((x, y) in self.pixels)
                else:
                    new_value = int(self.oob_default)
                value = (value << 1) + new_value
        return self.iea[value]

    def enhance(self):
        new_image = IeaImage()
        new_image.iea = self.iea
        for y in range(self.bounds[1]['min'] - 2, self.bounds[1]['max'] + 3):
            for x in range(self.bounds[0]['min'] - 2, self.bounds[0]['max'] + 3):
                pixel = (x, y)
                if self.enhance_pixel(pixel):
                    new_image.add_pixel(pixel)
        new_image.oob_default = new_image.iea[int(self.oob_default) * 511]
        self.pixels = new_image.pixels
        self.bounds = new_image.bounds
        self.oob_default = new_image.oob_default

    def on_pixels(self):
        return len(self.pixels)

    def __str__(self):
        col = []
        for y in range(self.bounds[1]['min'], self.bounds[1]['max'] + 1):
            row = []
            for x in range(self.bounds[0]['min'], self.bounds[0]['max'] + 1):
                if (x, y) in self.pixels:
                    row.append('#')
                else:
                    row.append('.')
            col.append(''.join(row))
        return '\n'.join(col)


def main():
    image = IeaImage()
    image.load(fileinput.input())
    for i in range(50):
        image.enhance()
        if i == 1:
            part_1 = image.on_pixels()

    print(f'Part 1: {part_1}; Part 2: {image.on_pixels()}')
    # print(str(image))


if __name__ == '__main__':
    main()
