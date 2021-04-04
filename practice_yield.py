def new_range(n):
    i = 0
    while i < n:
        # 用在函數中對呼叫方產生數值,若使用 yield 產生數值的話，函數會回傳一個產生器 (generator) 物件 (object)
        # 產生器物件，而非串列，利用產生器物件的好處是節省記憶體空間，並且提升程式執行的效率
        yield i
        i += 1

for i in new_range(10):
    print(i)
