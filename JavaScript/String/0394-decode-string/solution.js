                while stack and stack[-1] != '[':
                    sb.append(stack.pop())

                stack.pop()

                num = []
                while stack and stack[-1].isdigit():
                    num.append(stack.pop())

                count = int(''.join(num[::-1]))

                for j in range(count):
                    for k in sb[::-1]:
                        stack.append(k)

        return ''.join(stack)
