import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._panel1 = System.Windows.Forms.Panel()
		self._panel1.SuspendLayout()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(117, 82)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 0
		self._button1.Text = "calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(198, 84)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 1
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.White
		self._label1.Location = System.Drawing.Point(161, 50)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(113, 28)
		self._label1.TabIndex = 2
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.White
		self._label2.Location = System.Drawing.Point(161, 135)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(113, 28)
		self._label2.TabIndex = 3
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.White
		self._label3.Location = System.Drawing.Point(161, 92)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(113, 28)
		self._label3.TabIndex = 4
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.White
		self._label4.Location = System.Drawing.Point(161, 5)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(113, 28)
		self._label4.TabIndex = 5
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.White
		self._label5.Location = System.Drawing.Point(161, 180)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(113, 28)
		self._label5.TabIndex = 6
		# 
		# panel1
		# 
		self._panel1.BackColor = System.Drawing.Color.Violet
		self._panel1.Controls.Add(self._label4)
		self._panel1.Controls.Add(self._label5)
		self._panel1.Controls.Add(self._label1)
		self._panel1.Controls.Add(self._label2)
		self._panel1.Controls.Add(self._label3)
		self._panel1.Location = System.Drawing.Point(491, 82)
		self._panel1.Name = "panel1"
		self._panel1.Size = System.Drawing.Size(302, 230)
		self._panel1.TabIndex = 7
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.MediumPurple
		self.ClientSize = System.Drawing.Size(831, 431)
		self.Controls.Add(self._panel1)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "zap"
		self.Load += self.MainFormLoad
		self._panel1.ResumeLayout(False)
		self.ResumeLayout(False)
		self.PerformLayout()


	def MainFormLoad(self, sender, e):
	
	def Button1Click(self, sender, e):
		zaps = int(self._textBox1.Text)
		bill = zaps * 0.0475
		cityt = bill * 0.03
		scharge = bill * 0.10
		total = bill + cityt + scharge
		latef = total *1.04
		self._label1.Text = str(bill)