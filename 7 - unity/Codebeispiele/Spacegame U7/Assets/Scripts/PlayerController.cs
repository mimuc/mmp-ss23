using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerController : MonoBehaviour
{
    [SerializeField]
    private float speed;

    private Rigidbody2D rigidbody2D;
    
   
    // Start is called before the first frame update
    void Start()
    {
        rigidbody2D = GetComponent<Rigidbody2D>();
        
    }

    // Update is called once per frame
    void Update()
    {
        float moveHorizontal = Input.GetAxis("Horizontal");
        Vector2 movement = new Vector2(moveHorizontal, 0f);
        rigidbody2D.AddForce(movement * speed);
    }

    void OnCollisionEnter2D(Collision2D collision)
    {
        Debug.Log("Baaaaam");
    }

  
}
