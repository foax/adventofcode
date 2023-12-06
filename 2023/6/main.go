package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func raceDistance(raceTime, triggerTime int) int {
	return (raceTime - triggerTime) * triggerTime
}

func waysToWin(raceTime, distanceRecord int) int {
	wins := 0
	for i := 1; i < raceTime; i++ {
		d := raceDistance(raceTime, i)
		if d > distanceRecord {
			wins++
		}
	}
	return wins
}

func main() {
	part1Data := make(map[string][]int)
	part2Data := make(map[string]int)

	f := bufio.NewScanner(os.Stdin)
	f.Split(bufio.ScanLines)

	for f.Scan() {
		l := f.Text()
		fields := strings.Split(l, ":")
		for _, s := range strings.Fields(fields[1]) {
			v, _ := strconv.Atoi(s)
			part1Data[fields[0]] = append(part1Data[fields[0]], v)
		}
		v, _ := strconv.Atoi(strings.Join(strings.Fields(fields[1]), ""))
		part2Data[fields[0]] = v
	}

	part1Total := -1
	for i, raceTime := range part1Data["Time"] {
		distanceRecord := part1Data["Distance"][i]
		wins := waysToWin(raceTime, distanceRecord)
		fmt.Printf("Race time: %d; Distance: %d; Ways to win: %d\n", raceTime, distanceRecord, wins)
		if part1Total == -1 {
			part1Total = wins
		} else {
			part1Total *= wins
		}
	}

	part2Total := waysToWin(part2Data["Time"], part2Data["Distance"])
	fmt.Printf("Part 1: %d; Part 2: %d\n", part1Total, part2Total)
}
