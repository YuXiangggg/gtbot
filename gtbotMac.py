from pynput import keyboard
import pyautogui as gui
import time
import keyboard as kb 

def autobreak(fpos,bpos,poslst):

    def punch(fpos,poslst):
        gui.click(fpos)
        for i in poslst:
            gui.moveTo(i)
            gui.dragTo(i.x+1,i.y,0.55,button="left")
            
    def place(bpos,poslst):
        gui.click(bpos)
        for i in poslst:
            gui.click(i)
    
    while not kb.is_pressed('q'):
        place(fpos,poslst)
        punch(bpos,poslst)


def getpos():
    global lst
    lst = []
    def on_release(key):
        

        if key == keyboard._darwin.KeyCode(char="c"):
            
            lst.append(gui.position())
        if key == keyboard._darwin.KeyCode(char="q"):
            
            return False
        

    with keyboard.Listener(on_release = on_release) as listener:
        listener.join()
        
    
def confirmpos():
    for i in lst:
        gui.moveTo(i)
        time.sleep(1)
        
        
def getinv():
    

    def on_release(key):
        

        if key == keyboard._darwin.KeyCode(char="f"):
            global fist
            fist = gui.position()
        if key == keyboard._darwin.KeyCode(char="b"):
            global blk
            blk = gui.position()
        if key == keyboard._darwin.KeyCode(char="q"):
            
            return False
        

    with keyboard.Listener(on_release = on_release) as listener:
        listener.join()
        
def confirminv():
    gui.moveTo(fist) 
    time.sleep(1)
    gui.moveTo(blk)   
        
    
    
    
    
def main():
    print("Welcome to this thing that fishburrito made before bicul eoy\n")
    print("This thing is illegal, you will be a bad growtopian if u use this\n")
    yn = input("Do you want to be a bad Growtopian? yes/no \n")
    if yn.lower() != "yes":
        print("Goodjob, bye!")
        time.sleep(1)
        exit()
    print("Okay bad growtopian what do you want to do?")
    print("1. Autobreak")
    print("2. Fishing (WIP)")
    print("3. Auto water science/tackle farm (WIP)")
    option = input()
    
    if option == "1":
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
        #how many hits does it take
        #get a input then calc a time
        
        print("Put the block in the 2nd inv space from the left and select it before u start")
        ready = input("Ready? (yes to start)")
        print("Press 'q' to stop")
        autobreak(fist,blk,lst)

main()