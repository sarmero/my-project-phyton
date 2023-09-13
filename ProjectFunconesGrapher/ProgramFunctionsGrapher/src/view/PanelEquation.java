package view;

import java.awt.Color;
import java.awt.Component;
import java.awt.Font;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.BorderFactory;
import javax.swing.BoxLayout;
import javax.swing.JButton;
import javax.swing.JLabel;
import javax.swing.JPanel;

public abstract class PanelEquation extends JPanel{

    protected JLabel labTitle;
    private JLabel labHelp;
    protected JPanel pnlComponents;
    private JButton butAdd;
    
    public PanelEquation(){

        launchWidgets();
        launchEvents();

    } 

    protected void launchWidgets(){

        setLayout(new BoxLayout(this, BoxLayout.Y_AXIS));
        setAlignmentX(Component.LEFT_ALIGNMENT);
        setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));
        setBackground(Color.YELLOW);

        labTitle = new JLabel();
        labTitle.setFont(new Font("Arial", Font.BOLD, 12));
        add(labTitle);
        
        labHelp = new JLabel();
        labHelp.setText("Coeficientes");
        add(labHelp);

        pnlComponents = new JPanel();
        pnlComponents.setLayout(new BoxLayout(pnlComponents, BoxLayout.Y_AXIS));
        add(pnlComponents);

        butAdd = new JButton();
        butAdd.setText("+");
        add(butAdd);


    }

    protected void launchEvents(){

        butAdd.addActionListener(new ActionListener() {

            @Override
            public void actionPerformed(ActionEvent e) {
                addEquation();
            }
            
        });
        
    }

    public abstract void initPanel();
    public abstract void addEquation();
}
