public static class PlayerStats
{
    private static int deaths, score;

    public static int Deaths
    {
        get
        {
            return deaths;
        }
        set
        {
            deaths = value;
        }
    }
    public static int Score
    {
        get
        {
            return score;
        }
        set
        {
            score = value;
        }
    }
}