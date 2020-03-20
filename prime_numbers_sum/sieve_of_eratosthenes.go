package main

import "fmt"

func getPrimeNums(n int) int {
	isNotPrime := make([]bool, n+1)
	res := 0

	for i := 2; i * i <=n; i++ {
		if isNotPrime[i] == false {
			for j := i * i; j <= n; j +=i {
				isNotPrime[j] = true
			}
		}
	}

	for i := 2; i <= n; i ++ {
		if isNotPrime[i] == false {
			res += i
		}
	}
	return res
}

func main(){
	fmt.Printf("Sum of prime numbers till %d is: %d ", 11, getPrimeNums(11))
}