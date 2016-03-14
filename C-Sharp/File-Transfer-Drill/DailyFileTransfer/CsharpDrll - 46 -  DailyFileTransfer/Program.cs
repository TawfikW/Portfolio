using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CsharpDrll___46____DailyFileTransfer
{
    class Ftp2
    {
        static void Main()
        {
            FileTransfer();
        }


        static void FileTransfer()
        {
            string fileName = ".txt";
            string sourcePath = @"C:\Users\Wes\Desktop\Folder A\";
            string destPath = @"C:\Users\Wes\Desktop\Folder B\";
            string sourceFile = Path.Combine(sourcePath, fileName);
            string destFile = Path.Combine(destPath, fileName);


            if (Directory.Exists(destPath))
            {
                Directory.CreateDirectory(destPath);
            }

            if (Directory.Exists(sourcePath))
            {

                string[] files = Directory.GetFiles(sourcePath);
                foreach (string s in files)
                { Console.WriteLine(s); }

                // Copy the files more than 24hrs old, overwrites existing files
                foreach (string s in files)
                {
                    DateTime fileDate = File.GetLastWriteTime(s);
                    bool timeCheck = fileDate > DateTime.Now.AddHours(-24);

                    if (timeCheck == true)
                    {
                        fileName = Path.GetFileName(s);
                        destFile = Path.Combine(destPath, fileName);
                        File.Copy(s, destFile, true);

                        Console.WriteLine("Transferring file ... ");
                    }
                }
                Console.WriteLine("\nFile transfer complete.\n");
            }
            else
            {
                Console.WriteLine("Source path does not exist.");
            }

            //Console.WriteLine("Press any key to exit.");
            //Console.ReadKey();

        }


    }
}

