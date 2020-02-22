
import random
import os

#################################
## Content Management system data type 
#################################

class CMS(object):
    def __init__(self,name,des,size):
         self.name=name
         self.size=size
         self.des=des
    def get_details(self):
        return self.name
        return self.size
        return self.desclass


    def filesize(self):
     def __init__(self,name,des,size):
        CMS.__init__(self,name,des,size)
     def get_details(self):
        if self.size > 2 :
            
           return True
        else:
            return False
          
    
       


class PDF(CMS):
    def __init__(self,name,des,size):
        CMS.__init__(self,name,des,size)
                
        
    def get_details(self):

        return "%s created %s file and size is %s ." % (self.name, self.des, self.size)




class Word(CMS):
    def __init__(self,name,des,size):
        CMS.__init__(self,name,des,size)
               

    def get_details(self):

        return "%s created %s file and size is %s ." % (self.name, self.des, self.size)
    

  

class Picture(CMS):
    def __init__(self,name,des,size,dimension,form):
        CMS.__init__(self,name,des,size)
                
        self.dimension=dimension
        self.form=form

    def get_details(self):

        return "%s take %s and size is %s and dimension is %s and format is %s ." % (self.name, self.des, self.size,self.dimension,self.form)
    




class Video(CMS):

    def __init__(self,name,des,size,duration,form):
        CMS.__init__(self,name,des,size)
                
        self.duration=duration
        self.form=form

    def get_details(self):

        return "%s record %s and size is %sand duration is %s and format is %s  ." % (self.name, self.des, self.size,self.duration,self.form)
    


PDF1= PDF('shahram', 'pdf', 100)
Word1 = Word('shahram','word', 20)
picture1=Picture('shahram','pic1',100,'3*4','jpeg')
Movi1=Video('shahram','movie1',100,'30min','HD')



print(PDF1.get_details())
print(Word1.get_details())
print(picture1.get_details())
print(Movi1.get_details())




    






    
        
