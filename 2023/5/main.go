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
	start int
	end   int
	delta int
}

type almanacRanges []almanacRange

type almanacMap struct {
	key    string
	value  string
	ranges almanacRanges
}

type seedValues struct {
	start int
	end   int
}

func (a almanacRanges) Len() int           { return len(a) }
func (a almanacRanges) Swap(i, j int)      { a[i], a[j] = a[j], a[i] }
func (a almanacRanges) Less(i, j int) bool { return a[i].start < a[j].start }

func mapSeeds(t string, s []seedValues, am map[string]*almanacMap) (string, []seedValues) {
	a := am[t]
	newSeedValues := make([]seedValues, 0)
	for _, sv := range s {
		newSeedValues = append(newSeedValues, mapSeedRange(sv, a.ranges)...)
	}
	return a.value, newSeedValues
}

func mapValue(src int, r almanacRange) int {
	if src < r.start || src >= r.end {
		return src
	}
	return src + r.delta
}

func mapSeedRange(sv seedValues, ar almanacRanges) (newSeedValues []seedValues) {
	// fmt.Printf("Map seed values %v to ranges %v\n", sv, ar)
	for _, r := range ar {
		// fmt.Printf("Range: %#v\n", r)
		switch {
		case sv.start == sv.end:
			return
		case sv.end <= r.start:
			newSeedValues = append(newSeedValues, sv)
			return
		case sv.start >= r.end:
			continue
		default:
			if sv.start < r.start {
				newSeedValues = append(newSeedValues, seedValues{start: sv.start, end: r.start})
			}

			newSeed := seedValues{}
			if sv.start > r.start {
				newSeed.start = mapValue(sv.start, r)

			} else {
				newSeed.start = mapValue(r.start, r)
			}

			if sv.end < r.end {
				newSeed.end = mapValue(sv.end, r)
				sv.start = sv.end

			} else {
				newSeed.end = mapValue(r.end-1, r) + 1
				sv.start = r.end
			}

			newSeedValues = append(newSeedValues, newSeed)
		}
	}
	if sv.start != sv.end {
		newSeedValues = append(newSeedValues, sv)
	}
	return
}

func main() {
	var seeds []seedValues
	almanacMaps := make(map[string]*almanacMap)
	var a *almanacMap

	f := bufio.NewScanner(os.Stdin)
	f.Split(bufio.ScanLines)

	for f.Scan() {
		l := f.Text()
		switch {
		case seeds == nil:
			seedsFields := strings.Fields(strings.TrimLeft(l, "seeds: "))
			for i := 0; i < len(seedsFields)-1; i += 2 {

				seedValue, _ := strconv.Atoi(seedsFields[i])
				stepValue, _ := strconv.Atoi(seedsFields[i+1])
				seeds = append(seeds, seedValues{seedValue, seedValue + stepValue})
			}
			// fmt.Println(seeds)
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
			r := almanacRange{srcValue, srcValue + stepValue, destValue - srcValue}
			a.ranges = append(a.ranges, r)
		}
	}
	almanacMaps[a.key] = a

	for _, a := range almanacMaps {
		sort.Sort(a.ranges)
		// fmt.Println(k, *a)
	}

	fmt.Println()

	for seedType := "seed"; seedType != "location"; {
		seedType, seeds = mapSeeds(seedType, seeds, almanacMaps)
		// fmt.Println(seedType, seeds)
	}

	min := seeds[0].start
	for i := 1; i < len(seeds); i++ {
		if seeds[i].start < min {
			min = seeds[i].start
		}
	}

	// fmt.Println(almanacMaps)
	fmt.Println(min)

}
