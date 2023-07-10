using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class AsteroidController : MonoBehaviour
{

    public float speed = 0.5f;
    private Rigidbody2D rb2D;

    private Vector2 screenBounds;

    // Start is called before the first frame update
    void Start()
    {
        rb2D = GetComponent<Rigidbody2D>();
        rb2D.velocity = new Vector2(0, -speed);

        screenBounds = Camera.main.ScreenToWorldPoint(new Vector2(Screen.width, Screen.height));

    }

    // Update is called once per frame
    void Update()
    {        
        if (-transform.position.y > screenBounds.y * 2)
        {
           Destroy(this.gameObject);
        }
    }

    
}
