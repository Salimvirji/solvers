package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	strSantas := [...]string{"person1, "person2", "personN"}
	var k int
	fmt.Println(len(strSantas))
	l := len(strSantas) - 1
	
	rand.Seed(time.Now().UnixNano())
 	rand.Shuffle(len(strSantas), func(i, j int) { strSantas[i], strSantas[j] = strSantas[j], strSantas[i] })

	for j := 0; j <= l; j++ {
		if j == l {
			k = 0
		} else {
			k = j + 1
		}
	fmt.Printf("Ho! Ho! Ho! %s, you will be making %s especially merry this year by putting a special gift in their stocking. \n", strSantas[j], strSantas[k])
	}
} //main
