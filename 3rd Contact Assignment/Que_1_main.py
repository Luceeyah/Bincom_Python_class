series = [0,1] 
counter = 0

fibonoci_len = eval(input("Enter the range for fibonuci series: "))

while counter < fibonoci_len:
        ans = series[-1] + series[-2]
        series.append(ans)
        counter += 1
        
print(series)



