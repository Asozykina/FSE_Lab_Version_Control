class Storage:
    def __init__(self, data={}):
        super().__init__()
        if isinstance(data, dict):
            self.data = data
        else:
            raise Exception

    def get(self, key):
        if key in self.data:
            return self.data[key]
        else:
            return None

    def remove(self, key):
        if key in self.data:
            del self.data[key]

    def set(self,key,value):
        if key in self.data:
            self.data[key] = value
        else:
            print('key_not_found')
      

    def set(self):
        pass
    
    def add(self, key, value):
        self.data[key]=value