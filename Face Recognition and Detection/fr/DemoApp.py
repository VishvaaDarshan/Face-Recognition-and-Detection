from kivy.app import App
from kivy.properties import StringProperty
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import requests
import threading

Builder.load_string('''
<HomeView>:
    orientation: 'vertical'
    Label:
    	id: countValue
    	text_size: root.width, None
    	text: root.countValue
    Button:
        text: 'Send Request'
        size_hint_y: None
        on_press: root.count()
''')

class HomeView(BoxLayout):
	countnum = 0
	countValue = StringProperty("Click to Start")

	def requestThread(self):
		self.countValue = str(requests.get("https://google.com").text)

	def count(self):
		self.countnum += 1
		# self.countValue = "You Clicked the button "+str(self.countnum)+ " many times"
		self.countValue = "Requesting...."
		threading.Thread(target=self.requestThread).start()

class HelloApp(App):
	def build(self):
		return HomeView()

if __name__ == "__main__":
	HelloApp().run()