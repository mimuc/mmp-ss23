using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DeployAsteroids : MonoBehaviour
{
    [SerializeField]
    private GameObject[] asteroidPrefabs;
    [SerializeField]
    private float respawnTime = 1.0f;

    private Vector2 screenBounds;

    // Start is called before the first frame update
    void Start()
    {
        screenBounds = Camera.main.ScreenToWorldPoint(new Vector3(Screen.width, Screen.height, Camera.main.transform.position.z));
        StartCoroutine(AsteroidWave());
       // var timer = new Timer();

    }
    
    private void SpawnAsteroid()
    {
        int randomIndex = Random.Range(0, asteroidPrefabs.Length);
        GameObject asteroidPrefab = asteroidPrefabs[randomIndex];
        if (!asteroidPrefab)
        {
            return; // because array fields can be set to null
        }
        GameObject asteroidInstance = Instantiate(asteroidPrefab) as GameObject;
        float spawnX = Random.Range(-screenBounds.x, screenBounds.y);
        asteroidInstance.transform.position = new Vector2(spawnX, screenBounds.y * 2);
    }

    private IEnumerator AsteroidWave()
    {
        while (true)
        {
            yield return new WaitForSeconds(respawnTime);
            SpawnAsteroid();
        }
    }
}
