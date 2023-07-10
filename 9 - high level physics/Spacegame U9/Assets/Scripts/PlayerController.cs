using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class PlayerController : MonoBehaviour
{
    public float speed;


    private Animator animator;
    private Rigidbody2D rigidbody2D;
    private AudioSource audioSource;
    private ParticleSystem particleSystem;
    
   
    // Start is called before the first frame update
    void Start()
    {
        rigidbody2D = GetComponent<Rigidbody2D>();
        audioSource = GetComponent<AudioSource>();
        particleSystem = GetComponent<ParticleSystem>();
        animator = this.gameObject.transform.GetChild(0).gameObject.transform.GetChild(0).GetComponent<Animator>();
      //  animator.Play("");
        animator.StopPlayback();
        // animator.StopPlayback();//  SetBool("Animate", false);
        
    }

    // Update is called once per frame
    void Update()
    {
        
    }

    void FixedUpdate()
    {       
        float moveHorizontal = Input.GetAxis("Horizontal");
        Vector2 movement = new Vector2(moveHorizontal, 0f);
        rigidbody2D.AddForce(movement * speed);
        /*
        if (System.Math.Abs(moveHorizontal) > 0f && !audioSource.isPlaying)
        {
            audioSource.Play();           
        }
        else
        {
            audioSource.Stop();            
        }
        */
        

        if (System.Math.Abs(moveHorizontal) > 0f && !audioSource.isPlaying)
        {
            audioSource.Play();
            particleSystem.Play();           
        }
        else if (System.Math.Abs(moveHorizontal) < 0.001f)
        {
            particleSystem.Stop();
            audioSource.Stop();
        }
        
         
    }

    void OnTriggerEnter2D(Collider2D collider2D)
    {
        Debug.Log(collider2D.name);
        Debug.Log(collider2D.gameObject.name);
        // Explode();
        // collider2D.
        rigidbody2D.AddForce(new Vector2(10, -100));
        rigidbody2D.AddTorque(100f);
    }

   

    void Explode()
    {
        
        // animator.SetTrigger("Animate");
        Debug.Log("Animation!!");
        GetComponent<Animator>().StartPlayback();
    }
}
