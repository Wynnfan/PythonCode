import re

phoneNumRegx = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mobile = phoneNumRegx.findall('My number is 244-425-2824, My number is 351-515-1561')
print(mobile)
