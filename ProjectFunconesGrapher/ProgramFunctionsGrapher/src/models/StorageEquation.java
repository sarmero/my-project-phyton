package models;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.util.ArrayList;

import classes.Equation;

public class StorageEquation {
    // escribir(salida de datos desde la memoria)
    private FileOutputStream fileOS;
    private ObjectOutputStream objectOS;
    // leer (entrada de datos desde la memoria)
    private FileInputStream fileIS;
    private ObjectInputStream objectIS;
    private String nameFile;

    public StorageEquation() {
        nameFile = "";
    }

    public String getNameFile() {
        return nameFile;
    }

    public void setNameFile(String nameFile) {
        this.nameFile = nameFile;
    }

    // escribir datos en la memoria (guardar)
    // OUTPUT (salida de datos de la memoria)
    public void write(ArrayList<Equation> arrayEquations) throws FileNotFoundException, IOException {
        // Gestiona el archivo en el sistema operativo
        fileOS = new FileOutputStream(nameFile);
        // transforma objectos en bytes para almacenar
        objectOS = new ObjectOutputStream(fileOS);

        for (Equation fx : arrayEquations) {
            objectOS.writeObject(fx);
        }

        objectOS.close();
        fileOS.close();
    }
    // leer datos de la memoria (abrir)
    // INPUT(entrada de datos en la memoria)

    public ArrayList<Equation> read() throws FileNotFoundException, IOException, ClassNotFoundException {
        ArrayList<Equation> arrayEquations;
        Equation fx;

        arrayEquations = new ArrayList<Equation>();

        fileIS = new FileInputStream(nameFile);
        objectIS = new ObjectInputStream(fileIS);

        while (true) {
            try {
                fx = (Equation) objectIS.readObject();
                arrayEquations.add(fx);
            } catch (Exception e) {
                break;// romper el ciclo
            }
        }
        return arrayEquations;
    }

}
