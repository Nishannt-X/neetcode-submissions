class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        water=0

        leftm=0
        rightm=0

        while left<=right:
            if leftm<=rightm:
                if leftm<=height[left]:
                    leftm=height[left]
                else:
                    water+=leftm-height[left]
                left+=1
            else:
                if rightm<=height[right]:
                    rightm=height[right]
                else:
                    water+=rightm-height[right]
                right-=1
        return water






        