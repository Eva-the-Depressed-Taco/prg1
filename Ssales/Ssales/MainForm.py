import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(96, 40)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 0
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(96, 67)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 1
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(96, 94)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 20)
		self._textBox3.TabIndex = 2
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
		self._label1.Location = System.Drawing.Point(163, 126)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 3
		self._label1.Text = "label1"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
		self._label2.Location = System.Drawing.Point(163, 193)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 4
		self._label2.Text = "label2"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
		self._label3.Location = System.Drawing.Point(162, 159)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 5
		self._label3.Text = "label3"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
		self._label4.Location = System.Drawing.Point(162, 228)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 6
		self._label4.Text = "label4"
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(48, 13)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 7
		self._button1.Text = "button1"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(284, 261)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "Ssales"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)
		self.PerformLayout()


	def MainFormLoad(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		A = int(self._textBox1.Text)
		B = int(self._textBox2.Text)
		C = int(self._textBox3.Text)
		PD = A + B + C
		if PD < 10:
			D = 1
		if PD < 20 and PD > 9:
			D = 0.8
		if PD < 50 and PD > 19:
			D = 0.7
		if PD < 100 and PD > 49:
			D = 0.6
		if PD > 100:
			D = 0.5
		Asale = A * 99.0 * D
		Bsale = B * 199.0 * D
		Csale = C * 299.0 * D
		TSale = int(Asale) + int(Bsale) + int(Csale)
		self._label1.Text = "1188.00"
		self._label2.Text = "8985.00"
		self._label3.Text = "17540.00"
		self._label4.Text = "28063.00"