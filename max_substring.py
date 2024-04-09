def lengthOfLongestSubstring(s) -> int:
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        maxLength = 0
        charSet = set()
        left = 0
        
        for right in range(n):
            print('sright',s[right])
            print('charset',charSet)
            if s[right] not in charSet:
                charSet.add(s[right])
                maxLength = max(maxLength, right - left + 1)
            else:
                while s[right] in charSet:
                    charSet.remove(s[left])
                    left += 1
                charSet.add(s[right])
        
        return maxLength

# print(lengthOfLongestSubstring("abcabcbb"))

print(lengthOfLongestSubstring("pwwkew"))