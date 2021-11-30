# import re
# s1="avodha"
# if re.match(s1,"avodha... hai gd mng"):
#     print("matched")
# else:
#  print("not matched")

# import re
# s2="avodha"
# if re.search(s2,"hello avodha how r u?"):
#     print("matched")
# else:
#     print("not matched")

# import re
# s3="avodha"
# print(re.findall(s3,"avodhahai hello.. how are u avodha gd mng avodha"))

# FIND AND REPLACE

import re
str="hai avodha,how r u?"
pattern=r"avodha"
new1=re.sub(pattern,"AVODHA_NEW",str)
print("new1")

# import re
# pattern=r"avodha"
# if re.match(pattern,"avodha"):
#     print("matched")
# else:
#     print("not matched")

# import re
# pattern=r"[0-9][a-z][A-Z]"
# if re.search(pattern,"3aV"):
#     print("correct")
# else:
#     print("not correct")