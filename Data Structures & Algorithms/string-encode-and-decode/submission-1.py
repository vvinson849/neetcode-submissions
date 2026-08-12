class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0: return ""
        out = ""
        for s in strs:
            out += str(len(s))
            out += '#'
            out += s
        return out

    def decode(self, s: str) -> List[str]:
        if len(s) == 0: return []
        out = []
        while len(s) > 0:
            s_split = s.split('#', 1)
            readlen = int(s_split[0])
            out.append(s_split[1][:readlen])
            s = s_split[1][readlen:]
        return out

