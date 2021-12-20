s1="bctsjaft"
s2="owkhsynl"
merge_string=""
for i in s1:
    merge_string+=i
for i in s2:
    merge_string+=i
merge_string=sorted(merge_string)
final_ans=""
for i in merge_string:
    final_ans+=i
print("final string after merging 2 sorted arrays==",final_ans)
