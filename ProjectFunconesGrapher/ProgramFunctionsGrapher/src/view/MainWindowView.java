package view;

import java.awt.BorderLayout;
import java.awt.Dimension;
import java.awt.Image;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;

import javax.swing.ImageIcon;
import javax.swing.JButton;
import javax.swing.JFileChooser;
import javax.swing.JFrame;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JOptionPane;
import javax.swing.JSeparator;
import javax.swing.JToolBar;
import javax.swing.KeyStroke;
import javax.swing.filechooser.FileNameExtensionFilter;

import controllers.ListEquations;

public class MainWindowView extends JFrame {

        private ImageIcon imgIcon;
        private JMenuBar barMenu;
        private JMenu menFile;
        private JMenuItem iteNew;
        private JMenuItem iteOpen;
        private JMenuItem iteSave;
        private JMenu menTools;
        private JMenu menHelp;
        private JMenuItem iteSaveAs;
        private JSeparator separator1;
        private JSeparator separator2;
        private JMenuItem iteExit;
        private JMenuItem iteExportImage;
        private JMenuItem itePrint;
        private JMenuItem iteCredits;
        private JToolBar toolBar;
        private JButton butNew;
        private JButton butOpen;
        private JButton butSave;
        private JButton butSaveAs;
        private JButton butExportImage;
        private JButton butPrint;
        private JButton butFx;
        private JButton butTable;
        private PanelWork pnlWork;
        private PanelProperties pnlProperties;
        private PanelPlane pnlPlane;
        protected JFileChooser dlgFileOpen;
        protected File file;
        private JFileChooser dlgFile;

        // static permite que un espacio de memoria sea de acceso global desde cualquier
        // lugar de la aplicación (para todos los objeto)
        public static ListEquations listEquations;

        public MainWindowView() {

                listEquations = new ListEquations();
                launchWidgets();
                launchEvents();
        }

        private void launchWidgets() {

                // window
                setSize(1024, 768);
                setTitle("Gráficador de Funciones");
                setDefaultCloseOperation(JFrame.DO_NOTHING_ON_CLOSE);
                setLocationRelativeTo(null);
                setExtendedState(JFrame.MAXIMIZED_BOTH); // inicia la ventana maximizada
                setLayout(new BorderLayout()); // arriba, abajo, izquierda, centro, derecha
                imgIcon = new ImageIcon("img/main.png");
                setIconImage(imgIcon.getImage());

                createMenu();
                createToolBar();

                dlgFile = new JFileChooser();
                FileNameExtensionFilter filterFFX = new FileNameExtensionFilter("Archivo Función(.ffx)", "ffx");
                dlgFile.addChoosableFileFilter(filterFFX);
                dlgFile.setFileFilter(filterFFX);

                pnlWork = new PanelWork();
                add(pnlWork, BorderLayout.WEST);

                pnlProperties = new PanelProperties();
                add(pnlProperties, BorderLayout.EAST);

                pnlPlane = new PanelPlane();
                add(pnlPlane, BorderLayout.CENTER);

        }

        private void launchEvents() {

                butFx.addActionListener(new ActionListener() {

                        @Override
                        public void actionPerformed(ActionEvent e) {
                                pnlWork.showCard("fx");
                        }

                });

                butTable.addActionListener(new ActionListener() {

                        @Override
                        public void actionPerformed(ActionEvent e) {
                                pnlWork.showCard("table");
                        }

                });

                iteOpen.addActionListener(new ActionListener() {

                        @Override
                        public void actionPerformed(ActionEvent e) {
                                openFile();
                        }

                });

                iteSaveAs.addActionListener(new ActionListener() {

                        @Override
                        public void actionPerformed(ActionEvent e) {
                                saveFileAs();
                        }

                });

                iteSave.addActionListener(new ActionListener() {

                        @Override
                        public void actionPerformed(ActionEvent e) {
                                saveFile();
                        }

                });

                iteNew.addActionListener(new ActionListener() {

                        @Override
                        public void actionPerformed(ActionEvent e) {
                                newFile();
                        }

                });

                iteExit.addActionListener(new ActionListener() {

                        @Override
                        public void actionPerformed(ActionEvent e) {
                                exit();
                        }

                });

                this.addWindowListener(new WindowAdapter() {

                        @Override
                        public void windowClosing(WindowEvent e) {
                                exit();
                        }

                });

        }

        private void exit() {
                int result;
                if (listEquations.isStateEdit() == true) {
                        result = JOptionPane.showConfirmDialog(
                                        this,
                                        "Hay Cambios pendiente por guardar.\n¿esta seguro de salir de la aplicación?",
                                        "Gráficas de funciones",
                                        JOptionPane.YES_NO_OPTION);
                        if (result == JOptionPane.YES_OPTION) {
                                System.exit(0);
                        }
                } else {
                        System.exit(0);
                }
        }

        private void newFile() {
                int result;
                if (listEquations.isStateEdit() == true) {
                        result = JOptionPane.showConfirmDialog(
                                        this,
                                        "Hay Cambios pendiente por guardar.\n¿esta seguro de crear un nuevo archivo?",
                                        "Gráficas de funciones",
                                        JOptionPane.YES_NO_OPTION);
                        if (result == JOptionPane.YES_OPTION) {
                                listEquations = new ListEquations();
                                listEquations.newFile();
                        }
                } else {
                        listEquations = new ListEquations();
                        listEquations.newFile();
                }
        }

        private void saveFile() {
                if (listEquations.isStateEdit() == true) {
                        // si el archivo no tiene nombre pasa a realizar guardar como...
                        if (listEquations.getNameFile().equals("")) {
                                saveFileAs();
                        } else {
                                try {
                                        listEquations.saveFile();
                                } catch (FileNotFoundException e) {
                                        System.out.println("Archivo no encontrado");
                                } catch (IOException e) {
                                        System.out.println("Error al guardar el archivo");
                                }
                        }

                }
        }

        private void saveFileAs() {

                int result;
                File file;
                dlgFile.setSelectedFile(new File("funciones.ffx"));
                // abrir dialogo de archivo para guardar archivos
                result = dlgFile.showSaveDialog(this);

                // verificar que el usuario dio click en OK
                if (result == JFileChooser.APPROVE_OPTION) {
                        // obtener el archivo que el usuario selecciono
                        file = dlgFile.getSelectedFile();
                        // JOptionPane.showMessageDialog(this, file.getAbsolutePath());
                        try {
                                listEquations.saveAsFile(file.getAbsolutePath());
                        } catch (FileNotFoundException e) {
                                System.out.println("El archivo no se encuentra");
                        } catch (IOException e) {
                                System.out.println("Error en el proceso de escritura");
                        }
                }

        }

        private void openFile() {
                int result;
                dlgFileOpen = new JFileChooser();

                if (listEquations.isStateEdit() == true) {
                        result = JOptionPane.showConfirmDialog(
                                        this,
                                        "Hay Cambios pendiente por guardar.\n¿esta seguro de crear un nuevo archivo?",
                                        "Gráficas de funciones",
                                        JOptionPane.YES_NO_OPTION);
                        if (result == JOptionPane.YES_OPTION) {
                                openFileBase();
                        }
                } else {
                        openFileBase();
                }
        }

        private void openFileBase() {
                int result;

                dlgFile.setSelectedFile(new File(""));
                result = dlgFileOpen.showOpenDialog(this);
                if (result == JFileChooser.APPROVE_OPTION) {
                        file = dlgFileOpen.getSelectedFile();
                        JOptionPane.showMessageDialog(this, file.getAbsolutePath());
                        listEquations = new ListEquations();

                        try {
                                listEquations.openFile(file.getAbsolutePath());
                        } catch (FileNotFoundException e) {
                                System.out.println("Archivo no encontrado");
                        } catch (ClassNotFoundException e) {
                                System.out.println("Clase no encontrada");
                        } catch (IOException e) {
                                System.out.println("Error en el proceso de lectura");
                        }
                }
        }

        public void initWindow() {
                setVisible(true);
        }

        private void createMenu() {
                // Barra Menu
                barMenu = new JMenuBar();
                setJMenuBar(barMenu);

                // ----------------------------------------------------------------------------------------------------

                // Menu
                menFile = new JMenu();
                menFile.setText("Archivo");
                menFile.setMnemonic('R');
                barMenu.add(menFile);

                // Item
                iteNew = new JMenuItem();
                iteNew.setText("Nuevo");
                iteNew.setMnemonic('O');
                iteNew.setAccelerator(KeyStroke.getKeyStroke('O', KeyEvent.CTRL_DOWN_MASK));
                imgIcon = new ImageIcon("img/file.png");
                imgIcon = new ImageIcon(
                                imgIcon.getImage().getScaledInstance(16, 16, Image.SCALE_SMOOTH));
                iteNew.setIcon(imgIcon);
                menFile.add(iteNew);

                separator1 = new JSeparator();
                menFile.add(separator1);

                iteOpen = new JMenuItem();
                iteOpen.setText("Abrir");
                iteOpen.setMnemonic('A');
                iteOpen.setAccelerator(KeyStroke.getKeyStroke('A', KeyEvent.CTRL_DOWN_MASK));
                imgIcon = new ImageIcon("img/open.png");
                imgIcon = new ImageIcon(
                                imgIcon.getImage().getScaledInstance(16, 16, Image.SCALE_SMOOTH));
                iteOpen.setIcon(imgIcon);
                menFile.add(iteOpen);

                iteSave = new JMenuItem();
                iteSave.setText("Guardar");
                iteSave.setMnemonic('G');
                iteSave.setAccelerator(KeyStroke.getKeyStroke('G', KeyEvent.CTRL_DOWN_MASK));
                imgIcon = new ImageIcon("img/save.png");
                imgIcon = new ImageIcon(
                                imgIcon.getImage().getScaledInstance(16, 16, Image.SCALE_SMOOTH));
                iteSave.setIcon(imgIcon);
                menFile.add(iteSave);

                iteSaveAs = new JMenuItem();
                iteSaveAs.setText("Guardar Como");
                iteSaveAs.setMnemonic('U');
                iteSaveAs.setAccelerator(KeyStroke.getKeyStroke('U', KeyEvent.CTRL_DOWN_MASK));
                imgIcon = new ImageIcon("img/save_as.png");
                imgIcon = new ImageIcon(
                                imgIcon.getImage().getScaledInstance(16, 16, Image.SCALE_SMOOTH));
                iteSaveAs.setIcon(imgIcon);
                menFile.add(iteSaveAs);

                separator2 = new JSeparator();
                menFile.add(separator2);

                iteExit = new JMenuItem();
                iteExit.setText("Salir");
                iteExit.setMnemonic('X');
                iteExit.setAccelerator(KeyStroke.getKeyStroke('X', KeyEvent.CTRL_DOWN_MASK));
                imgIcon = new ImageIcon("img/close.png");
                imgIcon = new ImageIcon(
                                imgIcon.getImage().getScaledInstance(16, 16, Image.SCALE_SMOOTH));
                iteExit.setIcon(imgIcon);
                menFile.add(iteExit);

                // ----------------------------------------------------------------------------------------------------

                // Menu
                menTools = new JMenu();
                menTools.setText("Herramientas");
                menTools.setMnemonic('H');
                barMenu.add(menTools);

                // Item herramientas
                iteExportImage = new JMenuItem();
                iteExportImage.setText("Exportar Imagen");
                iteExportImage.setMnemonic('E');
                iteExportImage.setAccelerator(KeyStroke.getKeyStroke('E', KeyEvent.CTRL_DOWN_MASK));
                imgIcon = new ImageIcon("img/export_image.png");
                imgIcon = new ImageIcon(
                                imgIcon.getImage().getScaledInstance(16, 16, Image.SCALE_SMOOTH));
                iteExportImage.setIcon(imgIcon);
                menTools.add(iteExportImage);

                itePrint = new JMenuItem();
                itePrint.setText("Imprimir");
                itePrint.setMnemonic('P');
                itePrint.setAccelerator(KeyStroke.getKeyStroke('P', KeyEvent.CTRL_DOWN_MASK));
                imgIcon = new ImageIcon("img/print.png");
                imgIcon = new ImageIcon(
                                imgIcon.getImage().getScaledInstance(16, 16, Image.SCALE_SMOOTH));
                itePrint.setIcon(imgIcon);
                menTools.add(itePrint);

                // -----------------------------------------------------------------------------------------------------

                // Menu
                menHelp = new JMenu();
                menHelp.setText("Ayuda");
                menHelp.setMnemonic('Y');
                barMenu.add(menHelp);

                // Item ayuda
                iteCredits = new JMenuItem();
                iteCredits.setText("Créditos");
                iteCredits.setMnemonic('D');
                iteCredits.setAccelerator(KeyStroke.getKeyStroke('D', KeyEvent.CTRL_DOWN_MASK));
                imgIcon = new ImageIcon("img/help.png");
                imgIcon = new ImageIcon(
                                imgIcon.getImage().getScaledInstance(16, 16, Image.SCALE_SMOOTH));
                iteCredits.setIcon(imgIcon);
                menHelp.add(iteCredits);

        }

        private void createToolBar() {
                toolBar = new JToolBar();
                // toolBar.setFloatable(false);
                add(toolBar, BorderLayout.NORTH);

                butNew = new JButton();
                imgIcon = new ImageIcon("img/file.png");
                imgIcon = new ImageIcon(
                                imgIcon.getImage().getScaledInstance(30, 30, Image.SCALE_SMOOTH));
                butNew.setIcon(imgIcon);
                toolBar.add(butNew);

                toolBar.addSeparator(new Dimension(20, 0));

                butOpen = new JButton();
                imgIcon = new ImageIcon("img/open.png");
                imgIcon = new ImageIcon(
                                imgIcon.getImage().getScaledInstance(30, 30, Image.SCALE_SMOOTH));
                butOpen.setIcon(imgIcon);
                toolBar.add(butOpen);

                butSave = new JButton();
                imgIcon = new ImageIcon("img/save.png");
                imgIcon = new ImageIcon(
                                imgIcon.getImage().getScaledInstance(30, 30, Image.SCALE_SMOOTH));
                butSave.setIcon(imgIcon);
                toolBar.add(butSave);

                butSaveAs = new JButton();
                imgIcon = new ImageIcon("img/save_as.png");
                imgIcon = new ImageIcon(
                                imgIcon.getImage().getScaledInstance(30, 30, Image.SCALE_SMOOTH));
                butSaveAs.setIcon(imgIcon);
                toolBar.add(butSaveAs);

                toolBar.addSeparator(new Dimension(20, 0));

                butExportImage = new JButton();
                imgIcon = new ImageIcon("img/export_image.png");
                imgIcon = new ImageIcon(
                                imgIcon.getImage().getScaledInstance(30, 30, Image.SCALE_SMOOTH));
                butExportImage.setIcon(imgIcon);
                toolBar.add(butExportImage);

                butPrint = new JButton();
                imgIcon = new ImageIcon("img/print.png");
                imgIcon = new ImageIcon(
                                imgIcon.getImage().getScaledInstance(30, 30, Image.SCALE_SMOOTH));
                butPrint.setIcon(imgIcon);
                toolBar.add(butPrint);

                toolBar.addSeparator(new Dimension(20, 0));

                butFx = new JButton();
                imgIcon = new ImageIcon("img/fx.png");
                imgIcon = new ImageIcon(
                                imgIcon.getImage().getScaledInstance(30, 30, Image.SCALE_SMOOTH));
                butFx.setIcon(imgIcon);
                toolBar.add(butFx);

                butTable = new JButton();
                imgIcon = new ImageIcon("img/table.png");
                imgIcon = new ImageIcon(
                                imgIcon.getImage().getScaledInstance(30, 30, Image.SCALE_SMOOTH));
                butTable.setIcon(imgIcon);
                toolBar.add(butTable);

        }

}
