from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        """Encode a list of strings into a single string."""
        encoded = []
        for s in strs:
            # Prefix each string with its length followed by a delimiter
            encoded.append(f"{len(s)}#{s}")
        return "".join(encoded)
    
    def decode(self, s: str) -> List[str]:
        """Decode a string back into a list of strings."""
        decoded = []
        i = 0
        
        while i < len(s):
            # Find the delimiter position
            j = i
            while s[j] != '#':
                j += 1
            
            # Extract the length
            length = int(s[i:j])
            
            # Extract the string
            string_start = j + 1
            string_end = string_start + length
            decoded.append(s[string_start:string_end])
            
            # Move to the next string
            i = string_end
        
        return decoded