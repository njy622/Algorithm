class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        list = [[1]]
        # 두 번째 행부터 numRows까지 반복
        for i in range(1, numRows):
            # 모든 행의 첫 번째 원소는 항상 1로 고정
            row = [1]
            # 이전 행을 참조
            pre_row = list[i - 1]
            # 현재 행의 중간 값들을 계산
            for j in range(1, i):
                row.append(pre_row[j - 1] + pre_row[j])
            # 현재 행의 마지막 원소는 항상 1
            row.append(1)
            # 현재 행을 삼각형에 추가
            list.append(row)

        return list

