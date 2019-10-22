using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Player : MonoBehaviour
{
    public string name;
    public List<Move> history;
    public int money = 5;

    // Start is called before the first frame update
    void Start()
    {
        history = new List<Move>();
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}


/*
class Player:
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
    index = 1
    if len(self.history) > 5:
      print("".join(self.history[-5:]))
      index += 1
    else:
      print("".join(self.history))
  def lastHistory(self, times):
    newHistory = []
    for number in range(times):
      tester = -number
      newYatsu = self.history[tester]
      newHistory.append(newYatsu)
    return newHistory
*/