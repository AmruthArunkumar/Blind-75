class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "," + s
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        ind = 0
        while ind < len(s):
            size = ""
            while s[ind] != ",":
                size += s[ind]
                ind += 1
            size = int(size)
            ind += 1;
            decoded.append(s[ind : ind+size])
            ind += size
        return decoded