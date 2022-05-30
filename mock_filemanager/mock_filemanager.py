import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

import os

CSS = b"""
@keyframes animated-highlight {
  from { box-shadow: inset 0px 0px 4px  @theme_selected_bg_color; }
  to   { box-shadow: inset 0px 0px 8px @theme_selected_bg_color; }
}

.highlighted {
  animation: animated-highlight 1s infinite alternate;
}

.background {
    background-color: white;
}
"""

@Gtk.Template(filename=os.path.join(os.path.dirname(__file__), "mock_filemanager.ui"))
class NautilusMock(Gtk.Window):
    """
    Mock application simulating the nautilus filemanager. The purpose is to
    guide the user to right-click on an image and "Copy To Other AppVM...".
    """
    __gtype_name__ = "NautilusMock"
    picture = Gtk.Template.Child()
    rightclickmenu = Gtk.Template.Child()
    copy_to_appvm = Gtk.Template.Child()

    # file manager fragments
    work_picture_top     = Gtk.Template.Child()
    work_picture_middle  = Gtk.Template.Child()
    work_picture_picture = Gtk.Template.Child()
    work_picture_bottom  = Gtk.Template.Child()

    def __init__(self):
        super().__init__()
        self.set_style()
        self.present()
        self.fix_image_relative_imports()

    @Gtk.Template.Callback()
    def on_click_picture(self, widget, event):
        if event.button == 3: # right click
            self.rightclickmenu.popup_at_pointer()

    def set_style(self):
        style_provider = Gtk.CssProvider()
        style_provider.load_from_data(CSS)

        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )

    def fix_image_relative_imports(self):
        """
        Fixes the image locations when the program is being ran from another
        palce than the developement environment.
        """
        install_path = os.path.dirname(__file__)
        self.work_picture_top.set_from_file(
            os.path.join(install_path, "images", "work_picture_top.png"))
        self.work_picture_middle.set_from_file(
            os.path.join(install_path, "images", "work_picture_middle.png"))
        self.work_picture_picture.set_from_file(
            os.path.join(install_path, "images", "work_picture_picture.png"))
        self.work_picture_bottom.set_from_file(
            os.path.join(install_path, "images", "work_picture_bottom.png"))

    @Gtk.Template.Callback()
    def on_show_menu(self, *args, **kwargs):
        print("activate menu")
        self.picture.get_style_context().remove_class("highlighted")

    @Gtk.Template.Callback()
    def on_hide_menu(self, *args, **kwargs):
        print("deactivate menu")
        self.picture.get_style_context().add_class("highlighted")

    @Gtk.Template.Callback()
    def on_copy_to_appvm(self, *args, **kwargs):
        print("clicked right option")
        self.picture.get_style_context().remove_class("highlighted")

def main():
    NautilusMock()
    Gtk.main()

if __name__ == "__main__":
    main()