#!/usr/local/bin/python3

TWITTER = open("TwiTokens.txt", "r").read().splitlines()

print(TWITTER[0])
print(TWITTER[1])
print(TWITTER[2])
print(TWITTER[3])

# api.update_status(status='Hello. Is it me you\'re looking for?')

# result = getUserInfobyName("chenb0x")

"""
for key, value in result.items():
    try:
        print(value)
    except:
        pass
"""
# print(result['name'])
# print(str(result['status']['text']).encode('utf-8', 'ignore'))
# print(str(result).encode('utf-8', 'ignore'))
