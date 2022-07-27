from __future__ import absolute_import, division
import time
import psychopy
from psychopy import sound, gui, visual, core, data, event
from psychopy.hardware import keyboard
#from playsound import playsound
import numpy as np  # whole numpy lib is available, prepend 'np.'
import os  # handy system and path functions
import sys  # to get file system encoding
import pyglet
import math
import serial  #connecting to the serial port (Arduino)
from argparse import ArgumentParser
import random
# import keyboard
#import csv
"""

created by criminal mastermind "XD"
p.ortegaauriol@auckland.ac.nz
06/22

"""

_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)


class Experiment(object):
    print(os.getcwd())
    def __init__(self):
        psychopy.prefs.hardware['audioLib'] = ['PTB', 'pyo', 'pygame']
        self.countdown_clock = core.Clock()
        self.trialClock = core.Clock()
        self.delay = []
        self.shock = []
        self.range = []
        self.threat_bedroom = []
        self.threat_dining = []
        self.threat_gar = []
        self.threat_kit = []
        self.threat_lo = []
        self.RT = []
        self.nthreat_bedroom = []
        self.nthreat_dining = []
        self.nthreat_gar = []
        self.nthreat_kit = []
        self.nthreat_lo = []

        self.background = []
        self.nothreat = []
        self.Task()

        self.win = visual.Window(
            size= [1920, 1080],
            fullscr=self.expInfo['Full Screen'],
            winType='pyglet',
            monitor='testMonitor',
            screen=1,
            # monitor = 'Wired Display',
            color=[-1, -1, -1], colorSpace='rgb',
            # blendMode='avg', mouseVisible = False, allowGUI=False)
            blendMode='avg', allowGUI=False)
        #Instructions
        self.Break  = visual.ImageStim(self.win, image='Images/Instructions' + os.sep + 'Break.jpg')
        self.Correct  = visual.ImageStim(self.win, image='Images/Instructions' + os.sep + 'Correct.jpg')
        self.Incorrect  = visual.ImageStim(self.win, image='Images/Instructions' + os.sep + 'Incorrect.jpg')
        self.Instructions  = visual.ImageStim(self.win, image='Images/Instructions' + os.sep + 'Instructions.jpg')
        self.Trigger  = visual.ImageStim(self.win, image='Images/Instructions' + os.sep + 'Trigger.jpg')
        
        #Backgrounnd
        self.range.append(visual.ImageStim(self.win, image='Images/Background' + os.sep + 'Bedroom.jpg'))
        self.range.append(visual.ImageStim(self.win, image='Images/Background' + os.sep + 'Lounge.jpg'))
        self.range.append(visual.ImageStim(self.win, image='Images/Background' + os.sep + 'Kitchen.jpg'))
        self.range.append(visual.ImageStim(self.win, image='Images/Background' + os.sep + 'Garage.jpg'))
        self.range.append(visual.ImageStim(self.win, image='Images/Background' + os.sep + 'Dining Room.jpg'))

        #GO
        self.threat_bedroom.append(visual.ImageStim(self.win, image='Images/go' + os.sep + 'Bedroom Machete L.jpg'))
        self.threat_bedroom.append(visual.ImageStim(self.win, image='Images/go' + os.sep + 'Bedroom Machete R.jpg'))
        self.threat_bedroom.append(visual.ImageStim(self.win, image='Images/go' + os.sep + 'Bedroom Pistol L.jpg'))
        self.threat_bedroom.append(visual.ImageStim(self.win, image='Images/go' + os.sep + 'Bedroom Pistol R.jpg'))
        self.threat_bedroom.append(visual.ImageStim(self.win, image='Images/go' + os.sep + 'Bedroom Rifle L.jpg'))
        self.threat_bedroom.append(visual.ImageStim(self.win, image='Images/go' + os.sep + 'Bedroom Rifle R.jpg'))

        self.threat_dining.append(visual.ImageStim(self.win, image='Images/go' + os.sep + 'Dining Room Machete L.jpg'))
        self.threat_dining.append(visual.ImageStim(self.win, image='Images/go' + os.sep + 'Dining Room Machete R.jpg'))
        self.threat_dining.append(visual.ImageStim(self.win, image='Images/go' + os.sep + 'Dining Room Pistol L.jpg'))
        self.threat_dining.append(visual.ImageStim(self.win, image='Images/go' + os.sep + 'Dining Room Pistol R.jpg'))
        self.threat_dining.append(visual.ImageStim(self.win, image='Images/go' + os.sep + 'Dining Room Rifle L.jpg'))
        self.threat_dining.append(visual.ImageStim(self.win, image='Images/go' + os.sep + 'Dining Room Rifle R.jpg'))

        self.threat_gar.append(visual.ImageStim(self.win, image='Images/go' + os.sep + 'Garage Machete L.jpg'))
        self.threat_gar.append(visual.ImageStim(self.win, image='Images/go' + os.sep + 'Garage Machete R.jpg'))
        self.threat_gar.append(visual.ImageStim(self.win, image='Images/go' + os.sep + 'Garage Pistol L.jpg'))
        self.threat_gar.append(visual.ImageStim(self.win, image='Images/go' + os.sep + 'Garage Pistol R.jpg'))
        self.threat_gar.append(visual.ImageStim(self.win, image='Images/go' + os.sep + 'Garage Rifle L.jpg'))
        self.threat_gar.append(visual.ImageStim(self.win, image='Images/go' + os.sep + 'Garage Rifle R.jpg'))

        self.threat_kit.append(visual.ImageStim(self.win, image='Images/go' + os.sep + 'Kitchen Machete L.jpg'))
        self.threat_kit.append(visual.ImageStim(self.win, image='Images/go' + os.sep + 'Kitchen Machete R.jpg'))
        self.threat_kit.append(visual.ImageStim(self.win, image='Images/go' + os.sep + 'Kitchen Pistol L.jpg'))
        self.threat_kit.append(visual.ImageStim(self.win, image='Images/go' + os.sep + 'Kitchen Pistol R.jpg'))
        self.threat_kit.append(visual.ImageStim(self.win, image='Images/go' + os.sep + 'Kitchen Rifle L.jpg'))
        self.threat_kit.append(visual.ImageStim(self.win, image='Images/go' + os.sep + 'Kitchen Rifle R.jpg'))

        self.threat_lo.append(visual.ImageStim(self.win, image='Images/go' + os.sep + 'Lounge Machete L.jpg'))
        self.threat_lo.append(visual.ImageStim(self.win, image='Images/go' + os.sep + 'Lounge Machete R.jpg'))
        self.threat_lo.append(visual.ImageStim(self.win, image='Images/go' + os.sep + 'Lounge Pistol L.jpg'))
        self.threat_lo.append(visual.ImageStim(self.win, image='Images/go' + os.sep + 'Lounge Pistol R.jpg'))
        self.threat_lo.append(visual.ImageStim(self.win, image='Images/go' + os.sep + 'Lounge Rifle L.jpg'))
        self.threat_lo.append(visual.ImageStim(self.win, image='Images/go' + os.sep + 'Lounge Rifle R.jpg'))

        #NOGO

        self.nthreat_bedroom.append(visual.ImageStim(self.win, image='Images/NoGo' + os.sep + 'Bedroom Cup L.jpg'))
        self.nthreat_bedroom.append(visual.ImageStim(self.win, image='Images/NoGo' + os.sep + 'Bedroom Cup R.jpg'))
        self.nthreat_bedroom.append(visual.ImageStim(self.win, image='Images/NoGo' + os.sep + 'Bedroom Keys L.jpg'))
        self.nthreat_bedroom.append(visual.ImageStim(self.win, image='Images/NoGo' + os.sep + 'Bedroom Keys R.jpg'))
        self.nthreat_bedroom.append(visual.ImageStim(self.win, image='Images/NoGo' + os.sep + 'Bedroom Phone L.jpg'))
        self.nthreat_bedroom.append(visual.ImageStim(self.win, image='Images/NoGo' + os.sep + 'Bedroom Phone R.jpg'))

        self.nthreat_dining.append(visual.ImageStim(self.win, image='Images/NoGo' + os.sep + 'Dining Room Cup L.jpg'))
        self.nthreat_dining.append(visual.ImageStim(self.win, image='Images/NoGo' + os.sep + 'Dining Room Cup R.jpg'))
        self.nthreat_dining.append(visual.ImageStim(self.win, image='Images/NoGo' + os.sep + 'Dining Room Keys L.jpg'))
        self.nthreat_dining.append(visual.ImageStim(self.win, image='Images/NoGo' + os.sep + 'Dining Room Keys R.jpg'))
        self.nthreat_dining.append(visual.ImageStim(self.win, image='Images/NoGo' + os.sep + 'Dining Room Phone L.jpg'))
        self.nthreat_dining.append(visual.ImageStim(self.win, image='Images/NoGo' + os.sep + 'Dining Room Phone R.jpg'))

        self.nthreat_gar.append(visual.ImageStim(self.win, image='Images/NoGo' + os.sep + 'Garage Cup L.jpg'))
        self.nthreat_gar.append(visual.ImageStim(self.win, image='Images/NoGo' + os.sep + 'Garage Cup R.jpg'))
        self.nthreat_gar.append(visual.ImageStim(self.win, image='Images/NoGo' + os.sep + 'Garage Keys L.jpg'))
        self.nthreat_gar.append(visual.ImageStim(self.win, image='Images/NoGo' + os.sep + 'Garage Keys R.jpg'))
        self.nthreat_gar.append(visual.ImageStim(self.win, image='Images/NoGo' + os.sep + 'Garage Phone L.jpg'))
        self.nthreat_gar.append(visual.ImageStim(self.win, image='Images/NoGo' + os.sep + 'Garage Phone R.jpg'))

        self.nthreat_kit.append(visual.ImageStim(self.win, image='Images/NoGo' + os.sep + 'Kitchen Cup L.jpg'))
        self.nthreat_kit.append(visual.ImageStim(self.win, image='Images/NoGo' + os.sep + 'Kitchen Cup R.jpg'))
        self.nthreat_kit.append(visual.ImageStim(self.win, image='Images/NoGo' + os.sep + 'Kitchen Keys L.jpg'))
        self.nthreat_kit.append(visual.ImageStim(self.win, image='Images/NoGo' + os.sep + 'Kitchen Keys R.jpg'))
        self.nthreat_kit.append(visual.ImageStim(self.win, image='Images/NoGo' + os.sep + 'Kitchen Phone L.jpg'))
        self.nthreat_kit.append(visual.ImageStim(self.win, image='Images/NoGo' + os.sep + 'Kitchen Phone R.jpg'))

        self.nthreat_lo.append(visual.ImageStim(self.win, image='Images/NoGo' + os.sep + 'Lounge Cup L.jpg'))
        self.nthreat_lo.append(visual.ImageStim(self.win, image='Images/NoGo' + os.sep + 'Lounge Cup R.jpg'))
        self.nthreat_lo.append(visual.ImageStim(self.win, image='Images/NoGo' + os.sep + 'Lounge Keys L.jpg'))
        self.nthreat_lo.append(visual.ImageStim(self.win, image='Images/NoGo' + os.sep + 'Lounge Keys R.jpg'))
        self.nthreat_lo.append(visual.ImageStim(self.win, image='Images/NoGo' + os.sep + 'Lounge Phone L.jpg'))
        self.nthreat_lo.append(visual.ImageStim(self.win, image='Images/NoGo' + os.sep + 'Lounge Phone R.jpg'))


        #self.nothreat = visual.ImageStim(self.win, image='Images' + os.sep + 'NonThreat.jpg')

        self.Workflow()

    def Task(self):
        # Participant information
        self.expInfo = {'Participant code': 0000,'Session':00, 'Age (Years)': 00, 'Gender': ['M', 'F', 'Other'],
                        'n_go_trials (per block)': 3, 'n_stop_trials (per block)': 1, 'n blocks': 3,
                          'practice trials': True, 'n practice go trials': 1,
                          'n practice stop trials': 1, 'Full Screen': False, 'Keyboard': True,
                        'Threat Mode': True, 'Threat Response': 0.5,
                        'Response End Time': 2, 'Delay_1': 1.5, 'Delay_2': 2, 'Delay_3': 2.5 }
        self.expName = 'Shoot'
        dlg = gui.DlgFromDict(dictionary=self.expInfo, title='Participant Information', tip=None)
        if dlg.OK == False:
            print('Closing port and exit')
            self.arduino.close()
            core.quit()
        self.expInfo['date'] = data.getDateStr()
        #dlg.Destroy()
        return

    def Workflow(self):
        self.gen_trials()
        # define the instructions for the task?
        self.runExperiment()

    def gen_trials(self):
        print('Generating Trials')
        # Generate trials
        if self.expInfo['practice trials']:
            self.train_trial = [1] * self.expInfo['n practice go trials'] + [0] * self.expInfo['n practice stop trials']
            random.shuffle(self.train_trial)
        else:
            self.train_trial = []

        self.trials = [0] * self.expInfo['n_stop_trials (per block)'] + [1] * self.expInfo['n_go_trials (per block)']

        #Generating blocks
        if not self.expInfo['Threat Mode']:
            self.blocks = [0] * int(self.expInfo['n blocks'])
        else:
            self.blocks = [0] * int(math.ceil(self.expInfo['n blocks']/2)) + [1] * int(math.floor(self.expInfo['n blocks']/2))

        # Generate the random delays / trials
        self.times = [self.expInfo['Delay_1'], self.expInfo['Delay_2'],self.expInfo['Delay_3']]
        # Trials/delays * blocks
        self.trials = [self.trials]*len(self.blocks)

        background = []
        for sub in range(0, len(self.trials)):
            for n in range(len(self.trials[sub])):
                background.append(random.randint(0, int(len(self.range))-1))

        n = len(self.trials[0])
        self.background = [background[i:i + n] for i in range(0, len(background), n)]


        #Random shuffle the lists
        for i in self.trials:
            self.delay.append(random.choices(self.times, weights=[1, 1, 1], k=len(i)))
            if self.expInfo['Threat Mode']:
                self.shock.append([0]*int(len(i)/2) + [1]*int(len(i)/2))
            else:
                self.shock.append([0] * int(len(i)))

        self.trials = [random.sample(i, len(i)) for i in self.trials]
        self.shock = [random.sample(i, len(i)) for i in self.shock]
        random.shuffle(self.blocks)

        print('Practice Trials', self.train_trial)
        print('\nTrials', self.trials,'\nBlocks', self.blocks, '\nDelay', self.delay, '\nThreat', self.shock)
        print('Background = ', self.background)

    def countdown(self):  # give countdown and if finger is lifted say this is too soon and restart
        if self.expInfo['CountDown']:
            self.countdown_clock.reset()
            while int(self.countdown_clock.getTime()) < 4:
                pass
                #print(str(self.countdown_clock.getTime()))
            return

    def wait_keyboard(self):
        kb = keyboard.Keyboard()
        for keys in kb.getKeys(['space']):
            pass
        keys = []
        while True:
            keys = kb.getKeys(['space'], waitRelease=False, clear=True)
            if keys:
                return

    def keyboarding(self):
        kb = keyboard.Keyboard()
        for keys in kb.getKeys(['space']):
            pass
        keys = []
        while True:
            keys = kb.getKeys(['space'], waitRelease=False, clear=True)
            if keys:
                self.RT = self.trialClock.getTime()
                return self.RT
            elif int(self.trialClock.getTime()) >= self.expInfo['Response End Time']:
                self.RT = self.trialClock.getTime()
                return

    def classifier(self, shock, trial, block):

        # Classify for Shock
        if self.RT > self.expInfo['Threat Response'] and shock == 1 and \
                trial == 1 and block == 1:
            print (self.RT)
            self.Incorrect.draw()
            self.win.flip()
            time.sleep(1)
        elif self.RT < self.expInfo['Response End Time'] and shock == 1 and \
                trial == 0 and block == 1:
            print (self.RT)
            self.electroshock()
            self.Incorrect.draw()
            self.win.flip()
            time.sleep(1)

        #Shoot trial
        if self.RT > self.expInfo['Threat Response'] and trial == 1:
            print (self.RT)
            self.Incorrect.draw()
            self.win.flip()
            time.sleep(1)

        elif self.RT < self.expInfo['Response End Time'] and trial == 0:
            print (self.RT)
            self.Incorrect.draw()
            self.win.flip()
            time.sleep(1)
        else:
            # Build a classifier for the non-shock trials
            print (self.RT)
            self.Correct.draw()
            self.win.flip()
            time.sleep(1)

    def runExperiment(self):
        print('Experiment')
        self.Instructions.draw()
        self.win.flip()
        self.wait_keyboard()

        # Training Trials
        if self.train_trial:
            for k in np.arange(0, len(self.train_trial), 1):
                # for lines in self.arduino.readline(): pass
                print('Practice Trial')
                self.range[0].draw()
                self.win.flip()
                time.sleep(2)
                if self.train_trial[k] == 0:
                    self.nthreat_bedroom[random.randint(0, 1)].draw()
                else:
                    self.threat_bedroom[random.randint(0, 1)].draw()
                self.win.flip()
                self.trialClock.reset()
                self.keyboarding()
                print('Practice RT = ', self.RT)
                time.sleep(2)
                self.win.flip()
                time.sleep(3)
            print('End of Practice Trials')
            self.win.flip()
            self.wait_keyboard()

        # Experiment Trial
        for block in range(self.expInfo['n blocks']):
            #variables in the block
            trials = self.trials[block]
            delay = self.delay[block]
            shock = self.shock[block]
            background = self.background[block]
            # for lines in self.arduino.readline(): pass
            for k in np.arange(0, len(trials), 1):
                self.range[0].draw()
                self.win.flip()
                time.sleep(delay[k])

                #given the background and trial type show an according threat/no threat image/
                if trials[k] == 0:
                    self.nthreat_bedroom[random.randint(0, 2)].draw()

                elif trials[k] == 1:
                    self.threat_bedroom[random.randint(0, 2)].draw()

                self.win.flip()
                self.trialClock.reset()
                self.keyboarding()
                #Process response time for shock or feedback
                print('RT = ', self.RT)

                # Keep the screen for a consistent time after trigger independently of the trial type.
                while True:
                    if int(self.trialClock.getTime()) >= self.expInfo['Response End Time']:
                        break
                #Classify the reaction time
                self.classifier(shock[k], trials[k], self.blocks[block])
                self.win.flip()
                time.sleep(3)

    def savedata(self, RT, trial, shock, delay, block):
        # Save Variables into a file
        with open('DataFile' + str(self.expInfo['Participant code']) + str(self.expInfo['Session']) + '.txt', 'a') as b:
            b.write('\n %.4f    %s  %s  %s  %s  %s  %s	' % (RT, trial, shock, delay, block, self.expInfo['Participant code'],self.expInfo['Session']))
        # end trial wait time
        print('end trial wait')

    def saveconfig(self):
        with open('config' + '.txt', 'a') as b:
            b.write('%s  \n%s  \n%s  \n%s   \n%s\n' %
                    (self.shock, self.trials, self.expInfo, self.delay, self.blocks))

    def stats(self):
        #Read the saved file and do some stats with it for display.
        pass


if __name__ == "__main__":
    sa = Experiment()