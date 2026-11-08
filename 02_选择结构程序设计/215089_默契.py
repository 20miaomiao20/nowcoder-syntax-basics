# NC215089 默契：相等时输出 Tacit！——这里的感叹号是「全角」！(U+FF01)
# 不相等时是半角 ! (U+0021)，两个符号肉眼几乎看不出区别，抄错就 WA
x, y = map(int, input().split())
if x == y:
    print("Tacit\uff01")
else:
    print("No Tacit!")
