class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        # 0 ~ n 까지의 숫자를 반복하여,
        for i in range(n+1):
        # bin()인 이진수 함수에 넣어 이진수로 변환한 뒤, 해당 이진수에 포함된 '1'을 카운트하여 배열에 넣음
            result.append(bin(i).count('1'))
        return result