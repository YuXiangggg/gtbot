from pynput import keyboard
import pyautogui as gui
import time
import keyboard as kb 
from numpy import *
from PIL import ImageGrab
from PIL import ImageOps

def autobreak(fpos,bpos,poslst,no):

    def punch(fpos,poslst,no):
        gui.click(fpos)
        for i in poslst:
            gui.moveTo(i)
            gui.dragTo(i.x,i.y,0.18*no,button="left")
            
    def place(bpos,poslst):
        gui.click(bpos)
        for i in poslst:
            gui.click(i)
    
    while not kb.is_pressed('q'):
        place(bpos,poslst)
        punch(fpos,poslst,no)


def getpos():
    global lst
    lst = []
    
    def on_release(key):
        

        if key == keyboard._win32.KeyCode(char="c"):
            pos = gui.position()
            lst.append(pos)
        if key == keyboard._win32.KeyCode(char="q"):
            poslst = []
            for i in lst:
                poslst.append("&".join([str(i.x),str(i.y)]))
            with open("settings.txt", "w") as f:
                f.write(",".join(poslst)+"\n")
            
            return False
        

    with keyboard.Listener(on_release = on_release) as listener:
        listener.join()
        
    
        
    
def confirmpos():
    for i in lst:
        gui.moveTo(i)
        time.sleep(1)
        
        
def getinv():
    

    def on_release(key):
        
        if key == keyboard._win32.KeyCode(char="f"):
            global fist
            fist = gui.position()
        if key == keyboard._win32.KeyCode(char="b"):
            global blk
            blk = gui.position()
        if key == keyboard._win32.KeyCode(char="q"):
            with open("settings.txt", 'a') as f:
                fst = "&".join([str(fist.x),str(fist.y)])
                bk = "&".join([str(blk.x),str(blk.y)])
                f.write(",".join([fst,bk]) + "\n")
            return False
        

    with keyboard.Listener(on_release = on_release) as listener:
        listener.join()
        
    
        
def confirminv():
    gui.moveTo(fist) 
    time.sleep(1)
    gui.moveTo(blk)   
    
def image_grab(pos):
    box = (int(pos.x)-10, int(pos.y)+10,int(pos.x)+10,int(pos.y)+20)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
 
    return (a.sum())
    
def collect(pos,but):

    time.sleep(2)
    p = True
    gui.moveTo(but)
    gui.dragTo(but.x,but.y,0.3,button="left")
    time.sleep(0.5)
    gui.moveTo(but)
    gui.dragTo(but.x,but.y,8,button="left")

    while not kb.is_pressed("t"):
        
        #val = 0
        val = image_grab(pos) 
        
        if (val == 291) and (p == True):
            print("portal")

        else:
            p = True
            gui.dragTo(but.x,but.y,2,button="left")
    
def getblockspos():
    retry = "1"
    while retry == "1":
        print("Hover your cursor over the blocks that you want to break and click 'c' on your keyboard to add")
        print("When you are done, press 'q' to confirm the spaces")
        getpos()
        print("Now your cursor will move to the squares you selected, if you mess up you can try again")
        confirmpos()
        retry=input("Enter 1 to retry, 0 to continue: ")
        if retry != "1":
            break
def getbuttonspos():
    retry2 = "1"
    while retry2 == "1":
        print("Hover your cursor over the first 2 inv spaces click 'f' on your keyboard to select fist, 'b' to select block")
        print("When you are done, press 'q' to confirm")
        getinv()
        print("Now your cursor will move to the squares you selected, if you mess up you can try again")
        confirminv()
        retry2=input("Enter 1 to retry, 0 to continue")
        if retry2 != "1":
            break
        
def getnopunch():
    global no 
    no = int(input("Enter number of punches: "))
    with open("settings.txt", "a") as f:
        f.write(str(no))
    
def main():
    print("Welcome to this thing that fishburrito made before bicul eoy\n")
    # print("This thing is illegal, you will be a bad growtopian if u use this\n")
    # yn = input("Do you want to be a bad Growtopian? yes/no \n")
    # if yn.lower() != "yes":
    #     print("Goodjob, bye!")
    #     time.sleep(1)
    #     exit()
    print("Okay bad growtopian what do you want to do?")
    print("1. Autobreak")
    print("2. Fishing (WIP)")
    print("3. Auto water science/tackle farm (WIP)")
    option = input()
    
    if option == "1":
        try:
            with open("settings.txt","r") as f:
                settings = f.readlines()
                global lst
                global fist
                global blk
                global no 
                lst = []
                for pos in settings[0].split(","):
                    coord = pos.split("&")
                    lst.append(gui.Point(int(coord[0]),int(coord[1])))
                fcoord = settings[1].split(",")[0].split("&")
                fist = gui.Point(int(fcoord[0]),int(fcoord[1]))
                bcoord = settings[1].split(",")[1].split("&")
                blk = gui.Point(int(bcoord[0]),int(bcoord[1]))
                no = int(settings[2])
            print("current pos")
            confirmpos()
            confirminv()
            print("No of punches: " + str(no))
            change = input("change settings?(y/n): ")
            if change == 'y':
                getblockspos()
                getbuttonspos()
                getnopunch()
            # print("Select blocks before u start")
            # ready = input("Ready? (yes to start)")
            # print("Press 'q' to stop")
            # autobreak(fist,blk,lst,no)
                
        except:
            getblockspos()
                
            getbuttonspos()
            
            getnopunch()
            #how many hits does it take
            #get a input then calc a time
        
        print("Select blocks before u start")
        ready = input("Ready? (yes to start)")
        print("Press 'q' to stop")
        autobreak(fist,blk,lst,no)
    elif option == "2":
        print("Working in Progress")
    elif option == "3":
        print("Hover ur cursor over punch button and press 'f'; Stand in the middle of the screen and put ur cursor on ur feet and press 'b'; press 'q' when done")
        getinv()
        collect(blk,fist)
main()
