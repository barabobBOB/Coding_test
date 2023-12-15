class Solution:
    def convert(self, s: str, numRows: int) -> str:
      strList = [[''] for _ in range(numRows)]
      cut = 0
      idx = 0
      answer = ''
      while idx < len(s):
          if cut < numRows:
            for i in strList:
              if idx < len(s):
                i.append(s[idx])
                idx += 1
                cut += 1
              else:
                break
          else:
            cut = 0
            for i in range(numRows - 2, 0, -1):
              if idx < len(s):
                strList[i].append(s[idx])
                idx += 1
              else:
                break
      for i in strList:
        for j in i:
          if j=='':
            continue
          else:
            answer += j

      return answer