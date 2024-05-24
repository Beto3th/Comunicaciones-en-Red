import java.rmi.Naming;

public class Client {
    public static void main(String[] args) {
        try {
            // Buscar el objeto remoto en el registro RMI
            Hello obj = (Hello) Naming.lookup("//localhost/Hello");
            
            // Invocar el método remoto
            String message = obj.sayHello();
            System.out.println("Mensaje del servidor: " + message);
        } catch (Exception e) {
            System.err.println("Excepción del cliente: " + e.toString());
            e.printStackTrace();
        }
    }
}