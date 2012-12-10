import wave
import struct
import array

class Wave:

	def __init__(self):
            '''Initialize a new Wave object.  Use load to read in an existing file.'''
	    self.wave = None
	    self.number_channels = 1
	    self.sample_width = 2
	    self.sampling_rate = 48000
	    self.number_frames = 0
	    self.frames = []
	    self.sampleData = array.array('h')
	    self.unpackedData = []


	def load(self, wavfilename):
            '''Load in a wave file given by wavfilename.'''
	    self.wave = wave.open(wavfilename, 'r')
	    self.number_channels = self.wave.getnchannels()
	    self.sample_width = self.wave.getsampwidth()
	    self.sampling_rate = self.wave.getframerate()
	    self.number_frames = self.wave.getnframes()
	    self.frameData = self.wave.readframes(self.wave.getnframes())

	    for f in range(0, self.wave.getnframes()):
		self.unpackedData.append(struct.unpack("b", self.frameData[f]))


	def helpfulprinter(self):
	    print self.wave
	    print self.number_channels
	    print self.sample_width
	    print self.sampling_rate, "fps"
	    print "number of frames is", self.number_frames
	    print self.unpackedData[500][0], " is the value of frame 500"


	def get_max_frame(self):
            '''Find and return the most extreme wave value in the file.'''
            biggest_index = 0
            for i in range(0, self.number_frames):
                if abs(self.unpackedData[i][0] > biggest_index):
                    biggest_index = self.unpackedData[i][0]
	    print biggest_index, " is the most extreme value"
            return biggest_index

	def adjustVolume(self, x):

	def normalizeVolume(self):

	def save(self):

myWave = Wave()
myWave.load("minor_clam.wav")
myWave.helpfulprinter()
myWave.get_max_frame()
