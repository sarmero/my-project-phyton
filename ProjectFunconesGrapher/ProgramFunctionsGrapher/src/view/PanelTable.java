package view;

import java.awt.BorderLayout;
import java.awt.Dimension;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.Insets;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.Timer;
import javax.swing.DefaultComboBoxModel;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JSpinner;
import javax.swing.JTable;
import javax.swing.SpinnerNumberModel;
import javax.swing.table.DefaultTableModel;
import javax.swing.table.TableColumn;

import classes.Equation;

public class PanelTable extends JPanel {

    private JPanel pnlRange;
    private DefaultTableModel model;
    private JTable tabRange;
    private JScrollPane scroll;
    private TableColumn column;
    private GridBagConstraints rule;
    private JLabel labFx;
    private JComboBox<String> cmbFx;
    private JLabel labStart;
    private JSpinner spnStart;
    private JLabel labEnd;
    private JSpinner spnEnd;
    private JLabel labIncrement;
    private JSpinner spnIncrement;
    private JButton btnCalculate;
    private SpinnerNumberModel spnModelStart;
    private SpinnerNumberModel spnModelEnd;
    private SpinnerNumberModel spnModelIncrement;
    private DefaultComboBoxModel<String> cmbModelFx;
    private Timer timerFx;

    public PanelTable() {
        launchWidgets();
        launchEvents();
    }

    private void launchWidgets() {

        setLayout(new BorderLayout());

        setPreferredSize(new Dimension(200, 0));
        setMaximumSize(new Dimension(200, 0));
        setMinimumSize(new Dimension(200, 0));

        pnlRange = new JPanel();
        pnlRange.setLayout(new GridBagLayout());

        rule = new GridBagConstraints();
        rule.fill = GridBagConstraints.NONE;
        rule.anchor = GridBagConstraints.NORTHWEST;
        rule.insets = new Insets(2, 2, 2, 2);

        labFx = new JLabel();
        labFx.setText("Funciones");
        labFx.setPreferredSize(new Dimension(70, 25));
        rule.gridx = 0;
        rule.gridy = 0;
        pnlRange.add(labFx, rule);

        cmbModelFx = new DefaultComboBoxModel<String>();

        cmbFx = new JComboBox<String>();
        cmbFx.setModel(cmbModelFx);
        cmbFx.setPreferredSize(new Dimension(120, 25));
        rule.gridx = 1;
        rule.gridy = 0;
        pnlRange.add(cmbFx, rule);

        labStart = new JLabel();
        labStart.setText("Inicio: ");
        labStart.setPreferredSize(new Dimension(70, 25));
        rule.gridx = 0;
        rule.gridy = 1;
        pnlRange.add(labStart, rule);

        //modelo de datos maneja los datos del control(valor inicial,)
        spnModelStart = new SpinnerNumberModel(0, -100, 100, 0.1);

        //control de grafico (apariencia)
        spnStart = new JSpinner();
        spnStart.setModel(spnModelStart);
        spnStart.setPreferredSize(new Dimension(60, 23));
        rule.gridx = 1;
        rule.gridy = 1;
        pnlRange.add(spnStart, rule);

        labEnd = new JLabel();
        labEnd.setText("Fin: ");
        labEnd.setPreferredSize(new Dimension(70, 25));
        rule.gridx = 0;
        rule.gridy = 2;
        pnlRange.add(labEnd, rule);

        spnModelEnd = new SpinnerNumberModel(0, -100, 100, 0.1);

        spnEnd = new JSpinner();
        spnEnd.setModel(spnModelEnd);
        spnEnd.setPreferredSize(new Dimension(60, 23));
        rule.gridx = 1;
        rule.gridy = 2;
        pnlRange.add(spnEnd, rule);

        labIncrement = new JLabel();
        labIncrement.setText("Incremento: ");
        labIncrement.setPreferredSize(new Dimension(70, 25));
        rule.gridx = 0;
        rule.gridy = 3;
        pnlRange.add(labIncrement, rule);

        spnModelIncrement = new SpinnerNumberModel(0, -100, 100, 0.1);

        spnIncrement = new JSpinner();
        spnIncrement.setModel(spnModelIncrement);
        spnIncrement.setPreferredSize(new Dimension(60, 23));
        rule.gridx = 1;
        rule.gridy = 3;
        pnlRange.add(spnIncrement, rule);

        btnCalculate = new JButton();
        btnCalculate.setText("Calcular");
        btnCalculate.setPreferredSize(new Dimension(100, 25));
        rule.gridx = 0;
        rule.gridy = 4;
        rule.gridwidth = 2;
        rule.anchor = GridBagConstraints.CENTER;
        pnlRange.add(btnCalculate, rule);

        add(pnlRange, BorderLayout.NORTH);

        //
        model = new DefaultTableModel();

        model.setRowCount(0);
        model.setColumnCount(2);

        tabRange = new JTable();
        tabRange.setModel(model);
        tabRange.setRowHeight(20); // alto de las filas

        column = tabRange.getColumnModel().getColumn(0);
        column.setHeaderValue("x");

        column = tabRange.getColumnModel().getColumn(1);
        column.setHeaderValue("y");

        scroll = new JScrollPane();
        scroll.setViewportView(tabRange);

        add(scroll, BorderLayout.CENTER);

    }

    private void launchEvents() {

        timerFx = new Timer(100, new ActionListener() {

            @Override
            public void actionPerformed(ActionEvent e) {
                if (MainWindowView.listEquations.isStateDraw() == true) {
                    cmbModelFx.removeAllElements();
                    for (Equation fx : MainWindowView.listEquations.getArrayEquation()) {
                        cmbModelFx.addElement(fx.getEquation());
                    }
                    cmbFx.setModel(cmbModelFx);
                    MainWindowView.listEquations.setStateList(false);
                }
            }

        });
        timerFx.setRepeats(true);
        timerFx.start();

        btnCalculate.addActionListener(new ActionListener() {

            @Override
            public void actionPerformed(ActionEvent e) {
                calculateTabulation();
            }
            
        });
    }

    private void calculateTabulation(){
        double start, end, increment;
        String equation;
        Equation fx;
        double x, y;

        //obtener el item seleccionado del combo
        equation = (String) cmbFx.getSelectedItem();
        fx = MainWindowView.listEquations.searchByEquation(equation);

        if (fx != null){// la funcion fue encontrada
            start = (Double) spnStart.getValue();
            end = (Double) spnEnd.getValue();
            increment = (Double) spnIncrement.getValue();

            //llenar la tabla 
            model.setRowCount(0);// limpiar la tabla
            for (x = start; x <= end; x += increment){
                y = fx.getValueY((float)x);
                model.addRow(new Object[] {x, y});

            }
        }

    }


}
