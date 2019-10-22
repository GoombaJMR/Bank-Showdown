using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class GameController : MonoBehaviour
{
    public Player p1;
    public Player p2;

    private int mode = 0;
    private bool player1Turn = true;
    private bool chosen;

    private Move[] options;
    private Move selected;
    private int counter;

    private const int STEAL = 0;
    private const int ADD = 1;
    private const int BLOCK = 2;

    // Start is called before the first frame update
    void Start()
    {
        options = new Move[3];
        options[STEAL] = GameObject.Find("Options").transform.GetChild(STEAL).gameObject.GetComponent<Move>();
        options[ADD] = GameObject.Find("Options").transform.GetChild(ADD).gameObject.GetComponent<Move>();
        options[BLOCK] = GameObject.Find("Options").transform.GetChild(BLOCK).gameObject.GetComponent<Move>();

        selected = options[STEAL];
    }

    // Update is called once per frame
    void Update()
    {
        if (player1Turn && !chosen) {
            Debug.Log("Currently selected: " + selected.name);

            bool left = Input.GetKeyDown(KeyCode.LeftArrow);
            bool right = Input.GetKeyDown(KeyCode.RightArrow);
            bool choose = Input.GetKeyDown(KeyCode.Return);

            if (left || right) {
                selected.SetInactive();
                if (left) {
                    if (counter-1 < 0) {
                        counter = BLOCK;
                    } else {
                        counter--;
                    }
                }

                if (right) {
                    if (counter+1 > 2) {
                        counter = STEAL;
                    } else {
                        counter++;
                    }
                }
            }
            selected = options[counter];
            selected.SetActive();
        }
    }
}
