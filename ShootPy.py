from __future__ import absolute_import, division
import time
import psychopy
from psychopy import sound, gui, visual, core, data, event
import pandas as pd
import numpy as np  # whole numpy lib is available, prepend 'np.'
import os  # handy system and path functions
import matplotlib.pyplot as plt
import math
import serial  #connecting to the serial port (Arduino)
import random
#import csv
"""

created by criminal mastermind
p.ortegaauriol@auckland.ac.nz
06/22

"""

_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

class Experiment(object):
    print(os.getcwd())
    def __init__(self):
        # Arduino & Serial port configuration
        psychopy.prefs.hardware['audioLib'] = ['PTB', 'pyo', 'pygame']
        self.arduino = serial.Serial('COM7', 9600, timeout=0)
        self.line = self.arduino.readline()
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
        self.result = 0
        self.nthreat_bedroom = []
        self.nthreat_dining = []
        self.nthreat_gar = []
        self.nthreat_kit = []
        self.nthreat_lo = []

        self.background = []

        self.nothreat = []
        self.Task()

        #Panda data frame
        self.df = pd.DataFrame({"RT": [], "Trial": [], "Delay": [],"Threat": [], "PCode": [], "Session": [], 'Block': []})

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
                          'n practice stop trials': 1, 'Full Screen': False,
                        'Threat Mode': True, 'Threat Response': 0.5,
                        'Response End Time': 2, 'Delay_1': 1.5, 'Delay_2': 2, 'Delay_3': 2.5 }
        self.expName = 'Shoot'
        dlg = gui.DlgFromDict(dictionary=self.expInfo, title='Participant Information', tip=None)
        if dlg.OK == False:
            print('Closing port and exit')
            self.arduino.close()
            core.quit()
        self.expInfo['date'] = data.getDateStr()
        header = "RT    Trial   Delay   Threat   Code    Session "
        with open('DataFile' + str(self.expInfo['Participant code']) + str(self.expInfo['Session']) + '.txt', 'a') as b:
            b.write(header + "\n")
            b.close()
        return

    def Workflow(self):
        self.gen_trials()
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
                self.shock.append([1]*int(len(i)/2) + [1]*int(len(i)/2))
            else:
                self.shock.append([0] * int(len(i)))


        self.trials = [random.sample(i, len(i)) for i in self.trials]
        self.shock = [random.sample(i, len(i)) for i in self.shock]
        random.shuffle(self.blocks)

        print('Practice Trials', self.train_trial)
        print('\nTrials', self.trials,'\nBlocks', self.blocks, '\nDelay', self.delay, '\nThreat', self.shock)
        print('Background = ', self.background)

    def waitSwitch(self):
        for lines in self.arduino.readline(): pass
        line = []
        print('Press Trigger to Start')
        while len(line) == 0:
            line = self.arduino.readline()
            core.wait(0.1)
        print('Switch Pressed')
        time.sleep(0.1)
        for lines in self.arduino.readline():pass
        return

    def countdown(self):  # give countdown and if finger is lifted say this is too soon and restart
        if self.expInfo['CountDown']:
            self.countdown_clock.reset()
            while int(self.countdown_clock.getTime()) < 4:
                pass
                #print(str(self.countdown_clock.getTime()))
            return

    def trigger(self):
        for lines in self.arduino.readline(): pass
        line = []
        while len(line) == 0:
            line = self.arduino.readline()
            if int(self.trialClock.getTime()) >= self.expInfo['Response End Time']:
                break
        self.RT =  self.trialClock.getTime()
        #if not len(line) == 0:
            #playsound(r"""D:/Work/Shoot or Don't Shoot/sound/Gunshot.mp3""")
        #time.sleep(1)
        return self.RT

    def electroshock(self):
        print('Send Shock')
        self.arduino.write([1])
        return

    def emg(self):
        self.arduino.write([2])
        return

    def classifier(self, trial, block):

        # Classify for Shock
        if self.RT > self.expInfo['Threat Response'] and trial == 1:
            self.Incorrect.draw()
            if block == 1:
                self.electroshock()
            self.win.flip()
            time.sleep(1)
            self.result = 0

        elif self.RT < self.expInfo['Response End Time'] and trial == 0:
            self.Incorrect.draw()
            if block == 1:
                self.electroshock()
            self.win.flip()
            time.sleep(1)
            self.result = 0

        else:
            # Build a classifier for the non-shock trials
            self.Correct.draw()
            self.win.flip()
            time.sleep(1)
            self.result = 1

    def runExperiment(self):
        print('Experiment')
        self.saveconfig()
        self.Instructions.draw()
        self.win.flip()
        self.waitSwitch()

        # Training Trials
        if self.train_trial:
            for k in np.arange(0, len(self.train_trial), 1):
                for lines in self.arduino.readline(): pass
                print('Practice Trial')
                self.range[0].draw()
                self.win.flip()
                time.sleep(2)
                if self.train_trial[k] == 0:
                    self.nthreat_bedroom[random.randint(0, 5)].draw()
                else:
                    self.threat_bedroom[random.randint(0, 5)].draw()
                self.win.flip()
                self.trialClock.reset()
                self.trigger()
                print('Practice RT = ', self.RT)
                time.sleep(2)
                self.win.flip()
                time.sleep(3)
            print('End of Practice Trials')
            self.Break.draw()
            self.win.flip()
            self.waitSwitch()

        # Experiment Trial
        for block in range(self.expInfo['n blocks']):

            #variables in the block
            trials = self.trials[block]
            delay = self.delay[block]
            background = self.background[block]
            for lines in self.arduino.readline(): pass
            for k in np.arange(0, len(trials), 1):

                print('\n Trial =', k, 'Threat = ', self.blocks[block], 'Shoot = ', trials[k])

                for lines in self.arduino.readline(): pass
                self.range[background[k]].draw()
                self.win.flip()
                time.sleep(delay[k])

                #given the background and trial type show an according threat/no threat image/
                if trials[k] == 0:
                    if background[k] == 0:
                        self.nthreat_bedroom[random.randint(0,5)].draw()
                    elif background[k] == 1:
                        self.nthreat_lo[random.randint(0, 5)].draw()
                    elif background[k] == 2:
                        self.nthreat_kit[random.randint(0, 5)].draw()
                    elif background[k] == 3:
                        self.nthreat_gar[random.randint(0, 5)].draw()
                    elif background[k] == 4:
                        self.nthreat_dining[random.randint(0, 5)].draw()

                elif trials[k] == 1:
                    if background[k] == 0:
                        self.threat_bedroom[random.randint(0, 5)].draw()
                    elif background[k] == 1:
                        self.threat_lo[random.randint(0, 5)].draw()
                    elif background[k] == 2:
                        self.threat_kit[random.randint(0, 5)].draw()
                    elif background[k] == 3:
                        self.threat_gar[random.randint(0, 5)].draw()
                    elif background[k] == 4:
                        self.threat_dining[random.randint(0, 5)].draw()

                self.win.flip()
                self.emg()
                self.trialClock.reset()
                self.trigger()
                #Process response time for shock or feedback
                print('RT = ', self.RT)

                # Keep the screen for a consistent time after trigger independently of the trial type.
                while True:
                    if int(self.trialClock.getTime()) >= self.expInfo['Response End Time']:
                        break
                #Classify the reaction time
                self.classifier(trials[k], self.blocks[block])

                # self.win.flip()
                #Save the trials/info
                self.savedata(self.RT, trials[k], delay[k], self.blocks[block], self.result, block)
                time.sleep(3)
            self.stats(block)
            self.Break.draw()
            self.win.flip()
            for lines in self.arduino.readline(): pass
            self.waitSwitch()
            for lines in self.arduino.readline(): pass

    def saveconfig(self):
        with open('config' + '.txt', 'a') as b:
            b.write('%s  \n%s  \n%s   \n%s\n' %
                    (self.trials, self.expInfo, self.delay, self.blocks))

    def savedata(self, RT, trial, delay, threat, result, block):
        # Save Variables into a file

        df2 = pd.DataFrame({"RT": [RT], "Trial": [trial], "Delay": [delay], "Threat": [threat],
                            "PCode": [self.expInfo['Participant code']], "Session": [self.expInfo['Session']],
                            "Outcome": [result], "Block": [block]})
        self.df = pd.concat([self.df, df2])
        self.df.to_csv('DataFile' + str(self.expInfo['Participant code']) + '_' + str(self.expInfo['Session']) + '.csv', index=False)

    def stats(self, block):
        # Descriptive statistics at the end of the block.

        # MEAN REACTION TIME OF TRIALS
        df1 = self.df[['RT', 'Trial']]
        df1 = df1.groupby(['Trial'], as_index=False).mean()
        #Trials which are only a go.
        df2 = self.df.RT.where(self.df.Trial != 0)
        df2 = df2.dropna(axis=0)

        # PIE DATA
        df3 = self.df[['RT', 'Outcome']]
        piedata = [df3.Outcome.where(df3.Outcome == 1).count(), df3.Outcome.where(df3.Outcome == 0).count()]

        #PIE PLOT
        plt.figure(figsize=(12, 6))  # set figure size
        plt.xticks(family='Arial', size=12)
        plt.yticks(family='Arial', size=12)
        labels = ['Success', 'Fail']
        #colors = sns.color_palette('pastel')[0:2]
        p2 = plt.pie(piedata, labels=labels, autopct='%.0f%%') #colors=colors
        plt.savefig(_thisDir + '\Plot_%s_%s' % (self.expInfo['Participant code'], self.expInfo['Session']))
        pieplot = visual.ImageStim(self.win, image=(_thisDir + '\Plot_%s_%s' % (self.expInfo['Participant code'],
                                    self.expInfo['Session']) + '.png'), pos=[0, 0], units='cm', color=[1, 1, 1])
        pieplot.draw()
        self.win.flip()
        time.sleep(8)
        # LinePlot
        plt.figure(figsize=(12, 6))
        plt.ylabel('Reaction Time', size=20, family='Arial')  # create plot
        plt.xlabel('Trial Number', size=20, family='Arial')
        n = [float(i) for i in df2]
        p1 = plt.plot(n, linewidth=3)
        plt.xlabel("Trial Number")
        plt.ylabel("Reaction Time (sec)")
        plt.axhline(0.5, color='red')
        plt.savefig(_thisDir + '\Plot_%s_%s' % (self.expInfo['Participant code'], self.expInfo['Session']))
        linerplot = visual.ImageStim(self.win, image=(_thisDir + '\Plot_%s_%s' % (self.expInfo['Participant code'],
                                        self.expInfo['Session']) + '.png'), pos=[0, 0], units='cm', color=[1, 1, 1])
        linerplot.draw()
        self.win.flip()
        time.sleep(8)

if __name__ == "__main__":
    #parser = ArgumentParser(description=" FPS Shooter ")
    sa = Experiment()