package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type draw map[string]int

type game struct {
	id    int
	draws []draw
}

func parse_game_line(l string) *game {
	g := game{}

	fields := strings.Split(l, ": ")
	gameid_fields := strings.Fields(fields[0])
	i, _ := strconv.Atoi(gameid_fields[1])
	g.id = i

	draws_fields := strings.Split(fields[1], "; ")
	for _, draw_str := range draws_fields {
		d := draw{}
		cube_strs := strings.Split(draw_str, ", ")
		for _, cube_str := range cube_strs {
			cube_fields := strings.Fields(cube_str)
			i, _ := strconv.Atoi(cube_fields[0])
			d[cube_fields[1]] = i
		}
		g.draws = append(g.draws, d)
	}
	return &g
}

func part1_check_game(g *game, red int, green int, blue int) bool {
	for _, d := range g.draws {
		if d["red"] > red || d["green"] > green || d["blue"] > blue {
			return false
		}
	}
	return true
}

func part2_check_power(g *game) int {
	var red, green, blue int
	for _, d := range g.draws {
		if d["red"] > red {
			red = d["red"]
		}
		if d["green"] > green {
			green = d["green"]
		}
		if d["blue"] > blue {
			blue = d["blue"]
		}
	}
	return red * green * blue
}

func main() {
	f := bufio.NewScanner(os.Stdin)
	f.Split(bufio.ScanLines)
	part1_total := 0
	part2_total := 0
	for f.Scan() {
		l := f.Text()
		g := parse_game_line(l)
		if part1_check_game(g, 12, 13, 14) {
			part1_total += g.id
		}
		part2_total += part2_check_power(g)
	}
	fmt.Printf("Part 1: %d\n", part1_total)
	fmt.Printf("Part 2: %d\n", part2_total)

}
