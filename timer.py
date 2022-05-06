from kivy.app import App
from kivy.clock import Clock
from datetime import datetime

# from sound import Play

class Alarm(App):
    def __init__(self, alarm_time, **kwargs):
        super(Alarm, self).__init__(**kwargs)
        self.alarm_time = alarm_time

    # turn on alarm
    def clock_start(self):  # on_start는 무조건 build시 시작
        self.tick = Clock.schedule_interval(self.update, 1)
        print("start_timer")

    # ticktock every 1 second
    def update(self,dt):
        self.now = datetime.now().time()
        print(self.now)

        # beep & alarm at beep_time
        if self.alarm_time:
            if self.now >= self.alarm_time:
                self.alarm()
                self.tick.cancel()

    # print alarm
    def alarm(self):
        print("Alarm!")
        # Play().beep()