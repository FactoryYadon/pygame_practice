using System;
using ActUtlTypeLib;

namespace component
{
    class test_run
    {
        public ActUtlType _act = new ActUtlType();

        
        public void test_def()
        {
            Console.WriteLine("hello test");
            
        }
    }
    
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");

            // ActUtlTypeLib.ActUtlType act = new ActUtlTypeLib.ActUtlType();

            // act.ActLogicalStationNumber = 5;
            // act.Open();

            // int return_value;

            // act.GetDevice("D0",out return_value);
            // Console.WriteLine(return_value.ToString());

            // act.Close();
            test_run test = new test_run();
            test.test_def();



        }

        
    }

    
}
