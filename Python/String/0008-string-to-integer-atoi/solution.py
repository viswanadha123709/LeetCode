class Solution:
    def myAtoi(self, s: str) -> int:
        def check(s):
            s = s.strip()
            sign_used = False
            digit_started = False

            for ch in s:
                if not digit_started and not sign_used and ch in "+-":
                    sign_used = True
                    digit_started = True
                    yield ch
                elif ch.isdigit():
                    digit_started = True
                    yield ch
                else:
                    break

        ans = ""

        for ch in check(s):
            ans += ch

        if ans == "" or ans == "+" or ans == "-":
            return 0

        num = int(ans)

        if num < -2**31:
            return -2**31
        if num > 2**31 - 1:
            return 2**31 - 1

        return num