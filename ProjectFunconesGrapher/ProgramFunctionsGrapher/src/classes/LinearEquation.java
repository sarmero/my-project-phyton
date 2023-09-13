package classes;

public class LinearEquation extends Equation {

    private float a;
    private float b;

    public LinearEquation(float a, float b) {
        this.a = a;
        this.b = b;
    }

    @Override
    public String getEquation() {
        //Devolver la ecuación de la forma f(x) = ax + b

        String text;
        text = "f(x) = "+ a + "x";
        if(b > 0){
            text += " +";
        }
        text += b;
        return text;
    }

    @Override
    public float getValueY(float x) {
        float y;
        y = a * x + b;
        return y;
    }
    
}
