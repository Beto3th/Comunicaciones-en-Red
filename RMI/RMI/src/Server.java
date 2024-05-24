import java.rmi.Naming;
import java.rmi.registry.LocateRegistry;

public class Server {
    public static void main(String[] args) {
        try {
            // Crear el registro RMI en el puerto 1099
            LocateRegistry.createRegistry(1099);
            
            // Crear una instancia del objeto remoto
            HelloImpl obj = new HelloImpl();
            
            // Registrar el objeto remoto con el nombre "Hello"
            Naming.rebind("Hello", obj);
            
            System.out.println("Servidor listo");
        } catch (Exception e) {
            System.err.println("Excepción del servidor: " + e.toString());
            e.printStackTrace();
        }
    }
}
