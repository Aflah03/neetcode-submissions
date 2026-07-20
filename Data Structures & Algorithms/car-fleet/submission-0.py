class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = []
        for i in range(len(position)):
            arr.append((position[i], (target-position[i]) / speed[i]));
        arr.sort()
        print(arr)

        st  = []
        fleet = 0
        for i in range(len(arr)-1,-1,-1):
            if len(st) == 0:
                st.append(arr[i][1])
                fleet = 1
            if arr[i][1] <= st[-1]:
                continue
            elif arr[i][1] > st[-1]:
                st.append(arr[i][1])
                fleet+=1
        return fleet
