import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(106, 54)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 0
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.FromArgb(255, 128, 255)
		self._button1.Location = System.Drawing.Point(119, 80)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 1
		self._button1.Text = "calcualte"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.PaleVioletRed
		self._label1.Location = System.Drawing.Point(24, 128)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 2
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(106, 13)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 4
		# 
		# label2
		# 
		self._label2.Location = System.Drawing.Point(12, 13)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(88, 23)
		self._label2.TabIndex = 5
		self._label2.Text = "speed limit"
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(12, 51)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(88, 23)
		self._label3.TabIndex = 6
		self._label3.Text = "speed"
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self.ClientSize = System.Drawing.Size(284, 261)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "fuzz"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		speedlimit = int(self._textBox2.Text)
		speed = int(self._textBox1.Text)
		over = speed - speedlimit
		fine = (over * 5)+ 20
		self._label1.Text = str(fine)
		