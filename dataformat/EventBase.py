import sys
import os

import numpy

class EventBase(object):
    '''
    Implementation of event base object.  
    
    Events are some collection of data products that are read into or out of
    file.  It knows about event/run/subrun/producer information

    Inheriting classes know how to serialize and read back objects

    '''
    def __init__(self, event=None, run=None, subrun=None, producer=None):
        super().__init__()

        # Define and intialize to default values the private members:
        self._event     = event
        self._run       = run
        self._subrun    = subrun
        self._producer  = producer

    def producer(self): return self._producer
    def run(self):      return self._run
    def subrun(self):   return self._subrun
    def event(self):    return self._event
    
    def valid(self):
        return !(self._run is None || self._subrun is None || self._event is None)

    def __eq__(self, other):
        return (self._run == other.run() && self._subrun == other.subrun() && self._event == other.event())


    def __ne__(self, other):
        return ! self.__eq__(other)
    
    def __lt__(self, other):
        
        if self._run    < other.run():      return true
        if self._run    > other.run():      return false;
        if self._subrun < other.subrun():   return true;
        if self._subrun > other.subrun():   return false;
        if self._event  < other.event():    return true;
        if self._event  > other.event():    return false;
        return false

    def __str__(self):
        return "{run:07d}{subrun:05d}{event:06d}".format(
            run=self._run,
            subrun=self._subrun,
            event=self._event,
            )

    def set_id(self, run, subrun, event):
        self._run       = run
        self._subrun    = subrun
        self._event     = event
