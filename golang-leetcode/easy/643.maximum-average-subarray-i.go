package main
/*
 * @lc app=leetcode id=643 lang=golang
 *
 * [643] Maximum Average Subarray I
 */

// @lc code=start
func findMaxAverage(nums []int, k int) float64 {
	var wsum float64
	var lptr int
	max := math.Inf(-1)
	for rptr:=0; rptr < len(nums); rptr++ {
		wsum += float64(nums[rptr])
		if (rptr - lptr + 1 == k) {
			max = math.Max(max, wsum/float64(k))
			wsum -= float64(nums[lptr])
			lptr += 1
		}
	}
	return max
}

// @lc code=end
func findMaxAverage(nums []int, k int) float64 {
	max := math.Inf(-1)
	for i := 0; i < len(nums); i++ {
		sum := 0
		for j := 0; j < k; j++ {
			if !(i+k-1 > len(nums)-1) {
				sum += nums[i+j]
			} else {
				i = len(nums)
				j = k
			}
		}
		if sum != 0 { 
			max = math.Max(max, float64(sum)/float64(k))
		}
	}
	if max == math.Inf(-1) {
		return 0
	}
	return max
