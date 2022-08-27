class Solution:
	def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
		def find(nums: List[int]):
			prefixsums_encountered = [0]
			n = 1
			res = -inf
			for prefixsum in accumulate(nums):
				prev_sum = prefixsum - k
				pos = bisect_left(prefixsums_encountered, prev_sum)
				if pos < n:
					res = max(res, prefixsum - prefixsums_encountered[pos])
					if res == k:
						return k
				insort(prefixsums_encountered, prefixsum)
				n += 1
			return res

		height, width = len(matrix), len(matrix[0])
		res = -inf
		for rownum in range(height):
			totals = [0] * width
			for bottom_row in range(rownum, height):
				for colnum in range(width):
					totals[colnum] += matrix[bottom_row][colnum]

				res = max(res, find(totals))
				if res == k:
					return k
		return res