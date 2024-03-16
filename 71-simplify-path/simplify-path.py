class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for name in path.split("/"):
            # print(name)
            if stack and name == "..":
                stack.pop()
            elif name not in [".", "", ".."]:
                stack.append(name)
        return "/"+"/".join(stack)
