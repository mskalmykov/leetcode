class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = []
        for s in path.split('/'):
            if s == '' or s == '.':
                continue
            elif s == '..':
                if len(dirs) > 0:
                    dirs.pop()
            else:
                dirs.append(s)

        return '/' + '/'.join(dirs)

print(Solution().simplifyPath("/home/"))
print(Solution().simplifyPath("/home//foo/"))
print(Solution().simplifyPath("/home/user/Documents/../Pictures"))
print(Solution().simplifyPath("/../"))
print(Solution().simplifyPath("/.../a/../b/c/../d/./"))