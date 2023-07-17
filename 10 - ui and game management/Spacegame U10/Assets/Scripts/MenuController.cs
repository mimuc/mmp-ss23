using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class MenuController : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyDown("escape"))
        {
            print("escape key was pressed");
            SceneManager.LoadScene("SpaceGame");
        }
    }

    public void OnButtonClick()
    {
        Debug.Log("You have clicked the button!");
    }
}
