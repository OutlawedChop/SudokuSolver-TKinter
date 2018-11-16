from tkinter import *
from tkinter.messagebox import *
import copy
import time
#showinfo('info','Solution have been found!')
#showwarning('info','3')
#----------------------------------------------------------------------------------------------------------------
class SudokuSolver:
  def SudokuSolverMaim( puzzle ):
    solution = copy.deepcopy( puzzle )
    if SudokuSolver.SolveHelper(solution):
      return solution
    else:
      return False

  def SolveHelper( solution ):
    minpossiblecellvalues = None
    while True:
      minpossiblecellvalues = None
      for rowIndex in range(9):
        for columnIndex in range(9):
          if solution[ rowIndex ][ columnIndex ] != 0:
            continue
          cellpossiblevalues = SudokuSolver.findcellpossiblevalues( solution, rowIndex, columnIndex ) 
          countcellpossiblevalues = len(cellpossiblevalues)
          if countcellpossiblevalues == 0:
            return False
          if countcellpossiblevalues == 1:
            solution [ rowIndex ][ columnIndex ] = cellpossiblevalues.pop()
          if not minpossiblecellvalues  or len( minpossiblecellvalues ) > countcellpossiblevalues :
            minpossiblecellvalues = ( ( rowIndex, columnIndex ) , cellpossiblevalues )
      if not minpossiblecellvalues:
        return True
      elif len( minpossiblecellvalues[1] ) > 1:
        break

    r , c = minpossiblecellvalues[0]
    for var in minpossiblecellvalues[1]:
      solutioncopy = copy.deepcopy( solution )
      solutioncopy[ r ][ c ] = var
      if SudokuSolver.SolveHelper( solutioncopy ):
        for i in range(9):
          for j in range(9):
            solution[ i ][ j ] = solutioncopy[ i ][ j ]
        return True
    return False

  def findcellpossiblevalues(puzzle,rowIndex,columnIndex):
    values = { x for x in range(1,10) }
    values -= SudokuSolver.possiblerowvalues(puzzle,rowIndex)
    values -= SudokuSolver.possiblecolumnvalues(puzzle,columnIndex)
    values -= SudokuSolver.possibleblockvalues(puzzle,rowIndex,columnIndex)
    return values

  def possiblerowvalues(puzzle,rowIndex):
    return set( puzzle [ rowIndex ][ : ] )

  def possiblecolumnvalues(puzzle,columnIndex):
    return { puzzle [ x ][ columnIndex ] for x in range(9) }

  def possibleblockvalues(puzzle,rowIndex,columnIndex):
    startrowIndex = 3 * ( rowIndex // 3 )
    startcolumnIndex = 3 * ( columnIndex // 3 )
    return { puzzle [ startrowIndex + r ][ startcolumnIndex + c ]
    for r in range(3)
    for c in range(3) 
    }

def printpuzzle(puzzle):
  for x in range( len(puzzle) ):
    print( puzzle[x] )
#----------------------------------------------------------------------------------------------------------------  
def check(puzzle):
    
    for i in range(9):
        m1=[]
        for j in range(9):
            if puzzle[i][j]!=0: 
                if puzzle[i][j] not in m1:
                    m1.append(puzzle[i][j])
                else:
                    return False
    for i in range(9):
        m2=[]
        for j in range(9):
            if puzzle[j][i]!=0:
                if puzzle[j][i] not in m2:
                    m2.append(puzzle[j][i])
                else:
                    return False
                
    m3=[];m4=[];m5=[]
    count1=0;count2=0;count3=0
    for i in range(9):
        for j in range(9):
          if j>=0 and j<=2:
              count1+=1
              if puzzle[i][j]!=0:
                  if puzzle[i][j] not in m3:
                      m3.append(puzzle[i][j])
                  else:
                      print(m3,1)
                      return False
              if count1%9==0:
                  m3=[]
                  
          if j>=3 and j<=5:
              count2+=1
              if puzzle[i][j]!=0:
                  if puzzle[i][j] not in m4:
                      m4.append(puzzle[i][j])
                  else:
                      print(m4,2)
                      return False
              if count2%9==0:
                  m4=[]
                  
          if j>=6 and j<=8:
              count3+=1
              if puzzle[i][j]!=0:
                  if puzzle[i][j] not in m5:
                      m5.append(puzzle[i][j])
                  else:
                      print(m5,3)
                      return False
              if count3%9==0:
                  m5=[]
    return True

        
#----------------------------------------------------------------------------------------------------------------


root = Tk()
root.geometry("600x450+330+100")
root.title('Sudoku solver')
puzzlezero = [
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
]

puzzle=copy.deepcopy(puzzlezero)
puzzzlecurrent=copy.deepcopy(puzzlezero)

def lim(event,cell,numb):
    cell['fg']=color2
    count=0
    if len(cell.get())==0:
        for i in range(9):
            for j in range(9):
                count+=1
                if count==numb:
                    puzzle[i][j]=0
                    print(puzzle)
                    
    if not cell.get().isdigit():
        cell.delete('0',END)
        return None
    
    if len(cell.get())>1:
        s=cell.get()[-1]
        cell.delete('0',END)
        cell.insert(0,s)
        
    count=0
    for i in range(9):
        for j in range(9):
            count+=1
            if count==numb:
                puzzle[i][j]=int(cell.get())
                print(puzzle)
        
color1='#FFE4B5'
color2='red'
allfont='Arial'
bord=1

#frame1=Frame(root,bg='brown')
#frame1.place(x = 0, y = 0, width = 1000, heigh = 1000)

cell1=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell2=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell3=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell4=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell5=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell6=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell7=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell8=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell9=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell10=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell11=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell12=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell13=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell14=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell15=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell16=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell17=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell18=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell19=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell20=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell21=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell22=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell23=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell24=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell25=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell26=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell27=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell28=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell29=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell30=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell31=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell32=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell33=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell34=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell35=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell36=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell37=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell38=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell39=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell40=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell41=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell42=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell43=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell44=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell45=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell46=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell47=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell48=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell49=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell50=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell51=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell52=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell53=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell54=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell55=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell56=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell57=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell58=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell59=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell60=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell61=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell62=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell63=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell64=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell65=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell66=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell67=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell68=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell69=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell70=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell71=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell72=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell73=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell74=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell75=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell76=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell77=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell78=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell79=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell80=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')
cell81=Entry(root,bg=color1, borderwidth=bord,fg=color2,font=allfont,justify='center')

cell1.bind('<KeyRelease>',lambda event=0,cell=cell1,numb=1: lim(event,cell,numb))
cell2.bind('<KeyRelease>',lambda event=0,cell=cell2,numb=2: lim(event,cell,numb))
cell3.bind('<KeyRelease>',lambda event=0,cell=cell3,numb=3: lim(event,cell,numb))
cell4.bind('<KeyRelease>',lambda event=0,cell=cell4,numb=4: lim(event,cell,numb))
cell5.bind('<KeyRelease>',lambda event=0,cell=cell5,numb=5: lim(event,cell,numb))
cell6.bind('<KeyRelease>',lambda event=0,cell=cell6,numb=6: lim(event,cell,numb))
cell7.bind('<KeyRelease>',lambda event=0,cell=cell7,numb=7: lim(event,cell,numb))
cell8.bind('<KeyRelease>',lambda event=0,cell=cell8,numb=8: lim(event,cell,numb))
cell9.bind('<KeyRelease>',lambda event=0,cell=cell9,numb=9: lim(event,cell,numb))
cell10.bind('<KeyRelease>',lambda event=0,cell=cell10,numb=10: lim(event,cell,numb))
cell11.bind('<KeyRelease>',lambda event=0,cell=cell11,numb=11: lim(event,cell,numb))
cell12.bind('<KeyRelease>',lambda event=0,cell=cell12,numb=12: lim(event,cell,numb))
cell13.bind('<KeyRelease>',lambda event=0,cell=cell13,numb=13: lim(event,cell,numb))
cell14.bind('<KeyRelease>',lambda event=0,cell=cell14,numb=14: lim(event,cell,numb))
cell15.bind('<KeyRelease>',lambda event=0,cell=cell15,numb=15: lim(event,cell,numb))
cell16.bind('<KeyRelease>',lambda event=0,cell=cell16,numb=16: lim(event,cell,numb))
cell17.bind('<KeyRelease>',lambda event=0,cell=cell17,numb=17: lim(event,cell,numb))
cell18.bind('<KeyRelease>',lambda event=0,cell=cell18,numb=18: lim(event,cell,numb))
cell19.bind('<KeyRelease>',lambda event=0,cell=cell19,numb=19: lim(event,cell,numb))
cell20.bind('<KeyRelease>',lambda event=0,cell=cell20,numb=20: lim(event,cell,numb))
cell21.bind('<KeyRelease>',lambda event=0,cell=cell21,numb=21: lim(event,cell,numb))
cell22.bind('<KeyRelease>',lambda event=0,cell=cell22,numb=22: lim(event,cell,numb))
cell23.bind('<KeyRelease>',lambda event=0,cell=cell23,numb=23: lim(event,cell,numb))
cell24.bind('<KeyRelease>',lambda event=0,cell=cell24,numb=24: lim(event,cell,numb))
cell25.bind('<KeyRelease>',lambda event=0,cell=cell25,numb=25: lim(event,cell,numb))
cell26.bind('<KeyRelease>',lambda event=0,cell=cell26,numb=26: lim(event,cell,numb))
cell27.bind('<KeyRelease>',lambda event=0,cell=cell27,numb=27: lim(event,cell,numb))
cell28.bind('<KeyRelease>',lambda event=0,cell=cell28,numb=28: lim(event,cell,numb))
cell29.bind('<KeyRelease>',lambda event=0,cell=cell29,numb=29: lim(event,cell,numb))
cell30.bind('<KeyRelease>',lambda event=0,cell=cell30,numb=30: lim(event,cell,numb))
cell31.bind('<KeyRelease>',lambda event=0,cell=cell31,numb=31: lim(event,cell,numb))
cell32.bind('<KeyRelease>',lambda event=0,cell=cell32,numb=32: lim(event,cell,numb))
cell33.bind('<KeyRelease>',lambda event=0,cell=cell33,numb=33: lim(event,cell,numb))
cell34.bind('<KeyRelease>',lambda event=0,cell=cell34,numb=34: lim(event,cell,numb))
cell35.bind('<KeyRelease>',lambda event=0,cell=cell35,numb=35: lim(event,cell,numb))
cell36.bind('<KeyRelease>',lambda event=0,cell=cell36,numb=36: lim(event,cell,numb))
cell37.bind('<KeyRelease>',lambda event=0,cell=cell37,numb=37: lim(event,cell,numb))
cell38.bind('<KeyRelease>',lambda event=0,cell=cell38,numb=38: lim(event,cell,numb))
cell39.bind('<KeyRelease>',lambda event=0,cell=cell39,numb=39: lim(event,cell,numb))
cell40.bind('<KeyRelease>',lambda event=0,cell=cell40,numb=40: lim(event,cell,numb))
cell41.bind('<KeyRelease>',lambda event=0,cell=cell41,numb=41: lim(event,cell,numb))
cell42.bind('<KeyRelease>',lambda event=0,cell=cell42,numb=42: lim(event,cell,numb))
cell43.bind('<KeyRelease>',lambda event=0,cell=cell43,numb=43: lim(event,cell,numb))
cell44.bind('<KeyRelease>',lambda event=0,cell=cell44,numb=44: lim(event,cell,numb))
cell45.bind('<KeyRelease>',lambda event=0,cell=cell45,numb=45: lim(event,cell,numb))
cell46.bind('<KeyRelease>',lambda event=0,cell=cell46,numb=46: lim(event,cell,numb))
cell47.bind('<KeyRelease>',lambda event=0,cell=cell47,numb=47: lim(event,cell,numb))
cell48.bind('<KeyRelease>',lambda event=0,cell=cell48,numb=48: lim(event,cell,numb))
cell49.bind('<KeyRelease>',lambda event=0,cell=cell49,numb=49: lim(event,cell,numb))
cell50.bind('<KeyRelease>',lambda event=0,cell=cell50,numb=50: lim(event,cell,numb))
cell51.bind('<KeyRelease>',lambda event=0,cell=cell51,numb=51: lim(event,cell,numb))
cell52.bind('<KeyRelease>',lambda event=0,cell=cell52,numb=52: lim(event,cell,numb))
cell53.bind('<KeyRelease>',lambda event=0,cell=cell53,numb=53: lim(event,cell,numb))
cell54.bind('<KeyRelease>',lambda event=0,cell=cell54,numb=54: lim(event,cell,numb))
cell55.bind('<KeyRelease>',lambda event=0,cell=cell55,numb=55: lim(event,cell,numb))
cell56.bind('<KeyRelease>',lambda event=0,cell=cell56,numb=56: lim(event,cell,numb))
cell57.bind('<KeyRelease>',lambda event=0,cell=cell57,numb=57: lim(event,cell,numb))
cell58.bind('<KeyRelease>',lambda event=0,cell=cell58,numb=58: lim(event,cell,numb))
cell59.bind('<KeyRelease>',lambda event=0,cell=cell59,numb=59: lim(event,cell,numb))
cell60.bind('<KeyRelease>',lambda event=0,cell=cell60,numb=60: lim(event,cell,numb))
cell61.bind('<KeyRelease>',lambda event=0,cell=cell61,numb=61: lim(event,cell,numb))
cell62.bind('<KeyRelease>',lambda event=0,cell=cell62,numb=62: lim(event,cell,numb))
cell63.bind('<KeyRelease>',lambda event=0,cell=cell63,numb=63: lim(event,cell,numb))
cell64.bind('<KeyRelease>',lambda event=0,cell=cell64,numb=64: lim(event,cell,numb))
cell65.bind('<KeyRelease>',lambda event=0,cell=cell65,numb=65: lim(event,cell,numb))
cell66.bind('<KeyRelease>',lambda event=0,cell=cell66,numb=66: lim(event,cell,numb))
cell67.bind('<KeyRelease>',lambda event=0,cell=cell67,numb=67: lim(event,cell,numb))
cell68.bind('<KeyRelease>',lambda event=0,cell=cell68,numb=68: lim(event,cell,numb))
cell69.bind('<KeyRelease>',lambda event=0,cell=cell69,numb=69: lim(event,cell,numb))
cell70.bind('<KeyRelease>',lambda event=0,cell=cell70,numb=70: lim(event,cell,numb))
cell71.bind('<KeyRelease>',lambda event=0,cell=cell71,numb=71: lim(event,cell,numb))
cell72.bind('<KeyRelease>',lambda event=0,cell=cell72,numb=72: lim(event,cell,numb))
cell73.bind('<KeyRelease>',lambda event=0,cell=cell73,numb=73: lim(event,cell,numb))
cell74.bind('<KeyRelease>',lambda event=0,cell=cell74,numb=74: lim(event,cell,numb))
cell75.bind('<KeyRelease>',lambda event=0,cell=cell75,numb=75: lim(event,cell,numb))
cell76.bind('<KeyRelease>',lambda event=0,cell=cell76,numb=76: lim(event,cell,numb))
cell77.bind('<KeyRelease>',lambda event=0,cell=cell77,numb=77: lim(event,cell,numb))
cell78.bind('<KeyRelease>',lambda event=0,cell=cell78,numb=78: lim(event,cell,numb))
cell79.bind('<KeyRelease>',lambda event=0,cell=cell79,numb=79: lim(event,cell,numb))
cell80.bind('<KeyRelease>',lambda event=0,cell=cell80,numb=80: lim(event,cell,numb))
cell81.bind('<KeyRelease>',lambda event=0,cell=cell81,numb=81: lim(event,cell,numb))

cell1.place(x = 10, y = 10,width=40,heigh=40)
cell2.place(x = 50, y = 10,width=40,heigh=40)                              
cell3.place(x = 90, y = 10,width=40,heigh=40)
cell4.place(x = 145, y = 10,width=40,heigh=40)
cell5.place(x = 185, y = 10,width=40,heigh=40)
cell6.place(x = 225, y = 10,width=40,heigh=40)
cell7.place(x = 280, y = 10,width=40,heigh=40)
cell8.place(x = 320, y = 10,width=40,heigh=40)
cell9.place(x = 360, y = 10,width=40,heigh=40)
cell10.place(x = 10, y = 50,width=40,heigh=40)
cell11.place(x = 50, y = 50,width=40,heigh=40)                              
cell12.place(x = 90, y = 50,width=40,heigh=40)
cell13.place(x = 145, y = 50,width=40,heigh=40)
cell14.place(x = 185, y = 50,width=40,heigh=40)
cell15.place(x = 225, y = 50,width=40,heigh=40)
cell16.place(x = 280, y = 50,width=40,heigh=40)
cell17.place(x = 320, y = 50,width=40,heigh=40)
cell18.place(x = 360, y = 50,width=40,heigh=40)
cell19.place(x = 10, y = 90,width=40,heigh=40)
cell20.place(x = 50, y = 90,width=40,heigh=40)                              
cell21.place(x = 90, y = 90,width=40,heigh=40)
cell22.place(x = 145, y = 90,width=40,heigh=40)
cell23.place(x = 185, y = 90,width=40,heigh=40)
cell24.place(x = 225, y = 90,width=40,heigh=40)
cell25.place(x = 280, y = 90,width=40,heigh=40)
cell26.place(x = 320, y = 90,width=40,heigh=40)
cell27.place(x = 360, y = 90,width=40,heigh=40)
cell28.place(x = 10, y = 145,width=40,heigh=40)
cell29.place(x = 50, y = 145,width=40,heigh=40)                              
cell30.place(x = 90, y = 145,width=40,heigh=40)
cell31.place(x = 145, y = 145,width=40,heigh=40)
cell32.place(x = 185, y = 145,width=40,heigh=40)
cell33.place(x = 225, y = 145,width=40,heigh=40)
cell34.place(x = 280, y = 145,width=40,heigh=40)
cell35.place(x = 320, y = 145,width=40,heigh=40)
cell36.place(x = 360, y = 145,width=40,heigh=40)
cell37.place(x = 10, y = 185,width=40,heigh=40)
cell38.place(x = 50, y = 185,width=40,heigh=40)                              
cell39.place(x = 90, y = 185,width=40,heigh=40)
cell40.place(x = 145, y = 185,width=40,heigh=40)
cell41.place(x = 185, y = 185,width=40,heigh=40)
cell42.place(x = 225, y = 185,width=40,heigh=40)
cell43.place(x = 280, y = 185,width=40,heigh=40)
cell44.place(x = 320, y = 185,width=40,heigh=40)
cell45.place(x = 360, y = 185,width=40,heigh=40)
cell46.place(x = 10, y = 225,width=40,heigh=40)
cell47.place(x = 50, y = 225,width=40,heigh=40)                              
cell48.place(x = 90, y = 225,width=40,heigh=40)
cell49.place(x = 145, y = 225,width=40,heigh=40)
cell50.place(x = 185, y = 225,width=40,heigh=40)
cell51.place(x = 225, y = 225,width=40,heigh=40)
cell52.place(x = 280, y = 225,width=40,heigh=40)
cell53.place(x = 320, y = 225,width=40,heigh=40)
cell54.place(x = 360, y = 225,width=40,heigh=40)
cell55.place(x = 10, y = 280,width=40,heigh=40)
cell56.place(x = 50, y = 280,width=40,heigh=40)                              
cell57.place(x = 90, y = 280,width=40,heigh=40)
cell58.place(x = 145, y = 280,width=40,heigh=40)
cell59.place(x = 185, y = 280,width=40,heigh=40)
cell60.place(x = 225, y = 280,width=40,heigh=40)
cell61.place(x = 280, y = 280,width=40,heigh=40)
cell62.place(x = 320, y = 280,width=40,heigh=40)
cell63.place(x = 360, y = 280,width=40,heigh=40)
cell64.place(x = 10, y = 320,width=40,heigh=40)
cell65.place(x = 50, y = 320,width=40,heigh=40)                              
cell66.place(x = 90, y = 320,width=40,heigh=40)
cell67.place(x = 145, y = 320,width=40,heigh=40)
cell68.place(x = 185, y = 320,width=40,heigh=40)
cell69.place(x = 225, y = 320,width=40,heigh=40)
cell70.place(x = 280, y = 320,width=40,heigh=40)
cell71.place(x = 320, y = 320,width=40,heigh=40)
cell72.place(x = 360, y = 320,width=40,heigh=40)
cell73.place(x = 10, y = 360,width=40,heigh=40)
cell74.place(x = 50, y = 360,width=40,heigh=40)                              
cell75.place(x = 90, y = 360,width=40,heigh=40)
cell76.place(x = 145, y = 360,width=40,heigh=40)
cell77.place(x = 185, y = 360,width=40,heigh=40)
cell78.place(x = 225, y = 360,width=40,heigh=40)
cell79.place(x = 280, y = 360,width=40,heigh=40)
cell80.place(x = 320, y = 360,width=40,heigh=40)
cell81.place(x = 360, y = 360,width=40,heigh=40)




def clearall(event,puzzle):
    lable1['text']='Time: 00:00'
    for i in range(9):
        for j in range(9):
            puzzle[i][j]=0
    cell1.delete('0',END);cell29.delete('0',END);cell57.delete('0',END);
    cell2.delete('0',END);cell30.delete('0',END);cell58.delete('0',END)
    cell3.delete('0',END);cell31.delete('0',END);cell59.delete('0',END)
    cell4.delete('0',END);cell32.delete('0',END);cell60.delete('0',END)
    cell5.delete('0',END);cell33.delete('0',END);cell61.delete('0',END)
    cell6.delete('0',END);cell34.delete('0',END);cell62.delete('0',END)
    cell7.delete('0',END);cell35.delete('0',END);cell63.delete('0',END)
    cell8.delete('0',END);cell36.delete('0',END);cell64.delete('0',END)
    cell9.delete('0',END);cell37.delete('0',END);cell65.delete('0',END)
    cell10.delete('0',END);cell38.delete('0',END);cell66.delete('0',END)
    cell11.delete('0',END);cell39.delete('0',END);cell67.delete('0',END)
    cell12.delete('0',END);cell40.delete('0',END);cell68.delete('0',END)
    cell13.delete('0',END);cell41.delete('0',END);cell69.delete('0',END)
    cell14.delete('0',END);cell42.delete('0',END);cell70.delete('0',END)
    cell15.delete('0',END);cell43.delete('0',END);cell71.delete('0',END)
    cell16.delete('0',END);cell44.delete('0',END);cell72.delete('0',END)
    cell17.delete('0',END);cell45.delete('0',END);cell73.delete('0',END)
    cell18.delete('0',END);cell46.delete('0',END);cell74.delete('0',END)
    cell19.delete('0',END);cell47.delete('0',END);cell75.delete('0',END)
    cell20.delete('0',END);cell48.delete('0',END);cell76.delete('0',END)
    cell21.delete('0',END);cell49.delete('0',END);cell77.delete('0',END)
    cell22.delete('0',END);cell50.delete('0',END);cell78.delete('0',END)
    cell23.delete('0',END);cell51.delete('0',END);cell79.delete('0',END)
    cell24.delete('0',END);cell52.delete('0',END);cell80.delete('0',END)
    cell25.delete('0',END);cell53.delete('0',END);cell81.delete('0',END)
    cell26.delete('0',END);cell54.delete('0',END);
    cell27.delete('0',END);cell55.delete('0',END);
    cell28.delete('0',END);cell56.delete('0',END);
    printpuzzle( puzzle )
    return puzzle
def fill(sell,x,y,solution):
    if len(sell.get())==1:
        pass
    else:
        sell['fg']='black'
        sell.insert(0,solution[x][y])

def solve(event,puzzle):
    printpuzzle( puzzle )
    if check(puzzle)==False:
        print('Nope')
        showerror('Error','You entered incorrect information!')
        return None
    print()
    
    startTime = time.clock()
    solution = SudokuSolver.SudokuSolverMaim( puzzle )
    if solution:
      printpuzzle( solution )


    print()
    lable1['text'] = 'Time: {}'.format(round(time.clock() - startTime,4))
    print( time.clock() - startTime, "sec" )
    
    fill(cell1,0,0,solution);fill(cell28,3,0,solution);fill(cell55,6,0,solution)
    fill(cell2,0,1,solution);fill(cell29,3,1,solution);fill(cell56,6,1,solution)
    fill(cell3,0,2,solution);fill(cell30,3,2,solution);fill(cell57,6,2,solution)
    fill(cell4,0,3,solution);fill(cell31,3,3,solution);fill(cell58,6,3,solution)
    fill(cell5,0,4,solution);fill(cell32,3,4,solution);fill(cell59,6,4,solution)
    fill(cell6,0,5,solution);fill(cell33,3,5,solution);fill(cell60,6,5,solution)
    fill(cell7,0,6,solution);fill(cell34,3,6,solution);fill(cell61,6,6,solution)
    fill(cell8,0,7,solution);fill(cell35,3,7,solution);fill(cell62,6,7,solution)
    fill(cell9,0,8,solution);fill(cell36,3,8,solution);fill(cell63,6,8,solution)
    fill(cell10,1,0,solution);fill(cell37,4,0,solution);fill(cell64,7,0,solution)
    fill(cell11,1,1,solution);fill(cell38,4,1,solution);fill(cell65,7,1,solution)
    fill(cell12,1,2,solution);fill(cell39,4,2,solution);fill(cell66,7,2,solution)
    fill(cell13,1,3,solution);fill(cell40,4,3,solution);fill(cell67,7,3,solution)
    fill(cell14,1,4,solution);fill(cell41,4,4,solution);fill(cell68,7,4,solution)
    fill(cell15,1,5,solution);fill(cell42,4,5,solution);fill(cell69,7,5,solution)
    fill(cell16,1,6,solution);fill(cell43,4,6,solution);fill(cell70,7,6,solution)
    fill(cell17,1,7,solution);fill(cell44,4,7,solution);fill(cell71,7,7,solution)
    fill(cell18,1,8,solution);fill(cell45,4,8,solution);fill(cell72,7,8,solution)
    fill(cell19,2,0,solution);fill(cell46,5,0,solution);fill(cell73,8,0,solution)
    fill(cell20,2,1,solution);fill(cell47,5,1,solution);fill(cell74,8,1,solution)
    fill(cell21,2,2,solution);fill(cell48,5,2,solution);fill(cell75,8,2,solution)
    fill(cell22,2,3,solution);fill(cell49,5,3,solution);fill(cell76,8,3,solution)
    fill(cell23,2,4,solution);fill(cell50,5,4,solution);fill(cell77,8,4,solution)
    fill(cell24,2,5,solution);fill(cell51,5,5,solution);fill(cell78,8,5,solution)
    fill(cell25,2,6,solution);fill(cell52,5,6,solution);fill(cell79,8,6,solution)
    fill(cell26,2,7,solution);fill(cell53,5,7,solution);fill(cell80,8,7,solution)
    fill(cell27,2,8,solution);fill(cell54,5,8,solution);fill(cell81,8,8,solution)
    showinfo('info','Solution have been found!')

    
button1=Button(root,text='Clear')
button1.bind('<Button-1>',lambda event=0: clearall(event,puzzle))
button1.place(x = 450, y = 140,width=120,heigh=60)

button2=Button(root,text='Solve',command=lambda event=0: solve(event,puzzle))
#button2.bind('<Button-1>',lambda event=0: solve(event,puzzle))
button2.place(x = 450, y = 210,width=120,heigh=60)

lable1 = Label(root,text='Time: 00:00')
lable1.place(x=460,y=285,width=100,heigh=10)

root.mainloop()





