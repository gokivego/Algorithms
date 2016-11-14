#SGD

# -*- coding: utf-8 -*-
"""
    Created on Wed Sep 21 17:07:30 2016
    
    @author: gokivego
    """

from parabola import *
import scipy
import matplotlib
import matplotlib.pyplot
import pylab
from matplotlib import collections
from mpl_toolkits.mplot3d import Axes3D

def sfunc(k,gamma=0.9,start=10):
    return float(start)/(k**gamma)


class SGD:
    def __init__(self,afunc,x0,sfunc, proj = None, histsize = -1,
                 smallhist = False, ndata = 100, keepobj = True):
        
        """
            afunc −− the objective. has afunc.sgrad(x,ndata) returning a stochastic subgradient ,
            afunc . feval (x) returning a function evaluation , and
            afunc. sfeval(x,ndata ) returning a stochastic function evaluation
            x0 −− initial point
            sfunc −− a step function . sfunc (n) returns the size of the nth step
            proj −− a projection function . proj(x) returns the closest
            point to x within the feasible region
            histsize −− how many steps of history to maintain (−1 is all the steps )
            smallhist −− whether to maintain the history of gradients ,
            stepsizes , and pre−projection points
            ndata −− the number of data points to pass into sgrad and
            sfeval
            keepobj −− whether to maintain a history of the objective
            function value
            
            """
        
        self.afunc = afunc
        self.sfunc = sfunc
        self.proj = proj
        self.x0 = scipy.array(x0)
        #if self.proj == None:
        self.histsize = histsize
        self.smallhist = smallhist
        self.ndata = ndata
        self.init_point = scipy.array(x0)
        self.next_point = scipy.array(x0)
        self.keepobj = keepobj
        self.reset()
    
    ######################################
    
    def setStart(self, x0):
        
        """
            Set the start point
            """
        
        self.init_point = scipy.array(x0)
    
    
    ######################################
    
    def reset(self):
        """
            Reset the history of the optimization . In other words ,
            drop all history and start again from x0 and 1st step.
            """
        self.n = 1
        #self.histsize = 0
        self.grad_hist = []
        self.step_hist = []
        self.x_hist = []
        #if self.keepobj:
        self.init_point = scipy.array(self.x0)
        self.x_hist.append(self.x0.tolist())
        
        """
            if not self.proj:
            self.x_hist_aft_proj.append(self.proj(self.x0))
            else:
            self.x_hist_aft_proj.append(self.x0)
            """
    ######################################
    def dostep(self):
        """
            Take a single step of SGD.
            
            """
        
        self.next_point = self.init_point - sfunc(self.n)*afunc.sgrad(self.init_point.tolist(), self.ndata)
        self.x_hist.append(self.next_point.tolist())
        self.init_point=self.next_point
        self.n += 1
    
    #####################################
    
    def nsteps(self, an = 1):
        """
            Take n steps of SGD
            
            """
        for i in range(an):
            self.dostep()
    ######################################

def getAvgSoln(self, wsize = 10):
    
    """
        Average the last wsize points and return a solution
        
        """
            
            latest_wsize_points=scipy.array(self.x_hist[-(wsize):])
                return scipy.average(latest_wsize_points,axis=0)

######################################

def getSoln(self, wsize = 10, winterval = 1, abstol = 1e-6, reltol = 1e-6):
    """
        Keep performing SGD steps until :  afunc.feval(x∗_prev) and afunc.feval(x*) is
        within the specified tolerances .
        
        x∗ −− is a solution obtained from averaging the last wsize points .
        
        x∗ prev −− is a solution obtained by averaging the wsize points that were wsize ∗( winterval+1) back in history
        
        Intuitively , this function keeps performing steps until ”the objective value” doesn ’ t change much. Be careful
        because it involves calls to afunc . feval that may be slow
        
        """
            
            cal_tol = 1
                while cal_tol > abstol:
                    if self.n < wsize*(winterval+1):
                        self.dostep()
                            else:
                                self.dostep()
                                    #solution by averaging the last wsize points
                                    current_average_solution = self.afunc.feval(scipy.average(scipy.array(self.x_hist[-(wsize):]),axis=0))
                                        #solution by averaging the wsize points that were wsize ∗( winterval+1) back in history
                                        previous_average_solution = self.afunc.feval(scipy.average(scipy.array(self.x_hist[-(wsize)*(winterval+1):-(wsize*winterval)]),axis=0))
                                            cal_tol = previous_average_solution - current_average_solution
                                                #                print "previous_average_solution"
                                                #                print previous_average_solution
                                                #                print "current_average_solution"
                                                #                print current_average_solution
                                                #                print "cal_tol"
                                                #                print cal_tol
                                                
                                                print self.x_hist
                                            #print self.afunc.feval(self.x_hist)

######################################

def plot(self, fname = None, n =100, alphaMult = 1, axis = None):
    
    """
        Produce a plot of the last n SGD steps .
        
        fname −− a file name where to save the plot , or show if None
        
        n −− the number of points to display
        
        alphaMult −− a geometric multiplier on the alpha value of
        the segments, with the most recent one having alpha=1 axis −− the axis on which to plot the steps . ”””
        
        """
            x_hist_array = scipy.array(self.x_hist)
                matplotlib.pyplot.scatter(x_hist_array[:,0],x_hist_array[:,1])
                    zip(x_hist_array[:,0],x_hist_array[:,1])



######################################


alpha=[10,200]
center=[2,1]
afunc=ParabolaDir(alpha,center)
sgd= SGD(afunc, [3,3], sfunc)
sgd.nsteps(200)
sgd.getSoln()

"""
    if len(alpha)==2:
    segment_list=[]
    x_hist_array=scipy.array(sgd.x_hist)
    zipped_points=zip(x_hist_array[:,0],x_hist_array[:,1])
    for i in range(0,len(zipped_points)-1):
    segment_list.append([zipped_points[i],zipped_points[i+1]])
    
    for j in range(0,290,2):
    lines=segment_list[j:j+10]
    c = scipy.array([(0.5,0.5,0.5),(0.4,0.4,0.4),(0.3,0.3,0.3),(0.2,0.2,0.2),(0,0,0)])
    #c=scipy.array([(0.5,0.5,0.5),(0,0,0)])
    lc = collections.LineCollection(lines, colors=c, linewidths=2)
    fig, ax = pylab.subplots()
    pylab.ylim([-10,10])
    pylab.xlim([-10,10])
    ax.add_collection(lc)
    #       ax.autoscale()
    ax.margins(0.1)
    matplotlib.pyplot.savefig(str(j))
    matplotlib.pyplot.clf()
    
    elif len(alpha)==3:
    segment_list=[]
    x_hist_array=scipy.array(sgd.x_hist_aft_proj)
    zipped_points=zip(x_hist_array[:,0],x_hist_array[:,1],x_hist_array[:,2])
    for i in range(0,len(zipped_points)-1):
    segment_list.append([zipped_points[i],zipped_points[i+1]])
    x_hist_array=scipy.array(sgd.x_hist_aft_proj)
    
    for j in range(0,200,5):
    z = x_hist_array[j:j+5,2]
    x = x_hist_array[j:j+5,0]
    y = x_hist_array[j:j+5,1]       
    c = scipy.array([(0.5,0.5,0.5),(0.4,0.4,0.4),(0.3,0.3,0.3),(0.2,0.2,0.2),(0,0,0)])
    fig = matplotlib.pylab.figure()
    ax = fig.gca(projection='3d')   
    ax.set_xlim3d(-5,5)
    ax.set_ylim3d(-5,5)
    ax.set_zlim3d(-5,5)
    ax.plot(x, y, z, label='Graphs')
    matplotlib.pyplot.savefig(str(j))
    """
