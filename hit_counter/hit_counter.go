/**
Design Hit Counter
Design a hit counter which counts the number of hits received in the past 60 minutes.
Each function accepts a timestamp parameter (in seconds granularity) and you may assume that calls are being made to the system in chronological order (ie, the timestamp is monotonically increasing). You may assume that the earliest timestamp starts at 1.
It is possible that several hits arrive roughly at the same time.

Example:
HitCounter counter = new HitCounter();

// hit at timestamp 1.
counter.hit(1);

// hit at timestamp 2.
counter.hit(2);

// hit at timestamp 3.
counter.hit(3);

// get hits at timestamp 4, should return 3.
counter.getHits(4);

// hit at timestamp 300.
counter.hit(300);

// get hits at timestamp 300, should return 4.
counter.getHits(300);

// get hits at timestamp 301, should return 3.
counter.getHits(301);
*/
package main

import "fmt"

type hit_counter struct{
	timestamps [3600]int
	count [3600]int
}

// increment hit count: O(1)
func (hc *hit_counter)hit(timestamp int){
	tmp := timestamp % 3600
	if hc.timestamps[tmp] != timestamp {
		hc.count[tmp] = 1
		hc.timestamps[tmp] = timestamp
	} else {
		hc.count[tmp]++
	}
}

// get count: O(n)
func (hc *hit_counter)get_count(timestamp int)int{
	var total int
	for i := range hc.timestamps {
		if timestamp - hc.timestamps[i] < 3600 {
			total += hc.count[i]
		}
	}
	return total
}

func main(){
	hc := new(hit_counter)
	hc.hit(1)
	hc.hit(30)
	hc.hit(300)
	hc.hit(4500)
	hc.hit(4501)
	count := hc.get_count(4502)
	fmt.Printf("Total hits in the past 1 hr are: %d", count)
}