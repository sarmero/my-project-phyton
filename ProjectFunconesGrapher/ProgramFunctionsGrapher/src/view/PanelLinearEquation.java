package view;

import java.awt.Component;

import javax.swing.BoxLayout;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;

import classes.LinearEquation;

public class PanelLinearEquation extends PanelEquation {

    private JLabel labA;
    private JPanel pnlRow1;
    private JPanel pnlRow2;
    private JLabel labB;
    private JTextField txtA;
    private JTextField txtB;
    private LinearEquation fx;

    public PanelLinearEquation(){
        super(); //constructor de la super clase
    }

    @Override
    protected void launchWidgets() {
        super.launchWidgets(); 

        labTitle.setText("Función Lineal");

        pnlRow1 = new JPanel();
        pnlRow1.setLayout(new BoxLayout(pnlRow1, BoxLayout.X_AXIS));
        pnlRow1.setAlignmentX(Component.LEFT_ALIGNMENT);
        pnlComponents.add(pnlRow1);

        labA = new JLabel();
        labA.setText("a: ");
        pnlRow1.add(labA);

        txtA= new JTextField();
        pnlRow1.add(txtA);

        pnlRow2 = new JPanel();
        pnlRow2.setLayout(new BoxLayout(pnlRow2, BoxLayout.X_AXIS));
        pnlRow2.setAlignmentX(Component.LEFT_ALIGNMENT);
        pnlComponents.add(pnlRow2);

        labB = new JLabel();
        labB.setText("b: ");
        pnlRow2.add(labB);

        txtB= new JTextField();
        pnlRow2.add(txtB);

        
    }

    @Override
    public void initPanel() {
        
    }

    @Override
    public void addEquation() {
        String textA,textB;
        float a,b;

        textA = txtA.getText();
        textB = txtB.getText();

        a = Float.parseFloat(textA);
        b = Float.parseFloat(textB);

        fx = new LinearEquation(a, b);
        MainWindowView.listEquations.addEquation(fx);
        MainWindowView.listEquations.setStateList(true);
        MainWindowView.listEquations.setStateDraw(true);
        MainWindowView.listEquations.setStateEdit(true);
        MainWindowView.listEquations.setStateCombo(true);

        
    
    }
    
}
