package classes;

import java.io.Serializable;

public abstract class Equation implements Serializable{

    public abstract String getEquation();

    public abstract float getValueY(float x);
}
