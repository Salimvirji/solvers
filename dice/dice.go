package main

import (
        "flag"
        "fmt"
        "math/rand"
        "sync"
        "time"
)

// use this to ensure we only generate the random seed once
var onlyOnce sync.Once

// prepare the dice
var dice = []int{1, 2, 3, 4, 5, 6}

func rollDice() int {

        // only generate the randomness once
        onlyOnce.Do(func() {
                rand.Seed(time.Now().UnixNano())
        })

        return dice[rand.Intn(len(dice))]
}

func main() {
        numRolls := flag.Int("rolls", 5, "number of times to roll")
        numSides := flag.Int("sides", 6, "number of sides on each die")
        flag.Parse()

        // prepare the dice
        switch *numSides {
                case 4:
                        dice = []int{1, 2, 3, 4}
                case 6:
                        dice = []int{1, 2, 3, 4, 5, 6}
                case 10:
                        dice = []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
                case 12:
                        dice = []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
                default:
                        dice = []int{1, 2, 3, 4, 5, 6}
        }
        
        for i := 1; i <= *numRolls; i++ {
                diceroll := rollDice() 
                fmt.Printf("Die %3d: %2d\n", i, diceroll)
        }
}
