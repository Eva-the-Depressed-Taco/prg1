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
		self._button1 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(13, 34)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 0
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(151, 33)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 1
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Plum
		self._label1.Location = System.Drawing.Point(13, 77)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 2
		self._label1.Text = "sum"
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Plum
		self._label2.Location = System.Drawing.Point(13, 281)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 3
		self._label2.Text = "min"
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Plum
		self._label3.Location = System.Drawing.Point(12, 314)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 4
		self._label3.Text = "max"
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Plum
		self._label4.Location = System.Drawing.Point(12, 246)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 23)
		self._label4.TabIndex = 5
		self._label4.Text = "abs diff"
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Plum
		self._label5.Location = System.Drawing.Point(13, 161)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 23)
		self._label5.TabIndex = 6
		self._label5.Text = "product"
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.Plum
		self._label6.Location = System.Drawing.Point(12, 204)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 23)
		self._label6.TabIndex = 7
		self._label6.Text = "ave"
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.Plum
		self._label7.Location = System.Drawing.Point(13, 117)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(100, 23)
		self._label7.TabIndex = 8
		self._label7.Text = "diffrence"
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.Plum
		self._label8.Location = System.Drawing.Point(138, 117)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(100, 23)
		self._label8.TabIndex = 15
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.Plum
		self._label9.Location = System.Drawing.Point(137, 204)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(100, 23)
		self._label9.TabIndex = 14
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.Plum
		self._label10.Location = System.Drawing.Point(138, 161)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(100, 23)
		self._label10.TabIndex = 13
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.Plum
		self._label11.Location = System.Drawing.Point(137, 246)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(100, 23)
		self._label11.TabIndex = 12
		# 
		# label12
		# 
		self._label12.BackColor = System.Drawing.Color.Plum
		self._label12.Location = System.Drawing.Point(137, 314)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(100, 23)
		self._label12.TabIndex = 11
		# 
		# label13
		# 
		self._label13.BackColor = System.Drawing.Color.Plum
		self._label13.Location = System.Drawing.Point(138, 281)
		self._label13.Name = "label13"
		self._label13.Size = System.Drawing.Size(100, 23)
		self._label13.TabIndex = 10
		# 
		# label14
		# 
		self._label14.BackColor = System.Drawing.Color.Plum
		self._label14.Location = System.Drawing.Point(138, 77)
		self._label14.Name = "label14"
		self._label14.Size = System.Drawing.Size(100, 23)
		self._label14.TabIndex = 9
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(278, 77)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 16
		self._button1.Text = "calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(64, 0, 64)
		self.ClientSize = System.Drawing.Size(384, 454)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label12)
		self.Controls.Add(self._label13)
		self.Controls.Add(self._label14)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "minicalc2"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		Sum = num1 + num2
		Diff = num2 - num1
		AbsDiff = abs(Diff)
		max = 0
		Min = 0
		if num1 >= num2:
			Max = num1
		else:
			Max = num2
		if Max == num1:
			Min = num2
		else:
			Min = num1
			
		Product = num1 * num2
		Ave = (num1 + num2)/2
		self._label14.Text = str(Sum)
		self._label8.Text = str(Diff)
		self._label10.Text = str(Product)
		self._label9.Text = str(Ave)
		self._label11.Text = str(AbsDiff)
		self._label13.Text = str(Min)
		self._label12.Text = str(Max)
		