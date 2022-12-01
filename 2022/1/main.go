package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

func sum(s []int) (total int) {
	for _, x := range s {
		total += x
	}
	return
}

func main() {
	calories := make([]int, 0)
	f := bufio.NewScanner(os.Stdin)
	f.Split(bufio.ScanLines)

	x := 0
	for f.Scan() {
		l := f.Text()
		if l == "" {
			calories = append(calories, x)
			x = 0
			continue
		}

		c, err := strconv.Atoi(l)
		if err != nil {
			panic(err)
		}
		x += c
	}
	if x > 0 {
		calories = append(calories, x)
	}

	sort.Ints(calories)
	fmt.Printf("Part 1: %d\n", calories[len(calories)-1])
	fmt.Printf("Part 2: %d\n", sum(calories[len(calories)-3:]))

}
