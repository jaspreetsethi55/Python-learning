def longestCommonPrefix(strs):
        prefixes = []
        prefix = ""
        for i in range(len(strs[0])):
            if strs[1].startswith(strs[0][:i+1]):
                prefix = strs[0][0:i+1]
                prefixes.append(prefix)
        
        if len(prefixes) > 0:
            for word in strs[2:]:
                for j in range(len(prefixes)):
                    if prefixes[j] != 0:
                        if not word.startswith(prefixes[j]):
                            prefixes[j] = 0
        return ([i for i in prefixes if i != 0])[-1]



longestCommonPrefix(['flower','flowed','flew'])
#longestCommonPrefix(["dog","racecar","car"])

