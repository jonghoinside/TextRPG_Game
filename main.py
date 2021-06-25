# 몬스터 리스트
monsterList = {
  #이름, HP, 공격력, 경험치, 행운
  1: [["슬라임", 40, 45, 50, 0]],
  2: [["너구리", 54, 52, 15, 20], ["여우", 61, 50, 20, 11], ["늑대", 70, 81, 28, 18]],
  3: [["고블린", 75, 84, 39, 30], ["고블린 마법사", 78, 91, 46, 30], ["고블린 전사", 81, 88, 67, 30], ["사나운 늑대", 91, 92, 50, 20]],
  4: [["그리즐리 베어", 100, 100, 31, 14]]
}

expList = [100, 200, 300, 400]
hpList = [100, 200, 300, 400]
hitList = [20, 25, 30, 35]
lukList = [10, 20, 30, 40]

player = 'jongho inside'
level = 1
curHp = hpList[level-1]
monster = list()
monsterCurHp = 0
curExp = 0

attackAva = False
recoveryAva = False
runAva = False

# main
from random import *
from time import *
from tkinter import *
from tkinter.font import *

def playerUpdate():
  playerLevel = Label(w, text='레벨 : ' + str(level), fg='black', font=sf)
  playerHp = Label(w, text='체력 : ' + str(curHp) + '/' + str(hpList[level - 1]), fg='black', font=sf)
  playerExp = Label(w, text='경험치 : ' + str(curExp) + '/' + str(expList[level - 1]), fg='black', font=sf)

  playerLevel.grid(row=1, column=0, padx=20, pady=10)
  playerHp.grid(row=1, column=1, padx=0, pady=10)
  playerExp.grid(row=1, column=2, padx=0, pady=10)

def monsterUpdate():
  global monsterName, monsterHp
  monsterName = Label(w, text=monster[0], fg='black', font=f1)
  monsterHp = Label(w, text='체력 : ' + str(monsterCurHp) + '/' + str(monster[1]), fg='black', font=sf)

  monsterName.grid(row=2, column=0)
  monsterHp.grid(row=2, column=2)

def monsterDelete():
  global monsterName, monsterHp
  monsterName = Label(w, text='??????', fg='black', font=f1)
  monsterHp = Label(w, text='체력 : ?????/?????', fg='black', font=sf)

  monsterName.grid(row=2, column=0)
  monsterHp.grid(row=2, column=2)

  monsterName.grid_remove()
  monsterHp.grid_remove()


def levelUpDown(num):
  global level, curHp, curExp, runAva
  if num > 0:
    curExp = 0
    level += 1
    curHp = hpList[level - 1]
    runAva = True
    run(1)

  else:
    curExp = 0
    level -= 1
    curHp = hpList[level - 1]
    runAva = True
    run(2)

def fight():
  global curHp, attackAva, recoveryAva
  curHp -= monster[2]
  if curHp <= 0:
    curHp = 0
    playerUpdate()
    w.update()
    w.after(1000, wPrint('몬스터에 의해 사망했습니다.'))
    w.update()
    w.after(1000, wPrint('경험치가 낮아집니다.'))
    subExp()
    playerUpdate()
  else:
    w.update()
    w.after(1000, wPrint('몬스터가 플레이어를 공격했습니다.'))
    playerUpdate()

    w.update()
    w.after(1000, wPrint('inside 님의 공격 차례입니다.'))
    attackAva = True
    recoveryAva = True

def subExp():
  global curExp
  curExp -= monster[3]
  if curExp <= 0:
    levelUpDown(0)


def addExp():
  global curExp, runAva
  curExp += monster[3]
  if curExp >= expList[level-1]:
    levelUpDown(1)
  else:
    runAva = True
    run(0)

  w.update()
  playerUpdate()

def attack():
  global attackAva, recoveryAva, runAva, monsterCurHp
  if attackAva:
    attackAva = False
    recoveryAva = False
    runAva = False
    if monsterCurHp < hitList[level]:
      monsterCurHp = 0
      monsterUpdate()
      w.update()
      w.after(1000, wPrint('적을 처치했습니다.'))

      w.update()
      w.after(1000, wPrint('경험치가 올랐습니다.'))
      addExp()
      monster.clear()
    else:
      monsterCurHp -= hitList[level]
      monsterUpdate()
      w.update()
      w.after(1000, wPrint('inside님의 공격이 들어갔습니다.'))
      fight()

def recovery():
  global attackAva, runAva, recoveryAva, curHp
  if recoveryAva:
    attackAva = False
    runAva = False
    recoveryAva = False
    if curHp < hpList[level - 1]:
      curHp += 30
    else:
      curHp = hpList[level - 1]

    playerUpdate()
    w.update()
    w.after(1000, wPrint('inside님의 체력이 회복되었습니다.'))

    fight()

  return 0


def run(n):
  global attackAva, recoveryAva, runAva

  if runAva:
    runAva = False
    attackAva = False
    recoveryAva = False

    btnAttack.grid_remove()
    btnRecovery.grid_remove()
    btnRun.grid_remove()
    result.grid_remove()

    monsterDelete()

    btnEnter.grid(row=4, column=0, padx=20, pady=10)
    btnPotion.grid(row=4, column=2, padx=20, pady=10)

    if n == 1:
      monsterDelete()
      w.update()
      w.after(500, wPrint('inside님의 레벨이 올랐습니다.'))
      result.grid(row=5, column=1, padx=20, pady=10)
    elif n == 2:
      monsterDelete()
      w.update()
      w.after(500, wPrint('inside님의 레벨이 떨어졌습니다.'))
      result.grid(row=5, column=1, padx=20, pady=10)

def enter():
  btnEnter.grid_remove()
  btnPotion.grid_remove()

  btnAttack.grid(row=3, column=0, padx=20, pady=10)
  btnRecovery.grid(row=3, column=1, padx=20, pady=10)
  btnRun.grid(row=3, column=2, padx=20, pady=10)
  result.grid(row=5, column=1, padx=20, pady=10)

  result.config(text='던전에 입장하셨습니다.')
  w.after(randint(1000,2000), gameStart)

def monsterCreate():
  return monsterList[level][randint(1, len(monsterList[level]))-1]

def gameStart():
  global attackAva, recoveryAva, runAva, monsterName, monsterHp, monster, monsterCurHp
  attackAva = True
  recoveryAva = True
  runAva = True

  monster = monsterCreate().copy()
  monsterCurHp = monster[1]

  monsterName = Label(w, text=monster[0], fg='black', font=f1)
  monsterHp = Label(w, text='체력 : ' + str(monsterCurHp) + '/' + str(monster[1]), fg='black', font=sf)

  monsterName.grid(row=2, column=0)
  monsterHp.grid(row=2, column=2)

  result.config(text='야생의 ' + monster[0] + '이(가) 나타났습니다.\n먼저 공격하세요.')


def potion():
  global curHp
  curHp = hpList[level - 1]

  w.update()
  w.after(500, wPrint('inside님의 체력이 회복되었습니다.'))
  playerUpdate()
  result.grid(row=5, column=1, padx=20, pady=10)

def wPrint(str):
  result.config(text=str)

w = Tk()    # 윈도우 생성
w.title('Welcome to jongho inside DUNGEON')
bf = Font(family='맑은 고딕', size=15)
sf = Font(family='맑은 고딕', size=10)
f1 = Font(family='맑은 고딕', size=10, weight='bold')

# 화면 출력할 Player Info
playerName = Label(w, text=player, fg='black', font=bf)
playerLevel = Label(w, text='레벨 : ' + str(level), fg='black', font=sf)
playerHp = Label(w, text='체력 : ' + str(curHp) + '/' + str(hpList[level - 1]), fg='black', font=sf)
playerExp = Label(w, text='경험치 : ' + str(curExp) + '/' + str(expList[level-1]), fg='black', font=sf)
monsterName = Label(w, text='', fg='black', font=f1)
monsterHp = Label(w, text='', fg='black', font=sf)

# 버튼 Info
btnEnter = Button(w, text='던전 입장', command=enter, font=sf)
btnPotion = Button(w, text='Potion(물약)', command=potion, font=sf)
btnAttack = Button(w, text='공격', command=attack, font=sf)
btnRecovery = Button(w, text='회복', command=recovery, font=sf)
btnRun = Button(w, text='도망', command=run, font=sf)

# text 창 출력
result = Label(w, text='', font='TkFixedFont')

# window 상에 배치
playerName.grid(row=0, column=1, padx=20, pady=10)
playerLevel.grid(row=1, column=0, padx=20, pady=10)
playerHp.grid(row=1, column=1, padx=0, pady=10)
playerExp.grid(row=1, column=2, padx=0, pady=10)

btnEnter.grid(row=4, column=0, padx=20, pady=10)
btnPotion.grid(row=4, column=2, padx=20, pady=10)

result.grid(row=5, column=1, padx=20, pady=10)

w.geometry('600x300')

w.mainloop()
