﻿import System.Drawing
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
		self._textBox4 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(41, 31)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 0
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(41, 58)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 1
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(41, 85)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 20)
		self._textBox3.TabIndex = 2
		# 
		# textBox4
		# 
		self._textBox4.Location = System.Drawing.Point(41, 112)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(100, 20)
		self._textBox4.TabIndex = 3
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(41, 148)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 4
		self._button1.Text = "button1"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.MediumOrchid
		self._label1.ForeColor = System.Drawing.SystemColors.ButtonFace
		self._label1.Location = System.Drawing.Point(41, 237)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 5
		self._label1.Text = "ave"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.MediumOrchid
		self._label2.ForeColor = System.Drawing.SystemColors.ControlLightLight
		self._label2.Location = System.Drawing.Point(171, 237)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 6
		self._label2.Text = "sum"
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self.ClientSize = System.Drawing.Size(601, 449)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox4)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "Ave"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		num3 = int(self._textBox3.Text)
		num4 = int(self._textBox4.Text)
		sum = num1 + num2 + num3 + num4
		ave = (num1 + num2 + num3 + num4) / 4
		self._label2.Text = str(ave)
		self._label1.Text = str(sum)
		
				