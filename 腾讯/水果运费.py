"""
解题思路：
"""
  import sys
  if __name__ == "__main__":
     # 读取第一行的n
     n = int(sys.stdin.readline().strip())
     line = sys.stdin.readline().strip()
     values = list(map(int, line.split()))
     i = 0
     sum_ = 0
     while i < n-1:
         values[i+1] += values[i]
         sum_ += abs(values[i])
         i+=1
     print(sum_)
