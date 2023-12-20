import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._components = System.ComponentModel.Container()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._button4 = System.Windows.Forms.Button()
		self._button5 = System.Windows.Forms.Button()
		self._button6 = System.Windows.Forms.Button()
		self._button7 = System.Windows.Forms.Button()
		self._timer1 = System.Windows.Forms.Timer(self._components)
		self._timer2 = System.Windows.Forms.Timer(self._components)
		self._timer3 = System.Windows.Forms.Timer(self._components)
		self._timer4 = System.Windows.Forms.Timer(self._components)
		self._timer5 = System.Windows.Forms.Timer(self._components)
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(22, 38)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(89, 90)
		self._button1.TabIndex = 0
		self._button1.Text = "button1"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(455, 158)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(89, 90)
		self._button2.TabIndex = 1
		self._button2.Text = "button2"
		self._button2.UseVisualStyleBackColor = True
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(650, 243)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(28, 25)
		self._button3.TabIndex = 2
		self._button3.Text = "button3"
		self._button3.UseVisualStyleBackColor = True
		# 
		# button4
		# 
		self._button4.Location = System.Drawing.Point(235, 188)
		self._button4.Name = "button4"
		self._button4.Size = System.Drawing.Size(29, 31)
		self._button4.TabIndex = 3
		self._button4.Text = "button4"
		self._button4.UseVisualStyleBackColor = True
		self._button4.Click += self.Button4Click
		# 
		# button5
		# 
		self._button5.Location = System.Drawing.Point(733, 47)
		self._button5.Name = "button5"
		self._button5.Size = System.Drawing.Size(89, 90)
		self._button5.TabIndex = 4
		self._button5.Text = "button5"
		self._button5.UseVisualStyleBackColor = True
		# 
		# button6
		# 
		self._button6.Location = System.Drawing.Point(343, 25)
		self._button6.Name = "button6"
		self._button6.Size = System.Drawing.Size(89, 90)
		self._button6.TabIndex = 5
		self._button6.Text = "button6"
		self._button6.UseVisualStyleBackColor = True
		# 
		# button7
		# 
		self._button7.Location = System.Drawing.Point(788, 178)
		self._button7.Name = "button7"
		self._button7.Size = System.Drawing.Size(89, 90)
		self._button7.TabIndex = 6
		self._button7.Text = "button7"
		self._button7.UseVisualStyleBackColor = True
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(22, 330)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(38, 23)
		self._label1.TabIndex = 7
		self._label1.Text = "score"
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(83, 329)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 8
		self._label2.Text = "0"
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(904, 377)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button7)
		self.Controls.Add(self._button6)
		self.Controls.Add(self._button5)
		self.Controls.Add(self._button4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "game"
		self.ResumeLayout(False)


	def Button4Click(self, sender, e):
		self._label2.Text = "0"

	def Button1Click(self, sender, e):
		str(self.label2.Text) + 1