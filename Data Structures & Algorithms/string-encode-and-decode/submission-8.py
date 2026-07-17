class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ''.join(f"{len(s)}#{s}" for s in strs)
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            j = s.find('#', i)
            length = int(s[i:j])
            i = j + 1
            decoded.append(s[i:i + length])
            i += length
        return decoded

        