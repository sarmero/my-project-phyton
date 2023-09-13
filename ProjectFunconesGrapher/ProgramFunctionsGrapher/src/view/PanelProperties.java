package view;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.Insets;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.security.cert.TrustAnchor;

import javax.swing.JButton;
import javax.swing.JColorChooser;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JSlider;

public class PanelProperties extends JPanel {

    private JLabel labColor;
    private JButton bntColor;
    private JLabel labzoom;
    private JSlider sldZoom;
    private JPanel pnlEffects;
    private GridBagConstraints rule;
    private JColorChooser dglColor;

    public PanelProperties(){

        launchWidgets();
        launchEvents();

    }
    
    private void launchWidgets(){
        setPreferredSize(new Dimension(200, 0));
        setMaximumSize(new Dimension(200, 0));
        setMinimumSize(new Dimension(200, 0));

        dglColor = new JColorChooser();
        
        pnlEffects = new JPanel();
        pnlEffects.setLayout(new GridBagLayout());
        add (pnlEffects, BorderLayout.NORTH);

        rule = new GridBagConstraints();
        rule.fill = GridBagConstraints.NONE;
        rule.anchor = GridBagConstraints.NORTHWEST;
        rule.insets = new Insets(2, 2, 2, 2);


        labColor = new JLabel();
        labColor.setText("Color linea");
        labColor.setPreferredSize(new Dimension(60, 25));
        rule.gridx = 0;
        rule.gridy = 0;
        pnlEffects.add(labColor, rule);


        bntColor = new JButton();
        bntColor.setBackground(Color.BLACK);
        bntColor.setPreferredSize(new Dimension(25, 25));
        rule.gridx = 1;
        rule.gridy = 0;
        pnlEffects.add(bntColor, rule);

        //zoom
        labzoom = new JLabel();
        labzoom.setText("Zoom: ");
        labzoom.setPreferredSize(new Dimension(60, 25));
        rule.gridx = 0;
        rule.gridy = 1;
        pnlEffects.add(labzoom, rule);

        sldZoom = new JSlider(JSlider.HORIZONTAL,10,100,50);
        sldZoom.setMinorTickSpacing(50);
        sldZoom.setMajorTickSpacing(100);
        sldZoom.setPaintTicks(true);
        sldZoom.setPaintLabels(true);

        sldZoom.setLabelTable(sldZoom.createStandardLabels(20));
        sldZoom.setPreferredSize(new Dimension(170, 50));
        rule.gridx = 0;
        rule.gridy = 2;
        rule.gridheight = 2;
        rule.anchor = GridBagConstraints.CENTER;
        pnlEffects.add(sldZoom, rule);




    }

    private void launchEvents(){
        bntColor.addActionListener(new ActionListener() {

            @Override
            public void actionPerformed(ActionEvent e) {
                selectColorLine();
            }
            
        });

    }

    private void selectColorLine(){
        Color select;
        select = JColorChooser.showDialog(this, "Seleccionar el color de la linea", Color.BLACK);
        bntColor.setBackground(select);
    }

}
