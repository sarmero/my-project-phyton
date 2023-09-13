package controllers;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.ArrayList;


import classes.Equation;
import models.StorageEquation;

public class ListEquations {

    private ArrayList<Equation> arrayEquation;
    private boolean stateList;
    private boolean stateDraw;
    private StorageEquation storage;
    private boolean stateEdit;
    private boolean stateCombo;

    public ListEquations() {
        arrayEquation = new ArrayList<Equation>();
        storage = new StorageEquation();
        stateList = false;
        stateDraw = false;
        stateCombo = false;

    }

    public void addEquation(Equation equation) {
        arrayEquation.add(equation);
    }


    public Equation searchByEquation(String equation){
        Equation fx;//función encontrada
        fx = null;//no existe

        for ( Equation aux : arrayEquation) { //recorrer el arreglo de funciones 
            //verificar si el texto de la busca concide
            if (aux.getEquation().equals(equation)){
                fx = aux;//se captura la función encontrada
                break;//rompe la búsqueda
            }

        }
        return fx;
    }

    public ArrayList<Equation> getArrayEquation() {
        return arrayEquation;
    }

    public void setArrayEquation(ArrayList<Equation> arrayEquation) {
        this.arrayEquation = arrayEquation;
    }

    public boolean isStateList() {
        return stateList;
    }

    public void setStateList(boolean stateList) {
        this.stateList = stateList;
    }

    public boolean isStateDraw() {
        return stateDraw;
    }

    public void setStateDraw(boolean stateDraw) {
        this.stateDraw = stateDraw;
    }

    public boolean isStateEdit() {
        return stateEdit;
    }

    public void setStateEdit(boolean stateEdit) {
        this.stateEdit = stateEdit;
    }
    
    public boolean isStateCombo() {
        return stateCombo;
    }

    public void setStateCombo(boolean stateCombo) {
        this.stateCombo = stateCombo;
    }

    public void openFile(String absolutePath) throws FileNotFoundException, ClassNotFoundException, IOException {
        storage.setNameFile(absolutePath);
        arrayEquation = storage.read();
        stateList = true;
        stateDraw = true;
        stateEdit = false;
        stateCombo = true;
    }

    public void saveAsFile(String path) throws FileNotFoundException, IOException {
        storage.setNameFile(path);
        storage.write(arrayEquation);
        stateEdit = false;
    }

    public void saveFile() throws FileNotFoundException, IOException {
        storage.write(arrayEquation);
        stateEdit = false;
    }

    public void newFile() {
        stateList = true;
        stateDraw = true;
        stateEdit = false;
        stateCombo = true;
        storage.setNameFile(""); //archivo no tiene nombre 

    }
    public String getNameFile(){
        return storage.getNameFile();
    }

}