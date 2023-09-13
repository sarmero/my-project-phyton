import javax.swing.UIManager;

import view.MainWindowView;

public class App {
    public static void main(String[] args) throws Exception {

       // UIManager.setLookAndFeel("com.sun.java.swing.plaf.windows.WindowsLookAndFeel");

        // dialogo abrir archivo
        UIManager.put("FileChooser.openDialogTitleText", "Seleccionar archivo");
        UIManager.put("FileChooser.luckInLabelText", "Buscar en");
        UIManager.put("FileChooser.openButtonText", "Abrir");
        UIManager.put("FileChooser.openButtonToolTipText", "Abrir archivo seleccionado");

        // dialogo guardar archivo
        UIManager.put("FileChooser.saveDialogTitleText", "Guardar como");
        UIManager.put("FileChooser.saveInLabelText", "Guardar en");
        UIManager.put("FileChooser.saveButtonText", "Guardar");
        UIManager.put("FileChooser.saveButtonToolTipText", "Guardar Archivo Seleccionado");

        // dialogo abrir y guardad
        UIManager.put("FileChooser.cancelButtonText", "Cancelar");
        UIManager.put("FileChooser.cancelButtonToolTipText", "Cerrar el dialogo");
        UIManager.put("FileChooser.fileNameLabelText", "Nombre del archivo");
        UIManager.put("FileChooser.filesOfTypeLabelText", "Tipo de archivo");
        UIManager.put("FileChooser.acceptAllFileFilterText", "Todos los archivos");

        // mensaje de advertencia
        UIManager.put("OptionPane.yesButtonText", "Si");
        UIManager.put("OptionPane.noButtonText", "No");
        UIManager.put("OptionPane.okButtonText", "Aceptar");
        UIManager.put("OptionPane.cancelButtonText", "Cancelar");

        MainWindowView window;
        window = new MainWindowView();
        window.initWindow();
    }
}
