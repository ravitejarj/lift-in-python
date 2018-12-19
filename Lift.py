
import array

class ele:
    top=0
    def up(self, no):
        if ele.top>no:
            print("You can't go")
        elif ele.top<no:
            if ele.top== 0:
                for i in range(no):
                    print("Now your going to", i+1,"floor")
                print("You are in", no, "floor")
            else:
                t=no-ele.top
                for i in range(t):
                    print("Now your going to", ele.top+(i+1),"floor")
                print("You are in", no, "floor")
            ele.top=no         

        elif ele.top== no:
            print("Your in current", no,"floor")

    def down(self, no):
        if ele.top< no:
            print("You can't go")
        elif ele.top> no:
            t=ele.top-no
            for i in range(t):
                print("Now your going to", (ele.top-1)-i,"floor")
            ele.top=no 
        elif ele.top== no:
            print("Your in current", no,"floor")
                

    def curfloor(self):
        print("You are in", ele.top,"floor")

    def ret(self):
        print("Enter your choice")
        print("1 for lift go to up")
        print("2 for lift go to down")
        print("3 for lift current floor")
        choice = int(input(""))
        if choice == 1:
            no = int(input("Which floor do you want to go:"))
            obj1.up(no)
        elif choice == 2:
            no = int(input("Which floor do you want to go:"))
            obj1.down(no)
        elif choice ==3:
            obj1.curfloor()

for i in range(500):
    obj1 = ele()
    obj1.ret()




