package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strings"
)

func main() {

	f := bufio.NewScanner(os.Stdin)
	f.Split(bufio.ScanLines)
	var directions []rune
	var dirmap = map[rune]int{
		'L': 0,
		'R': 1,
	}

	network := make(map[string][]string)
	nodes := make([]string, 0)

	for f.Scan() {
		l := f.Text()
		if len(directions) == 0 {
			directions = []rune(l)
			continue
		}
		if l == "" {
			continue
		}
		fields := strings.Split(l, " = ")
		network[fields[0]] = strings.Split(strings.Trim(fields[1], "()"), ", ")
		if strings.HasSuffix(fields[0], "A") {
			nodes = append(nodes, fields[0])
		}
	}

	// part 1
	node := "AAA"
	steps := 0
	for node != "ZZZ" {
		idx := dirmap[directions[steps%len(directions)]]
		// fmt.Printf("step: %d; dir index: %d; src: %v; dst: %v\n", steps, idx, node, network[node][idx])
		node = network[node][idx]
		steps++
	}
	fmt.Printf("part 1: %d\n", steps)

	// part 2
	steps = 0
	endNodeSteps := make([]int, len(nodes))

	for {
		doneCount := 0
		idx := dirmap[directions[steps%len(directions)]]
		for i, n := range nodes {
			if strings.HasSuffix(n, "Z") {
				if endNodeSteps[i] == 0 {
					endNodeSteps[i] = steps
				}
			}
			if endNodeSteps[i] > 0 {
				doneCount++
			}
			nodes[i] = network[n][idx]
		}

		if doneCount == len(nodes) {
			break
		}
		steps++
	}

	sort.Sort(sort.IntSlice(endNodeSteps))
	fmt.Println(endNodeSteps)

	part2Total := endNodeSteps[0]
	for i := 1; i < len(endNodeSteps); i++ {
		x := part2Total
		for y := 2; x%endNodeSteps[i] != 0; y++ {
			x = y * part2Total
		}
		part2Total = x
	}

	fmt.Printf("part 2: %d\n", part2Total)

}
