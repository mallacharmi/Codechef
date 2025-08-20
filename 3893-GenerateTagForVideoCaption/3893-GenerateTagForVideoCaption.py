# Last updated: 8/20/2025, 5:41:29 PM
class Solution:
    def generateTag(self, caption: str) -> str:
        # Step 1: Split the caption into words
        words = caption.split()
        
        # Step 2: Convert to camelCase
        if not words:
            return "#"
        camel_case = words[0].lower()
        for word in words[1:]:
            camel_case += word.capitalize()
        
        # Step 3: Remove all non-English letters (except the first '#')
        cleaned = ''.join(c for c in camel_case if c.isalpha())
        
        # Step 4: Add '#' at the beginning
        result = '#' + cleaned
        
        # Step 5: Truncate to 100 characters
        return result[:100]