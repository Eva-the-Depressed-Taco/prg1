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
		self._textBox2 = System.Windows.Forms.TextBox()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._label12 = System.Windows.Forms.Label()
		self._label13 = System.Windows.Forms.Label()
		self._label14 = System.Windows.Forms.Label()
		self._label15 = System.Windows.Forms.Label()
		self._label16 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.White
		self._button1.Location = System.Drawing.Point(32, 85)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 0
		self._button1.Text = "calc"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(21, 32)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 1
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(138, 32)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 2
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(148, 85)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 3
		self._button2.Text = "clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(90, 56)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 4
		self._button3.Text = "off"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self._label1.Location = System.Drawing.Point(32, 126)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 5
		self._label1.Text = " sum"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self._label2.Location = System.Drawing.Point(32, 275)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 6
		self._label2.Text = " "
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self._label3.Location = System.Drawing.Point(32, 169)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 7
		self._label3.Text = " diffrence"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self._label4.Location = System.Drawing.Point(32, 318)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 8
		self._label4.Text = " "
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self._label5.Location = System.Drawing.Point(32, 205)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 9
		self._label5.Text = " product"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self._label6.Location = System.Drawing.Point(32, 363)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 23)
		self._label6.TabIndex = 10
		self._label6.Text = " "
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self._label7.Location = System.Drawing.Point(32, 237)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(100, 23)
		self._label7.TabIndex = 11
		self._label7.Text = " ave"
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self._label8.Location = System.Drawing.Point(32, 401)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(100, 23)
		self._label8.TabIndex = 12
		self._label8.Text = " "
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self._label9.Location = System.Drawing.Point(148, 401)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(100, 23)
		self._label9.TabIndex = 20
		self._label9.Text = " "
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self._label10.Location = System.Drawing.Point(148, 237)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(100, 23)
		self._label10.TabIndex = 19
		self._label10.Text = " "
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self._label11.Location = System.Drawing.Point(148, 363)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(100, 23)
		self._label11.TabIndex = 18
		self._label11.Text = " "
		# 
		# label12
		# 
		self._label12.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self._label12.Location = System.Drawing.Point(148, 205)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(100, 23)
		self._label12.TabIndex = 17
		self._label12.Text = " "
		# 
		# label13
		# 
		self._label13.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self._label13.Location = System.Drawing.Point(148, 318)
		self._label13.Name = "label13"
		self._label13.Size = System.Drawing.Size(100, 23)
		self._label13.TabIndex = 16
		self._label13.Text = " "
		# 
		# label14
		# 
		self._label14.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self._label14.Location = System.Drawing.Point(148, 169)
		self._label14.Name = "label14"
		self._label14.Size = System.Drawing.Size(100, 23)
		self._label14.TabIndex = 15
		self._label14.Text = " "
		# 
		# label15
		# 
		self._label15.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self._label15.Location = System.Drawing.Point(148, 275)
		self._label15.Name = "label15"
		self._label15.Size = System.Drawing.Size(100, 23)
		self._label15.TabIndex = 14
		self._label15.Text = " "
		# 
		# label16
		# 
		self._label16.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self._label16.Location = System.Drawing.Point(148, 126)
		self._label16.Name = "label16"
		self._label16.Size = System.Drawing.Size(100, 23)
		self._label16.TabIndex = 13
		self._label16.Text = " "
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(272, 436)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label12)
		self.Controls.Add(self._label13)
		self.Controls.Add(self._label14)
		self.Controls.Add(self._label15)
		self.Controls.Add(self._label16)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "mini calc"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)
		self.PerformLayout()


	def MainFormLoad(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		num1 = int(self._textBox1.text)
		num2 = int(self._textBox2.text)
		Sum = num1 + num2
		diff = num1 - num2
		Absdiff = abs(Diif)
		Max = 0
		Min = 0
		if num1 >= num2:
			Max = num1
		else: 
			Max = num2
		if max == num1: 
			Min = num2
		else:
			Min = num1
		self._label14.Text = str(Max)
		self._label16.Text = str(Min)
			

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""

	def Button3Click(self, sender, e):
		Applicition.Exit()