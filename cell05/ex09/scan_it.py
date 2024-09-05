#!/usr/bin/env python3

import sys
import re

if len(sys.argv) != 3:
    print("\033[38;5;219m" + "none")
else:
    keyword = sys.argv[1]
    text = sys.argv[2]
    
    matches = re.findall(re.escape(keyword), text)
    
    if matches:
        print(len(matches))
    else:
        print("\033[38;5;219m" + "none")



# keyword = "example.*com"

# text = "Visit example.*com for more information. example.*com is great."

# matches_without_escape = re.findall(keyword, text)
# print("Without re.escape():", matches_without_escape)

# escaped_keyword = re.escape(keyword)
# matches_with_escape = re.findall(escaped_keyword, text)
# print("With re.escape():", matches_with_escape)

