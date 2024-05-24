import java.rmi.Remote;
import java.rmi.RemoteException;

public interface RemoteClient extends Remote {
    void half(int i) throws RemoteException;
}