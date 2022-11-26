package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type sub struct {
	pos   int
	depth int
}

type improved_sub struct {
	sub
	aim int
}

func (s sub) String() string {
	return fmt.Sprintf("Pos: %d Depth %d", s.pos, s.depth)
}

func (s improved_sub) String() string {
	return fmt.Sprintf("Pos: %d Depth: %d Aim: %d", s.pos, s.depth, s.aim)
}

func main() {
	var s sub
	var s2 improved_sub
	fileScanner := bufio.NewScanner(os.Stdin)
	fileScanner.Split(bufio.ScanLines)

	for fileScanner.Scan() {
		command := strings.Split(fileScanner.Text(), " ")
		x, err := strconv.Atoi(command[1])
		if err != nil {
			panic(err)
		}

		switch command[0] {
		case "forward":
			s.pos += x
			s2.pos += x
			s2.depth += s2.aim * x
		case "down":
			s.depth += x
			s2.aim += x
		case "up":
			s.depth -= x
			s2.aim -= x
		}
		fmt.Printf("Sub 2 %v\n", s2)
	}

	fmt.Printf("Sub %v\n", s)
	fmt.Println("Part 1:", s.pos*s.depth)
	fmt.Println("Part 2:", s2.pos*s2.depth)

}
