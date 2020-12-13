#### CAFE: gene family evolution

- hamstr输出结果格式为
```
EOG805VVD|SINV|Waur|XP_011702617.1|0|MENTDGSRRKLSF
```
EOG805VVD（基因名称）SINV（参考基因组名称）Waur（物种名）XP_011702617.1（基因组文件中基因ID）MENTDGSRRKLSF （序列信息）

```
cat hym_48_COGs.fas | awk -F "|" '{print$1" "$3}' > cafe.fas
cat hym_288_COGs.fas | awk -F "|" '{print$1" "$3}' > cafe.fas
cat spider5_COGs.fas | awk -F "|" '{print$1" "$3}' > cafe.fas
cat spider71_COGs.fas | awk -F "|" '{print$1" "$3}' > cafe.fas
cat yu30_COGs.fas | awk -F "|" '{print$1" "$3}' > cafe.fas
cat yu33_COGs.fas | awk -F "|" '{print$1" "$3}' > cafe.fas
```

- 提取第一格和第三格的信息
```
sort -u cafe.fas > cafe.fas.u
```

- 把以上提取的结果进行排序

```
sed -i 's/ /:/g' cafe.fas.u
```

- 把提取文件中的空格替换成“：”
```
python multiple.py
```

- 运行multiple.py
output file: result.csv


- 编辑出一格物种的文件，species.txt
- 格式如下：(物种名4digit后加:NONE)

Acep:NONE
Amel:NONE
```
sort -u species.txt > species.txt.u
```
- 对species.txt文件进行排序
```
sed -i 's/,/:/g' cafe.fas.u
sed -i 's/,/:/g' result.csv
```
- 对分析结果进行格式校正
```
python dic.py result.csv hamstr_count.csv
```
input: result.csv
output: hamstr_count.csv
