package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

const (
	HIGH_CARD = iota
	PAIR
	TWO_PAIR
	THREE_OF_A_KIND
	FULL_HOUSE
	FOUR_OF_A_KIND
	FIVE_OF_A_KIND
)

type card rune

type camelHand struct {
	cards string
	bid   int
}

type camelHands []camelHand

type cardCount struct {
	c     card
	count int
}

type cardCounts []cardCount

var cardRank = map[card]int{
	'J': 0,
	'2': 1,
	'3': 2,
	'4': 3,
	'5': 4,
	'6': 5,
	'7': 6,
	'8': 7,
	'9': 8,
	'T': 9,
	'Q': 10,
	'K': 11,
	'A': 12,
}

func (c cardCounts) Len() int           { return len(c) }
func (c cardCounts) Swap(i, j int)      { c[i], c[j] = c[j], c[i] }
func (c cardCounts) Less(i, j int) bool { return c[i].count < c[j].count }

func (c camelHands) Len() int      { return len(c) }
func (c camelHands) Swap(i, j int) { c[i], c[j] = c[j], c[i] }
func (c camelHands) Less(i, j int) bool {
	if c[i].handType() == c[j].handType() {
		for a, x := range c[i].cards {
			y := c[j].cards[a]
			if cardRank[card(x)] == cardRank[card(y)] {
				continue
			}
			return cardRank[card(x)] < cardRank[card(y)]
		}
	}
	return c[i].handType() < c[j].handType()
}

func (c camelHand) getCardCount() (cc cardCounts) {
	ccm := make(map[card]int)
	for _, c := range c.cards {
		ccm[card(c)] += 1
	}
	for c, count := range ccm {
		cc = append(cc, cardCount{c, count})
	}
	sort.Sort(sort.Reverse(cc))
	return
}

func (c camelHand) handType() int {
	cc := c.getCardCount()
	i := 0
	if cc[i].c == 'J' {
		if cc[i].count == 5 {
			return FIVE_OF_A_KIND
		}
		i++
	}

	jokers := 0
	for _, c := range cc {
		if c.c == 'J' {
			jokers = c.count
			break
		}
	}

	switch cc[i].count + jokers {
	case 5:
		return FIVE_OF_A_KIND
	case 4:
		return FOUR_OF_A_KIND
	case 3:
		if cc[1].count == 2 {
			return FULL_HOUSE
		} else {
			return THREE_OF_A_KIND
		}
	case 2:
		if cc[1].count == 2 {
			return TWO_PAIR
		} else {
			return PAIR
		}
	default:
		return HIGH_CARD
	}
}

func main() {
	f := bufio.NewScanner(os.Stdin)
	f.Split(bufio.ScanLines)

	game := make(camelHands, 0)

	for f.Scan() {
		l := f.Text()
		fields := strings.Fields(l)
		bid, _ := strconv.Atoi(fields[1])
		c := camelHand{fields[0], bid}
		game = append(game, c)
	}

	fmt.Println(game)
	sort.Sort(game)
	fmt.Println(game)

	winnings := 0
	for i, c := range game {
		fmt.Printf("Rank: %d; Hand: %v; Hand type: %d; Bid: %d\n", i+1, c.cards, c.handType(), c.bid)
		winnings += (i + 1) * c.bid
	}

	fmt.Println(winnings)
}
