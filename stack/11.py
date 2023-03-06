res = []
stack = []
while True:
    command, *args = input().split()
    if command == "size":
        res.append(len(stack))
    elif command == "back":
      if len(stack) == 0:
        res.append('error')
      else:  
        res.append(stack[-1])
    elif command == "pop":
      if len(stack) == 0:
        res.append('error')
      else:  
        res.append(stack.pop())
    elif command == "clear":
        stack.clear()
        res.append("ok")
    elif command == "push":
        stack.append(int(args[0]))
        res.append("ok")
    elif command == "exit":
        res.append("bye")
        break
print(*res,sep='\n')
