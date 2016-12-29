#from pydoc import help
class regnemaskine(object):
    '''
    Min regnemaskine kan meget
    '''

    res=1
    tal=1
    def __str__(self):
        return('Min regnemaskine klasse')
    def __init__(self, tal , res):
        self.res=res
      #  print(' ',self, ' ', res, ' ', tal)
        self.navn = 'truttelut'

    def plus(self, tal):
        '''Her kan tal lgges sammen'''
        #  print(self, 'old  ', self.res, ' operator ', tal)
        self.res=tal+self.res
        return self.res

    def gange(self, tal):
        self.res=tal*self.res
        return self.res
    def minus(self, tal):
        self.res=self.res-tal
        return self.res
    def divider(self, tal):
      #  print(self, ' ', self.res, ' ', tal)
        self.res=self.res/tal
        return self.res


t1 = regnemaskine(0, 0)

print(t1.plus(2))
#print (t1.tal,t1.res)
