
song_line = input("请输入你最喜欢的歌曲的第一行：")

length = len(song_line)
print(f"这行歌词的长度是：{length}")


start_index = int(input("请输入起始位置（从0开始）："))
end_index = int(input("请输入结束位置（不包括该位置）："))


if 0 <= start_index < end_index <= length:
    section = song_line[start_index:end_index]
    print(f"指定的歌词部分是：'{section}'")
else:
    print("输入的起始和结束位置无效，请确保它们在字符串范围内。")