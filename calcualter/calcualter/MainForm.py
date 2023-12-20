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
		self._label1 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._button4 = System.Windows.Forms.Button()
		self._button5 = System.Windows.Forms.Button()
		self._label2 = System.Windows.Forms.Label()
		self._button6 = System.Windows.Forms.Button()
		self._button7 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(52, 28)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 0
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(52, 85)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 1
		# 
		# label1
		# 
		self._label1.Location = System.Drawing.Point(52, 57)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 2
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(177, 24)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(31, 23)
		self._button1.TabIndex = 3
		self._button1.Text = "+"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(191, 110)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(31, 23)
		self._button2.TabIndex = 4
		self._button2.Text = "="
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(214, 52)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(31, 23)
		self._button3.TabIndex = 5
		self._button3.Text = "-/-"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# button4
		# 
		self._button4.Location = System.Drawing.Point(177, 52)
		self._button4.Name = "button4"
		self._button4.Size = System.Drawing.Size(31, 23)
		self._button4.TabIndex = 6
		self._button4.Text = "X"
		self._button4.UseVisualStyleBackColor = True
		self._button4.Click += self.Button4Click
		# 
		# button5
		# 
		self._button5.Location = System.Drawing.Point(214, 24)
		self._button5.Name = "button5"
		self._button5.Size = System.Drawing.Size(31, 23)
		self._button5.TabIndex = 7
		self._button5.Text = "-"
		self._button5.UseVisualStyleBackColor = True
		self._button5.Click += self.Button5Click
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Lavender
		self._label2.Location = System.Drawing.Point(52, 125)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 8
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label2.Click += self.Label2Click
		# 
		# button6
		# 
		self._button6.Location = System.Drawing.Point(177, 81)
		self._button6.Name = "button6"
		self._button6.Size = System.Drawing.Size(31, 23)
		self._button6.TabIndex = 9
		self._button6.Text = "^"
		self._button6.UseVisualStyleBackColor = True
		self._button6.Click += self.Button6Click
		# 
		# button7
		# 
		self._button7.Location = System.Drawing.Point(214, 81)
		self._button7.Name = "button7"
		self._button7.Size = System.Drawing.Size(31, 23)
		self._button7.TabIndex = 10
		self._button7.Text = "//"
		self._button7.UseVisualStyleBackColor = True
		self._button7.Click += self.Button7Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.MediumPurple
		self.ClientSize = System.Drawing.Size(284, 261)
		self.Controls.Add(self._button7)
		self.Controls.Add(self._button6)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._button5)
		self.Controls.Add(self._button4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "calcualter"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		#num1 = str(self._textBox1.Text)
		#num2 = str(self._textBox2.Text)
		#answer1 = num1 + num2
		self._label1.Text = "+"
		#self._label2.Text = answer1
	def Label2Click(self, sender, e):
		pass

	def Button2Click(self, sender, e):
		num1 = float(self._textBox1.Text)
		num2 = float(self._textBox2.Text)
		if self._label1.Text == "+":
			answer = num1 + num2
		if self._label1.Text == "-":
			answer = num1 - num2
		if self._label1.Text == "X":
			answer = num1 * num2
		if self._label1.Text == "-/-":
			answer = num1 / num2
		if self._label1.Text == "^":
			answer = num1 ** num2
		if self._label1.Text == "//":
			answer = num1 // num2
		self._label2.Text = str(answer)

	def Button5Click(self, sender, e):
		self._label1.Text = "-"

	def Button4Click(self, sender, e):
		self._label1.Text = "X"

	def Button3Click(self, sender, e):
		self._label1.Text = "-/-"

	def Button6Click(self, sender, e):
		self._label1.Text = "^"

	def Button7Click(self, sender, e):
		self._label1.Text = "//"