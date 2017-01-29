from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

import os


class LoadDialog(FloatLayout):
	load = ObjectProperty(None)
	input_file_path = ObjectProperty(None)
	output_file_path = ObjectProperty(None)
	cancel = ObjectProperty(None)


class SaveDialog(FloatLayout):
	save = ObjectProperty(None)
	decrypt_file_path = ObjectProperty(None)
	cancel = ObjectProperty(None)


class Root(FloatLayout):
	loadfile = ObjectProperty(None)
	savefile = ObjectProperty(None)
	input_file_path = ObjectProperty(None)
	output_file_path = ObjectProperty(None)
	decrypt_file_path = ObjectProperty(None)
	inorout = 'n'


	def dismiss_popup(self):
		self._popup.dismiss()

	def show_load(self, inout):
		self.inorout = inout
		content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
		self._popup = Popup(title="Load file", content=content,
							size_hint=(0.9, 0.9))
		self._popup.open()

	def show_save(self):
		content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
		self._popup = Popup(title="Save file", content=content,
							size_hint=(0.9, 0.9))
		self._popup.open()

	def load(self, path, filename):
		with open(os.path.join(path, filename[0])) as stream:
			#self.text_input.text = stream.read()
			print os.path.join(path, filename[0])
			if self.inorout == 'in':
				self.input_file_path.text = os.path.join(path, filename[0])
			if self.inorout == 'out':
				self.output_file_path.text = os.path.join(path, filename[0])
			if self.inorout == 'dec':
				self.decrypt_file_path.text = os.path.join(path, filename[0])

		self.dismiss_popup()

	def save(self, path, filename):
#        with open(os.path.join(path, filename), 'w') as stream:
#            stream.write(self.text_input.text)


		self.dismiss_popup()

	def cancel(self):
		self.dismiss_popup()

	def encrypt(self):
		print 'encrypting...'

	def decrypt(self):
		print 'decrypting...'

class Editor(App):
	pass


Factory.register('Root', cls=Root)
Factory.register('LoadDialog', cls=LoadDialog)
#Factory.register('LoadDialog', cls=LoadDialog)
#Factory.register('SaveDialog', cls=SaveDialog)


if __name__ == '__main__':
	Editor().run()