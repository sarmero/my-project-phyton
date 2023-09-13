package view;

import java.awt.CardLayout;

import javax.swing.JPanel;

public class PanelWork extends JPanel {

    private PanelFunctions pnlFx;
    private PanelTable pnlTable;
    private CardLayout layout;

    public PanelWork(){
        launchWidgets();
    }

    private void launchWidgets() {

        pnlFx = new PanelFunctions();
        pnlTable = new PanelTable();

        layout = new CardLayout();
        setLayout(layout);

        add(pnlFx, "fx"); //adicionar el panel al gestor de tarjetas 
        add(pnlTable, "table");

    }

    public void showCard(String key){
        layout.show(this, key);
    }

}
