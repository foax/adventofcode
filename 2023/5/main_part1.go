package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

type almanacRange struct {
	src  int
	dest int
	step int
}

type almanacRanges []almanacRange

type almanacMap struct {
	key    string
	value  string
	ranges almanacRanges
}

func (a almanacRanges) Len() int           { return len(a) }
func (a almanacRanges) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }
func (a almanacRanges) Less(i, j int) bool { return a[i].src < a[j].src }

func mapSeed(t string, v int, am map[string]*almanacMap) (string, int) {
	a := am[t]
	fmt.Printf("%s to %s - Value: %v; Ranges: %v\n", t, a.value, v, a.ranges)
	// Loop:
	for _, r := range a.ranges {
		fmt.Printf("src: %d; dst: %d; step: %d\n", r.src, r.dest, r.step)
		if v >= r.src && v < r.src+r.step {
			fmt.Printf("%s number %v maps to %s number %v\n", t, v, a.value, r.dest+v-r.src)
			return a.value, r.dest + v - r.src
		}
	}
	fmt.Printf("%s number %v maps to %s number %v (didn't match)\n", t, v, a.value, v)
	return a.value, v
}

func main() {
	var seeds []int
	almanacMaps := make(map[string]*almanacMap)
	var a *almanacMap

	f := bufio.NewScanner(os.Stdin)
	f.Split(bufio.ScanLines)

	for f.Scan() {
		l := f.Text()
		switch {
		case seeds == nil:
			seedsFields := strings.Split(l, ": ")
			for _, s := range strings.Fields(seedsFields[1]) {
				seedValue, _ := strconv.Atoi(s)
				seeds = append(seeds, seedValue)
			}
		case strings.Contains(l, "map:"):
			mapFields := strings.Fields(l)
			a = &almanacMap{
				key:   strings.Split(mapFields[0], "-")[0],
				value: strings.Split(mapFields[0], "-")[2],
			}
		case l == "":
			if a != nil {
				almanacMaps[a.key] = a
			}
		default:
			fields := strings.Fields(l)
			srcValue, _ := strconv.Atoi(fields[1])
			destValue, _ := strconv.Atoi(fields[0])
			stepValue, _ := strconv.Atoi(fields[2])
			r := almanacRange{srcValue, destValue, stepValue}
			a.ranges = append(a.ranges, r)
		}
	}
	almanacMaps[a.key] = a

	for k, a := range almanacMaps {
		sort.Sort(a.ranges)
		fmt.Println(k, *a)
	}

	fmt.Println()

	for i, _ := range seeds {
		for seedType := "seed"; seedType != "location"; {
			var newSeed int
			seedType, newSeed = mapSeed(seedType, seeds[i], almanacMaps)
			seeds[i] = newSeed
		}
	}

	min := seeds[0]
	for i := 1; i < len(seeds); i++ {
		if seeds[i] < min {
			min = seeds[i]
		}
	}

	fmt.Println(almanacMaps)
	fmt.Println(min)

}
