package view;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JPanel;
import javax.swing.Timer;

import classes.Equation;

public class PanelPlane extends JPanel {

    private Graphics2D g2;
    private Timer timerFx;

    public PanelPlane() {
        launchWidgets();
        launchEvents();

    }

    public void launchWidgets() {

        setBackground(Color.WHITE);

    }

    public void launchEvents() {
        timerFx = new Timer(100, new ActionListener() {

            @Override
            public void actionPerformed(ActionEvent e) {
                if (MainWindowView.listEquations.isStateDraw() == true) {
                    repaint();
                    MainWindowView.listEquations.setStateList(false);
                }
            }

        });
        timerFx.setRepeats(true);
        timerFx.start();

    }

    @Override
    public void paint(Graphics g) {

        int width, height;
        int x1, y1, x2, y2;

        width = getWidth();
        height = getHeight();

        super.paintComponent(g);

        g2 = (Graphics2D) g;
        g2.translate(width / 2, height / 2);
        g2.scale(1, -1);

        g2.drawLine(-width / 2, 0, width / 2, 0);

        g2.drawLine(0, height / 2, 0, -height / 2);

        for (Equation fx : MainWindowView.listEquations.getArrayEquation()) {
            for (x1 = -width / 2; x1 <= width / 2; x1 += 20) {
                y1 = (int) fx.getValueY(x1);
                x2 = x1 + 20;
                y2 = (int) fx.getValueY(x2);
                g2.drawLine(x1, y1, x2, y2);

            }

        }
    }

}
