from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen

from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.picker import MDTimePicker

from datetime import datetime
from timer import Alarm

class MainApp(MDApp):

    # Main Screen -----------------------------------------------------
    def build(self):
        screen = Screen()
        self.alarm_time = None

        # button: open time picker
        button = MDRectangleFlatButton(text="Open Time Picker",
                                       pos_hint={'center_x':.5, 'center_y':.5},)
        button.bind(on_release=self.show_time_picker)
        screen.add_widget(button)

        # label: show the time
        self.label = MDLabel(text="Alarm : "+str(self.alarm_time),
                        pos_hint={'center_x':.8, 'center_y':.4},)
        screen.add_widget(self.label)

        return screen

    # Time Picker -----------------------------------------------------
    def show_time_picker(self, instance):
        time_dialog = MDTimePicker()
        time_dialog.set_time(self.chk_alarm_time())
        time_dialog.open()

        time_dialog.bind(on_save=self.set_time)

    # logic -----------------------------------------------------
    def chk_alarm_time(self):
        if self.alarm_time == None:
            set_time = datetime.strptime("00:00:00", "%H:%M:%S")
        else:
            set_time = self.alarm_time

        return set_time

    def set_time(self, instance, time):
        self.alarm_time = time
        self.label.text = "Alarm : "+str(self.alarm_time)

        # alarm ----------------------
        timer = Alarm(self.alarm_time)
        timer.clock_start()


if __name__ == '__main__':
    MainApp().run()