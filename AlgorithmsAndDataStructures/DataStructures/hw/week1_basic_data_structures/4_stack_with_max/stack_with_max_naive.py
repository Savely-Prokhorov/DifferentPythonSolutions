#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__max1 = None
        self.__max2 = None
        self.__stack = []
		
    def Push(self, a):
        self.__stack.append(a)
        if self.__max1 == None:
            self.__max1 = a
        else:
            if a >= self.__max1:
                self.__max2 = self.__max1
                self.__max1 = a     

    def Pop(self):
        assert(len(self.__stack))
        if self.__stack.pop() == self.__max1:
            if self.__max2 != None:
                self.__max1 = self.__max2
                self.__max2 = None
            else:
                self.__max1 = max(self.__stack)
                #temp = self.__stack.pop()
                #self.__max_2 = max(self.__stack)
                #self.Push(temp)

    def Max(self):
        assert(len(self.__stack))
        return self.__max1


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
