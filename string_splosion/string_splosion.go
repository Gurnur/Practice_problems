/***
Given a non-empty string like "Code" return a string like "CCoCodCode".

stringSplosion("Code") → "CCoCodCode"
stringSplosion("abc") → "aababc"
stringSplosion("ab") → "aab"
*/
package main

import "fmt"

func stringSplosion(str string) string {
	i := 1
	var result []byte
	for a := 0; a < len(str); a++ {
		for j := 0; j < i; j++ {
			result = append(result, str[j])
		}
		i++
	}
	return string(result)
}

func main() {
	var str = "Code"
	result := stringSplosion(str)
	fmt.Println(result)
}
