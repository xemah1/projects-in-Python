height = [1,8,6,3,2,5,4,2,5,4,8,3,7,8,3,7]

def maxArea(height) -> int:
    left = 0 
    right = len(height)-1
    max_h = 0 
    
    while left<right:
        h = min(height[right] , height[left])
        area = (right-left)*h
        if area >max_h:
            max_h = area
        
        if height[left]<height[right]:
            left+=1
        else:
            right-=1
        
    
    return max_h