class StyleWidget:
    def __init__(self, type_font):
        self.__font_family = type_font

    def styleDialog(self, color):
        style = "QDialog {background-color:" + str(color) + "; color: white;}"
        return style

    def styleMainWindow(self, color):
        style = "QMainWindow {background-color:" + str(color) + "; color: white;}"
        return style
    
    def styleMenu(self, color_bck, color_for):
        style = "QMenu {background-color:" + str(color_bck) + "; color:" + str(color_for)+ ";}"
        style += " QMenu:hover{ background-color: "+ str(color_for)+ ";"+ "color: "+ str(color_bck)+ ";}"
        return style
    
    def styleBar(self, color, color_for):
        style = "QMenuBar{background-color:" + str(color) + "; color:" + str(color_for) + ";}"
        style += " QMenu:MenuBar{ background-color: "+ str(color_for)+ ";"+ "color: "+ str(color)+ ";}"
        return style

    def styleLabel(self, name, color, color_hover, font_size, font_weight):
        style = (
            "#"
            + str(name)
            + " {color: "
            + str(color)
            + ";font-family:"
            + str(self.__font_family)
            + ";font-size:"
            + str(font_size)
            + "px;font-weight:"
            + str(font_weight)
            + "; }"
        )
        style += "#" + str(name) + ":hover { color: " + str(color_hover) + ";}"
        return style
    
    def styleLabelBorderHover(self,name,color, size_border):
        style = ("#" + str(name) + ":hover { border-radius: "+str(size_border)+"px; border: 2px solid "+ str(color) + ";}")
        return style

    def styleButton(
        self,
        name,
        color_back,
        color_fore,
        font_size,
        font_weight,
        size_border,
    ):
        style = (
            "#"
            + str(name)
            + " { background-color: "
            + str(color_back)
            + ";"
            + "color: "
            + str(color_fore)
            + ";font-family:"
            + str(self.__font_family)
            + ";font-size:"
            + str(font_size)
            + "px;font-weight:"
            + str(font_weight)
            + "; border-radius:"
            + str(size_border)
            + "px"
            + "; border: 2px solid "
            + str(color_fore)
            + "; }"
        )
        style += (
            "#"
            + str(name)
            + ":hover { background-color: "
            + str(color_fore)
            + ";"
            + "color: "
            + str(color_back)
            + "; border: 2px solid "
            + str(color_back)
            + ";}"
        )

        return style

    def styleLine(self, name, font_size):
        style = (
            "#"
            + str(name)
            + "{font-family:"
            + str(self.__font_family)
            + ";font-size: "
            + str(font_size)
            + "px;"
            + "color: #351C75; border-radius: 12px; border: 1px solid green;}"
        )
        return style
    
    def styleTexPlain(self, name, font_size):
        style = (
            "#"
            + str(name)
            + "{font-family:"
            + str(self.__font_family)
            + ";font-size: "
            + str(font_size)
            + "px;"
            + "; background-color: white; color: #351C75; border-radius: 16px; border: 2px solid green;}"
        )
        return style
    

    def styleCheckBox(self, name, font_size, color):
        style = (
            "#"
            + str(name)
            + "{font-family:"
            + str(self.__font_family)
            + ";font-size: "
            + str(font_size)
            + "px;"
            + "color : "+ str(color)+";}"
        )

        return style

    def styleTable(self, name, font_size, color_for, color_back):
        style = (
            "#"
            + str(name)
            + "{font-family:"
            + str(self.__font_family)
            + ";font-size: "
            + str(font_size)
            + "px;"
            + "alternate-background-color:" + str(color_for)
            + "; background :" + str(color_back)
            + "; border-radius: 12px; border: 2px solid #351C75;}"
        )

        return style

    
