FileInputStream fileIn = new FileInputStream("data.ser");
ObjectInputStream in = new ObjectInputStream(fileIn);
Object obj = in.readObject();
in.close();

if (obj instanceof MyClass) {
    MyClass myObj = (MyClass) obj;
    // Operazioni su myObj
}
