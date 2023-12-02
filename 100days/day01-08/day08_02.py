from time import sleep

class Clock():
    def __init__(self, h=0, m=0, s=0):    
        self.h = h
        self.m = m
        self.s = s
    
    def run(self):
        self.s += 1
        if self.s == 60:
            self.s = 0
            self.m += 1
        if self.m == 60:
            self.m = 0
            self.h += 1
        if self.h == 24:
            self.h = 0
    
    def show(self):
        print(f"{self.h:02d}:{self.m:02d}:{self.s:02d}")

def main():
    c1 = Clock(23, 59, 55)
    while 1:
        c1.run()
        c1.show()
        sleep(1)

if __name__ == "__main__":
    main()