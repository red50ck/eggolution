import random
import tkinter as tk
import pygame

class Sound:
    def __init__(self, root, sound_file):
        #initialisation of images, sound mixer and button
        self.ims_sound = [tk.PhotoImage(file = 'sound.png'),
                     tk.PhotoImage(file = 'mute_sound.png')]
        pygame.mixer.init()
        pygame.mixer.music.load(sound_file)
        self.sound_state = False
        self.sound_started = False
        self.button = tk.Button(root, image = self.ims_sound[0], bd = 0, bg = '#fcefd4',
                                activebackground = '#fcefd4', command = self.toggle_sound)
        self.button.place(x = 20, y = 500)
        
    #toggle sound button function
    def toggle_sound(self):
        if self.sound_state:
            pygame.mixer.music.pause()
            self.button.config(image = self.ims_sound[0])
        else:
            if self.sound_started and not pygame.mixer.music.get_busy():
                pygame.mixer.music.unpause()
            else:
                pygame.mixer.music.play(-1)
                self.sound_started = True
            self.button.config(image = self.ims_sound[1])
        self.sound_state = not self.sound_state

    #end music
    def sound_end(self):
        pygame.mixer.music.stop()
        
class Program:
    def __init__(self):
        #game window initialisation
        self.root = tk.Tk()
        self.root.title("Eggolution")
        self.root['bg'] = '#fcefd4'
        self.root.geometry("800x600")
        #initialisation of click cycle variables
        self.cc = 0
        self.d = 0
        self.i = 1
        self.r = random.randint((self.i*1),(6*self.i))
        #initialisation of images
        self.im = [tk.PhotoImage(file = '1.png'),
              tk.PhotoImage(file = '2.png'),
              tk.PhotoImage(file = '3.png'),
              tk.PhotoImage(file = '4.png'),
              tk.PhotoImage(file = '5.png'),
              tk.PhotoImage(file = '6.png'),
              tk.PhotoImage(file = '6.png')]
        self.imstart = tk.PhotoImage(file = 'start.gif')
        self.imend = tk.PhotoImage(file = 'end.png')
        self.end_image = tk.Label(self.root, image = self.imend)
        self.imquit = tk.PhotoImage(file = 'quit.png')
        #initialisation of buttons
        self.bstart = tk.Button(self.root, image = self.imstart, bd = 0, bg = '#fcefd4',
                        activebackground = '#fcefd4', command = self.start)
        self.bstart.place(x=150, y=215)
        self.bend = tk.Button(self.root, image = self.imend, bd = 0, bg = '#fcefd4',
                       activebackground = '#fcefd4', command = self.end)
        self.bquit = tk.Button(self.root, image = self.imquit, bd = 0, bg = '#fcefd4',
                        activebackground = '#fcefd4', command = self.quit)
        self.bquit.place(x = 720, y = 500)
        self.but = tk.Button(self.root, bd = 0, relief = 'groove', bg = '#fcefd4',
                        activebackground = '#fcefd4', image = self.im[self.d], command = self.click)
        #initialiation audiofile
        self.sound = Sound(self.root, 'wave.mp3')

    #main button click function  
    def click(self):
        self.cc += 1
        if self.cc == self.r:
                self.cc = 0
                self.i += 3
                self.d += 1
                self.but.config(image=self.im[self.d])
                self.r = random.randint((self.i*1),(1*self.i))
        if self.d > 5:
                self.end_image.place(x=150, y = 150)
                self.but.place_forget()

    #first button function            
    def start(self):
        self.but.place(x=200, y = 32)
        self.bstart.place_forget()

    #last button function    
    def end(self):
            print('Thanks for playing!')
            
    #close the window        
    def quit(self):
        self.sound.sound_end()
        self.root.destroy()
            
def main():
    #class element initialisation
    p = Program()
    
    p.root.mainloop()
        
if __name__ == "__main__":
    main()
