package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {

	var previous, increased, window_increased int
	var window [3]int
	started := false
	fileScanner := bufio.NewScanner(os.Stdin)
	fileScanner.Split(bufio.ScanLines)

	for idx := 0; fileScanner.Scan(); idx++ {
		depth, err := strconv.Atoi(fileScanner.Text())
		if err != nil {
			panic(err)
		}

		if started && depth > previous {
			increased++
		}
		previous = depth
		started = true

		if idx > 2 {
			if depth > window[0] {
				window_increased++
			}
		}

		window[0] = window[1]
		window[1] = window[2]
		window[2] = depth

	}

	fmt.Printf("Part 1 - number of increases: %d\n", increased)
	fmt.Printf("Part 2 - number of increases: %d\n", window_increased)

}
