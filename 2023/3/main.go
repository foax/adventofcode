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

func parse_schematic_line(l string, y int, p *[]part_number) []int {
	data := make([]int, len(l))
	new_number := 0
	for i, c := range l {
		switch {
		case c >= '0' && c <= '9':
			new_number = new_number*10 + int(c-'0')
			data[i] = PART_NUMBER
		case c == '.':
			data[i] = NULL
			if new_number > 0 {
				x := part_number{new_number, i - len(fmt.Sprint(new_number)), y}
				*p = append(*p, x)
				new_number = 0
			}
		default:
			data[i] = SYMBOL
			if new_number > 0 {
				x := part_number{new_number, i - len(fmt.Sprint(new_number)), y}
				*p = append(*p, x)
				new_number = 0
			}
		}
	}
	if new_number > 0 {
		x := part_number{new_number, len(l) - len(fmt.Sprint(new_number)), y}
		*p = append(*p, x)
		new_number = 0
	}

	return data
}

func check_adjacent_to_symbol(p part_number, s [][]int) bool {
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
			if s[y][x] == SYMBOL {
				return true
			}
		}
	}
	return false
}

func main() {

	part_number_list := make([]part_number, 0, 1000)
	schematic := make([][]int, 0)
	f := bufio.NewScanner(os.Stdin)
	f.Split(bufio.ScanLines)

	y := 0
	for f.Scan() {
		l := f.Text()
		schematic = append(schematic, parse_schematic_line(l, y, &part_number_list))
		y++
	}

	part1_total := 0
	for _, p := range part_number_list {
		if check_adjacent_to_symbol(p, schematic) {
			part1_total += p.value
		}
	}

	// fmt.Println(schematic)
	// fmt.Println(part_number_list)
	fmt.Printf("Part 1: %d\n", part1_total)
	// fmt.Printf("Part 2: %d\n", part2_total)

}
