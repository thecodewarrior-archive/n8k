import cPickle as pickle


class _Settings:
    ISO_VALUES = [60, 100, 200, 320, 400, 500, 640, 800]

    def __init__(self):
        self.iso = 0
        """The ISO power of the camera. The index in the ISO_VALUES array"""
        self.load()

    def get_iso(self):
        return (2**self.iso) * 100

    def save():
        try:
            outfile = open('cam.pkl', 'wb')
            # Use a dictionary (rather than pickling 'raw' values) so
            # the number & order of things can change without breaking.
            d = {'fx': fxMode,
                 'iso': isoMode,
                 'size': sizeMode,
                 'store': storeMode}
            pickle.dump(d, outfile)
            outfile.close()
        except:
            pass

    def load():
        try:
            infile = open('cam.pkl', 'rb')
            d = pickle.load(infile)
            infile.close()
            if 'fx' in d: setFxMode(d['fx'])
            if 'iso' in d: setIsoMode(d['iso'])
            if 'size' in d: sizeModeCallback(d['size'])
            if 'store' in d: storeModeCallback(d['store'])
        except:
            pass


Settings = _Settings()
