# all_favorite_colors.txt を全世界の人の好きな色を記録したファイルとする
# 一行に一つ色が書いてあり、色をカウントするプログラムを考える

# ファイル全体を呼び込む方法(メモリ効率が悪い)
# メモリ使用量: O(N)
color_counts = {}
with open('all_favorite_colors.txt') as favorite_colors_file:
    favorite_colors = favorite_colors_file.read().splitlines()
for color in favorite_colors:
    if color in color_counts:
        color_counts[color] += 1
    else:
        color_counts[color] = 1

# 一行ずつメモリに読む込む方法
# メモリ使用量: O(1)
color_counts = {}
with open('all_faborite_colors.txt') as favorite_colors_file:
    for color in favorite_colors_file: # 前のループのcolorを上書き
        color = color.strip() # 文末の改行文字を削除
        if color in color_counts:
            color_counts[color] += 1
        else:
            color_counts[color] = 1

