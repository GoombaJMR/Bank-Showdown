using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Player : MonoBehaviour
{
    private string name;
    private List<Move> history;
    private int money = 5;
    private SpriteRenderer spr;

    // Start is called before the first frame update
    void Start()
    {
        history = new List<Move>();
        spr = GetComponent<SpriteRenderer>();
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    public void AddMoveToHistory(Move move) {
        history.Add(move);
    }

    public int CurrentBalance() {
        return money;
    }

    public void StealMoney(int value) {
        money += value;
    }

    public void AddMoney(int value) {
        money += value;
    }

    public void MoneyStolen(int value) {
        money -= value;
    }

    public string GetName() {
        return name;
    }

    public List<Move> ReturnMoveHistory() {
        return history;
    }

    public void SetPlayerSprite(Sprite sprite) {
        spr.sprite = sprite;
    }
}


/*
class Player:
  def makeChoice(self, choice):
    "Set Player choice"
    self.choice = choice
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