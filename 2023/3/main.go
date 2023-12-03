package main

import (
	"bufio"
	"fmt"
	"os"
)

const (
	NULL = iota
	SYMBOL
	PART_NUMBER
)

type part_number struct {
	value int
	x     int
	y     int
}

type schematic_data struct {
	data_type int
	part      *part_number
}

func parse_schematic_line(l string, y int) ([]schematic_data, []*part_number, [][2]int) {
	p := make([]*part_number, 0)
	g := make([][2]int, 0)
	data := make([]schematic_data, len(l))
	new_part_number := &part_number{y: y}

	for i, c := range l {
		if c >= '0' && c <= '9' {
			new_part_number.value = new_part_number.value*10 + int(c-'0')
			data[i].data_type = PART_NUMBER
			data[i].part = new_part_number
		} else {
			if new_part_number.value > 0 {
				new_part_number.x = i - len(fmt.Sprint(new_part_number.value))
				p = append(p, new_part_number)
				new_part_number = &part_number{y: y}
			}
			if c == '.' {
				data[i].data_type = NULL
			} else {
				data[i].data_type = SYMBOL
			}
			if c == '*' {
				g = append(g, [2]int{i, y})
			}
		}
	}
	if new_part_number.value > 0 {
		new_part_number.x = len(l) - len(fmt.Sprint(new_part_number.value))
		p = append(p, new_part_number)
	}
	return data, p, g
}

func check_adjacent_to_symbol(p *part_number, s [][]schematic_data) bool {
	num_len := len(fmt.Sprint(p.value))
	for y := p.y - 1; y <= p.y+1; y++ {
		if y < 0 || y >= len(s) {
			continue
		}
		for x := p.x - 1; x <= p.x+num_len; x++ {
			if x < 0 || x >= len(s[y]) {
				continue
			}
			if y == p.y && x >= p.x && x <= p.x+num_len-1 {
				continue
			}
			if s[y][x].data_type == SYMBOL {
				return true
			}
		}
	}
	return false
}

func gear_ratio(g [2]int, s [][]schematic_data) int {
	var last_num *part_number
	for y := g[1] - 1; y <= g[1]+1; y++ {
		if y < 0 || y >= len(s) {
			continue
		}
		for x := g[0] - 1; x <= g[0]+1; x++ {
			if s[y][x].data_type == PART_NUMBER {
				if last_num == nil {
					last_num = s[y][x].part
				} else if last_num != s[y][x].part {
					return last_num.value * s[y][x].part.value
				}
			}
		}
	}
	return 0
}

func main() {

	part_number_list := make([]*part_number, 0)
	gear_list := make([][2]int, 0)
	schematic := make([][]schematic_data, 0)
	f := bufio.NewScanner(os.Stdin)
	f.Split(bufio.ScanLines)

	y := 0
	for f.Scan() {
		l := f.Text()
		d, p, g := parse_schematic_line(l, y)
		schematic = append(schematic, d)
		part_number_list = append(part_number_list, p...)
		gear_list = append(gear_list, g...)
		y++
	}

	part1_total := 0
	for _, p := range part_number_list {
		if check_adjacent_to_symbol(p, schematic) {
			part1_total += p.value
		}
	}

	part2_total := 0
	for _, g := range gear_list {
		part2_total += gear_ratio(g, schematic)
	}

	// fmt.Println(schematic)
	// fmt.Println(part_number_list)
	fmt.Printf("Part 1: %d\n", part1_total)
	fmt.Printf("Part 2: %d\n", part2_total)

}
