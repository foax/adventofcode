package main

import (
	"bufio"
	"errors"
	"fmt"
	"os"
	"regexp"
	"strings"
)

	var number_map map[string]int = {
		"one":   1,
		"two":   2,
		"three": 3,
		"four":  4,
		"five":  5,
		"six":   6,
		"seven": 7,
		"eight": 8,
		"nine":  9,
	}

	number_map_keys := make([]string, len(number_map))
	i := 0
	for k := range number_map {
		number_map_keys[i] = k
		i++
	}


func part1_handler(l string) (number int, err error) {
	calibration := [2]int{0, 0}
	for _, c := range l {
		x := int(c) - '0'
		if x >= 0 && x <= 9 {
			idx := 0
			if calibration[idx] != 0 {
				idx = 1
			}
			calibration[idx] = x
		}
	}

	if calibration[0] == 0 {
		return 0, errors.New("first number not set")
	}

	number = 10 * calibration[0]
	if calibration[1] != 0 {
		number += calibration[1]
	} else {
		number += calibration[0]
	}
	return

}

func part2_handler(l string) (number int, err error) {
	number_set := make([]bool, len(l))
	number_list := make([]int, len(l))


	re_str := "(" + strings.Join(number_map_keys, "|") + ")"
	re, err := regexp.Compile(re_str)
	if err != nil {
		return 0, err
	}

	i = 0
	for {
		n := re.FindStringIndex(l[i:])
		// fmt.Println(n)
		if n == nil {
			break
		}
		number_set[n[0]+i] = true
		number_list[n[0]+i] = number_map[l[n[0]+i:n[1]+i]]
		i += n[0] + 1
		// fmt.Println(len(l))
		// fmt.Println(i)
		if i == len(l) {
			break
		}
	}

	// number_locations := re.FindAllStringIndex(l, -1)
	// for _, n := range number_locations {
	// 	number_set[n[0]] = true
	// 	number_list[n[0]] = number_map[l[n[0]:n[1]]]
	// }

	for i, c := range l {
		x := int(c) - '0'
		if x >= 0 && x <= 9 {
			number_set[i] = true
			number_list[i] = x
		}
	}

	fmt.Printf("Input line: %s\n", l)
	// fmt.Println("numbers set:")
	// fmt.Println(number_set)
	// fmt.Println("number list:")
	fmt.Println(number_list)

	a, b := -1, -1
	for i, c := range number_set {
		if c {
			if a == -1 {
				a = i
			}
			b = i
		}
	}

	number = 10*number_list[a] + number_list[b]
	fmt.Println(number)
	return
}

func main() {

	f := bufio.NewScanner(os.Stdin)
	f.Split(bufio.ScanLines)

	part1_total := 0
	part2_total := 0

	for f.Scan() {
		l := f.Text()
		part1_number, err := part1_handler(l)
		if err != nil {
			panic(err)
		}
		part1_total += part1_number

		// part2_number, err := part2_handler(l)
		// if err != nil {
		// 	panic(err)
		// }
		// part2_total += part2_number

	}

	fmt.Printf("Part 1: %d\n", part1_total)
	fmt.Printf("Part 2: %d\n", part2_total)
}
