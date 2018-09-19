#!/usr/bin/env python
####################################################################
######    BANK  SHOWDOWN    ###############    JULIAN  RICE  #######
####################################################################

#IMPORTING MODULES
from os import system, name
from time import sleep
from random import *

#CONSTANTS
ADDER = 1
STEAL = 2
BLOCK = 3

#CLASS DECLARATION
class Player:
  "Base class for the player"
  def __init__(self, name, history):
    "Initialize a Player object"
    self.name = name
    self.history = history
    self.money = 5
  def currentMoney(self):
    return self.money
  def makeChoice(self, choice):
    "Set Player choice"
    self.choice = choice
  def addMoney(self):
    "Add money to Player"
    self.money += 1
  def stealMoney(self):
    "Steal money and gain 2"
    self.money += 2
  def loseMoney(self):
    "Lose money from getting money stolen"
    self.money -= 2
  def addMoveToHistory(self, move, history):
    "Add previous made move into transaction history"
    self.history.append(move)
  def showName(self):
    "Show a Name: status with the Player name"
    response = "Player: " + self.name
    return response
  def showBalance(self):
    "Show a Balance: status with the Player name"
    response = "Balance: $" + str(self.money)
    return response
  def showHistory(self):
    "Show the complete transaction history for the Player"
    for obj in self.history:
      print(obj)
  def lastHistory(self, times):
    newHistory = []
    for number in range(times):
      tester = -number
      newYatsu = self.history[tester]
      newHistory.append(newYatsu)
    return newHistory

def clear():
    "Clear the screen"
    #Windows (nt)
    if name == 'nt':
        _ = system('cls')
    #Mac/Linux (posix)
    else:
        _ = system('clear')

def title():
  "Title screen is displayed in this function"
  print("$---------$$$$$$$$$$---------$")
  print("$--WELCOME-TO-BANK-SHOWDOWN--$")
  print("$---------$$$$$$$$$$---------$")
  print("$----------------------------$")
  print("$------JULIAN-RICE-2018------$")
  print("$-------[1]-P1-vs-CPU--------$")
  print("$-------[2]-P1-vs-P2---------$")
  print("$----------------------------$")

def printLine():
  "Print a new line of dashes in this function"
  print("------------------------------------")

def instructions(mode):
  "Instructions are played at over time intervals this function"
  print("$---------$$$$$$$$$$---------$")
  print("$--------INSTRUCTIONS--------$")
  print("$---------$$$$$$$$$$---------$")
  if mode == 1:
    print("$--------1-PLAYER-MODE-------$")
  if mode == 2: #mode is 2p
    print("$--------VERSUS-MODE---------$")
  print("$--------------------------------------------$")
  print("$--You have 5$ in your bank and need to get--$")
  print("$--10$. Each turn, you have three potential--$")
  print("$--actions to choose from. Check them out!---$")
  print("$--------------------------------------------$")
  sleep(1.5)
  print("$--[1]: ADD 1 dollar to your balance---------$")
  print("$--[2]: STEAL 2 dollars from your enemy------$")
  print("$--[3]: BLOCK a steal from your enemy--------$")
  print("$--------------------------------------------$")
  sleep(1.5)
  print("$--If you try to STEAL and get BLOCKED by----$")
  print("$--your enemy, YOU LOSE 2 dollars! Careful!--$")
  print("$--First one to get to 10 dollars WINS!------$")
  print("$--------------------------------------------$")

def moveSelection(player):
  "Player can select one of three moves in this function"
  print("$$ Choose an action from below $$")
  print("$$-$$ [1]: ADD 1 dollar to your balance")
  print("$$-$$ [2]: STEAL 2 dollars from the enemy")
  print("$$-$$ [3]: BLOCK a steal from your opponent \n")
  decision = int(input("$$ [Selection] = "))
  if decision > 3 and decision < 1:
    print("> OUT OF RANGE < > CHOOSING [1] <")
    decision = 1
  player.makeChoice(decision)
  player.addMoveToHistory(decision, player.history)
  return decision

def historyMutate(player):
  "1-2-3's get converted into ADD 1, TAKE 2, and BLOCK in this function"
  for index in range(len(player.history)):
    if player.history[index] == 1:
      player.history[index] = "# ADD  1 #"
    elif player.history[index] == 2:
      player.history[index] = "# TAKE 2 #"
    elif player.history[index] == 3:
      player.history[index] = "# BLOCK  #"

def showResults(player1, opponent):
  "The results of the round are displayed in this function"
  printLine()
  print("\n$$-ROUND RESULTS-$$")
  print(player1.showName() + " -> " + player1.showBalance())
  print(opponent.showName() + " -> " + opponent.showBalance())
  historyMutate(player1)
  historyMutate(opponent)
  print(player1.showName() + "'s transaction history!")
  player1.showHistory()
  print(opponent.showName() + "'s transaction history!")
  opponent.showHistory()
  print("$$-WORK HARD, AND WIN!!-$$")

def showdown(player1, opponent, move1, move2):
  "The balance changes are made here between both players in this function"
  if move1 == ADDER:
    player1.addMoney()
  if move2 == ADDER:
    opponent.addMoney()
  if move1 == STEAL and move2 != BLOCK:
    player1.stealMoney()
    opponent.loseMoney()
  if move2 == STEAL and move1 != BLOCK:
    player1.loseMoney()
    opponent.stealMoney()
  if move1 == STEAL and move2 == BLOCK:
    player1.loseMoney()
    opponent.stealMoney()
  if move1 == BLOCK and move2 == STEAL:
    opponent.loseMoney()
    player1.stealMoney()
  showResults(player1, opponent)

def singleplayer(player, computer, mode):
  "General flow for the 1 player mode"
  turn = 1
  while True:
    sleep(turn/1.5) ; clear() ; printLine()
    print("[Turn " + str(turn) + "]   " + player.showName() + "   " + player.showBalance())
    print("Enemy's " + computer.showBalance())
    currentMoveP1 = moveSelection(player)
    moneyDifferential = player.currentMoney() - computer.currentMoney()
    if mode == 1: #EASY
      name = "EASY"
      moveChoice = randint(ADDER, BLOCK)
    elif mode == 2: #NORMAL
      name = "NORMAL"
      if moneyDifferential >= 3:
        moveChoice = randint(STEAL, BLOCK)
      else:
        moveChoiceT = randint(1, 2)
        moveChoice = ADDER if moveChoiceT == 1 else BLOCK
    elif mode == 3: #HARD
      name = "HARD"
      if turn != 1 and turn != 2:
        lHistory = player.lastHistory(2)
        rHistory = computer.lastHistory(2)
        previousMove, beforeThatMove = lHistory[0], lHistory[1]
        compPrev, compBefore = rHistory[0], rHistory[1]
        if player.currentMoney() == 8:
          print(previousMove)
          print(beforeThatMove)
          if previousMove == STEAL and beforeThatMove == STEAL:
            moveChoice = randint(STEAL, BLOCK)
          elif previousMove == BLOCK:
            moveChoice = STEAL
          else:
            moveChoice = BLOCK
        elif player.currentMoney() == 9:
          if compPrev != ADDER:
            moveChoice = randint(ADDER, STEAL)
          else:
            moveChoice = ADDER
        elif moneyDifferential >= 2:
          if compPrev != ADDER and compBefore != ADDER:
            moveChoice = ADDER
          elif previousMove == STEAL:
            moveChoice = randint(STEAL, BLOCK)
          elif beforeThatMove == STEAL:
            moveChoice = BLOCK
          else:
            moveChoice = randint(ADDER, STEAL)
        else:
          moveChoice = randint(STEAL, BLOCK)
      else:
        moveChoice = randint(ADDER, BLOCK)
    computer.addMoveToHistory(moveChoice, computer.history)
    showdown(player, computer, currentMoveP1, moveChoice)
    if player.currentMoney() >= 10 or computer.currentMoney() >= 10:
      break
    turn += 1
  print(player.showName() + "'s FINAL BALANCE: $" + str(player.currentMoney()))
  print(computer.showName() + "'s FINAL BALANCE: $" + str(computer.currentMoney()))
  print("TURNS TAKEN: " + str(turn))
  if (player.money > computer.money):
    print("CONGRATULATIONS, PLAYER 1!! " + player.name)
    print("You managed to beat the " + name + " computer!")
  else:
    print("As expected, " + name + " mode...")
  printLine()

def multiplayer(player1, player2):
  "General flow for the 2 player mode"
  turn = 1
  while True:
    sleep(2.5) ; clear() ; printLine()
    print("[Turn " + str(turn) + "]   " + player1.showName() + "   " + player1.showBalance())
    print("Enemy's " + player2.showBalance())
    currentMoveP1 = moveSelection(player1)
    clear() ; printLine()
    print("[Turn " + str(turn) + "]   " + player2.showName() + "   " + player2.showBalance())
    currentMoveP2 = moveSelection(player2)
    showdown(player1, player2, currentMoveP1, currentMoveP2)
    if player1.money >= 10 or player2.money >= 10:
      break
    turn += 1
  printLine()
  print(player1.showName() + "'s FINAL BALANCE: $" + str(player1.currentMoney()))
  print(player2.showName() + "'s FINAL BALANCE: $" + str(player2.currentMoney()))
  print("TURNS TAKEN: " + str(turn))
  if (player1.currentMoney() > player2.currentMoney()):
    print("CONGRATULATIONS, PLAYER 1!! " + player1.name)
  else:
    print("EXCELLENT FEAT, PLAYER 2!! " + player2.name)
  printLine()

def playGame():
  "General flow for the game when started"
  title()
  mode = int(input("\n$$ Enter a MODE [?]: "))
  instructions(mode)
  p1Name = input("\n$$ Player 1 - Enter your name here: ")
  if mode == 1:
    while True:
      compDiff = input("$$ Choose a difficulty level [HARD] [NORMAL] [EASY]: ")
      if compDiff != "EASY" and compDiff != "NORMAL" and compDiff != "HARD":
        print("You made a typo error! ")
        sleep(2.5)
      else:
        break
  else:
    p2Name = input("$$ Player 2 - Enter your name here: ")
  p1History = []
  p2History = []
  print("Loading...")
  if mode == 1:
    player1 = Player(p1Name, p1History)
    computer = Player("Kuribo", p2History)
    if compDiff == "EASY":
      difficultyMode = 1
    elif compDiff == "NORMAL":
      difficultyMode = 2
    else:
      difficultyMode = 3
    singleplayer(player1, computer, difficultyMode)
  if mode == 2:
    player1 = Player(p1Name, p1History)
    player2 = Player(p2Name, p2History)
    multiplayer(player1, player2)

def main():
  playGame()

main()
