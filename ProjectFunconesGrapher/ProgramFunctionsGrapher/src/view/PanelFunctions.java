package view;

import java.awt.BorderLayout;
import java.awt.Dimension;
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.DefaultListModel;
import javax.swing.JButton;
import javax.swing.JList;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.ScrollPaneConstants;
import javax.swing.Timer;

import classes.Equation;

public class PanelFunctions extends JPanel {

    private JButton butX1;
    private JPanel pnlButtonsFx;
    private JList<String> listFx;
    private JScrollPane scrFx;
    private DefaultListModel<String> model;
    private JButton butX2;
    private JButton butX3;

    private PanelLinearEquation pnlLinearEquation;
    private JPanel pnlCard;
    private Timer timerFx;

    public PanelFunctions() {

        launchWidgets();
        launchEvents();
    }

    private void launchWidgets() {

        setPreferredSize(new Dimension(200, 0));
        setMaximumSize(new Dimension(200, 0));
        setMinimumSize(new Dimension(200, 0));
        setLayout(new BorderLayout());

        pnlCard = new JPanel();
        pnlCard.setLayout(new BorderLayout(5, 5));

        pnlButtonsFx = new JPanel();
        pnlButtonsFx.setLayout(new FlowLayout());
        pnlCard.add(pnlButtonsFx, BorderLayout.NORTH);

        butX1 = new JButton();
        butX1.setText("x1");
        pnlButtonsFx.add(butX1);

        butX2 = new JButton();
        butX2.setText("x2");
        pnlButtonsFx.add(butX2);

        butX3 = new JButton();
        butX3.setText("x3");
        pnlButtonsFx.add(butX3);

        pnlLinearEquation = new PanelLinearEquation();
        pnlCard.add(pnlLinearEquation, BorderLayout.CENTER);

        model = new DefaultListModel<String>();

        listFx = new JList<String>(); // lista de elementos
        listFx.setModel(model);

        scrFx = new JScrollPane(); // panel de desplazamiento
        scrFx.setVerticalScrollBarPolicy(ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS);
        // siempre visible la barra del panel de desplazamiento
        scrFx.setViewportView(listFx); // adicionar la lista al panel de desplazamiento

        add(pnlCard, BorderLayout.NORTH);
        add(scrFx, BorderLayout.CENTER);

    }

    private void launchEvents() {

        butX1.addActionListener(new ActionListener() {

            @Override
            public void actionPerformed(ActionEvent e) {

            }

        });

        timerFx = new Timer(100, new ActionListener() {

            @Override
            public void actionPerformed(ActionEvent e) {
                if (MainWindowView.listEquations.isStateDraw() == true) {
                    model.clear();
                    for (Equation fx : MainWindowView.listEquations.getArrayEquation()) {
                        model.addElement(fx.getEquation());
                    }
                    listFx.setModel(model);
                    MainWindowView.listEquations.setStateList(false);
                }
            }

        });
        timerFx.setRepeats(true);
        timerFx.start();
    }

}
