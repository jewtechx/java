import java.io.*;

class Demo implements java.io.Serializable
{
    public int a;
    public String b;

    public Demo(int a, String b)
    {
        this.a  = a;
        this.b = b;
    }
}

public class SerializationEg{
    public static void main(String[] args){
        Demo object = new Demo(1, "JewTechX");
        String filename = "file.ser";

        //serializing the obejct into byte stream
        if(args[0].equals("--serialize")){

       
        try
        {
            FileOutputStream file = new FileOutputStream(filename);
            ObjectOutputStream out = new ObjectOutputStream(file);

            out.writeObject(object);

            out.close();
            file.close();

            System.out.println("Object has been serialized");
        }
        catch(IOException ex){
            System.out.println("IOException spoted");
        }
     }
    //  deserializing the object into byte stream


     else if(args[0].equals("--deserialize"))
     {
        Demo object1 = null;

        try
        {
            FileInputStream file = new FileInputStream(filename);
            ObjectInputStream in = new ObjectInputStream(file);

            object1 = (Demo) in.readObject();

            in.close();
            file.close();
        
            System.out.println("Object has been deserialized ");
            System.out.println("a = " + object1.a);
            System.out.println("b = " + object1.b);
        }
         
        catch(IOException ex)
        {
            System.out.println("IOException is caught");
        }
         
        catch(ClassNotFoundException ex)
        {
            System.out.println("ClassNotFoundException is caught");
        }
     }else
     {
        System.out.println("No argument passed");
     }
    }
}