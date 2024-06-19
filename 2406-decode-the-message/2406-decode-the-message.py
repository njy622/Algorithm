class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        dict_key = {}
        a = 97
        for k in key:
            if k != ' ' and k not in dict_key:
                dict_key[k] = chr(a)
                a += 1
        list_message = []
        for m in message:
            if m == ' ':
                list_message.append(' ')
            else:
                list_message.append(dict_key[m])
        return ''.join(list_message)
        