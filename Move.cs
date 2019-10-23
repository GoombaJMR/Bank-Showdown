using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public enum MoveType {
    Steal, Add, Block
}

public class Move : MonoBehaviour
{
    public MoveType type;
    public Sprite image;
    private Image rend;
    public bool active;

    private Color32 SELECTED = new Color32(255, 255, 255, 255);
    private Color32 UNSELECTED = new Color32(150, 150, 150, 150);

    private void Start() {
        rend = GetComponent<Image>();
    }

    private void Update() {
        SetColor();
        Oscillate();
    }

    private void Oscillate() {
        float size_x = transform.localScale.x;
        float size_y = transform.localScale.y;
        Vector3 tempTrans;

        float range = 0.15f;
        float speed = 3f;
        float minSize = 0.95f;

        if (active) {
            size_x = (Mathf.Sin(Time.time * speed) + 1.0f) / 2.0f * range + minSize;
            size_y = (Mathf.Sin(Time.time * speed) + 1.0f) / 2.0f * range + minSize;
            tempTrans = new Vector3(size_x, size_y, 1f);
            transform.localScale = tempTrans;
        } else {
            Vector3 original = new Vector3(1f, 1f, 1f);
            transform.localScale = original;
        }
    }

    private void SetColor() {
        if (active) {
            rend.color = SELECTED;
        } else {
            rend.color = UNSELECTED;
        }
    }

    public void SetActive() {
        active = true;
    }

    public void SetInactive() {
        active = false;
    }
}
