# input  [3,5,6,2,1,4,6,9]
# output [1,2,3,1,1,3,4,8]

def max_duration_timeseries(values):
    stack = []
    output = []
    for num in values:
        while stack and stack[-1] < num:
            stack.pop()
    
        if stack:
            output.append(stack[-1])
        else:
            output.append(-1)
        
        stack.append(num)

    return output
              
            
    
        
print(max_duration_timeseries([3, 5, 6, 2, 1, 4, 6, 9]))
# → [1, 2, 3, 1, 1, 1, 5, 8]