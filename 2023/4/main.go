package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type card map[int]bool

func parse_card_line(l string) [2]card {
	var cards [2]card

	for i, _ := range cards {
		cards[i] = make(map[int]bool)
	}

	fields := make([][]string, 0)
	fields = append(fields, strings.Split(l, ": "))
	fields = append(fields, strings.Split(fields[0][1], " | "))
	for i, c := range fields[1] {
		for _, x := range strings.Fields(c) {
			y, _ := strconv.Atoi(x)
			cards[i][y] = true
		}
	}

	return cards
}

func card_matches(cards [2]card) int {
	score := 0
	for c, _ := range cards[1] {
		if cards[0][c] {
			score++
		}
	}
	return score
}

func main() {
	f := bufio.NewScanner(os.Stdin)
	f.Split(bufio.ScanLines)
	part1_total := 0
	all_cards := make([][2]card, 0)
	for f.Scan() {
		l := f.Text()
		cards := parse_card_line(l)
		all_cards = append(all_cards, cards)
		part1_total += 2 ^ card_matches(cards)
	}

	card_copies := make([]int, len(all_cards))
	fmt.Println(card_copies)

	for i, c := range all_cards {
		score := card_matches(c)
		fmt.Println(i, c, score)
		if score > 0 {
			for x := i + 1; x <= i+score && x < len(all_cards); x++ {
				card_copies[x] += 1 + card_copies[i]
			}
		}
	}

	part2_total := 0
	for _, x := range card_copies {
		part2_total += 1 + x
	}

	fmt.Printf("Part 1: %d\n", part1_total)
	fmt.Printf("Part 2: %d\n", part2_total)

}
