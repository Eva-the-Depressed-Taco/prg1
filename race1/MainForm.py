import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._textBox4 = System.Windows.Forms.TextBox()
		self._textBox5 = System.Windows.Forms.TextBox()
		self._textBox6 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.LightSkyBlue
		self._label1.Location = System.Drawing.Point(148, 177)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 23)
		self._label1.TabIndex = 0
		self._label1.Text = " "
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.LightSkyBlue
		self._label2.Location = System.Drawing.Point(148, 213)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 23)
		self._label2.TabIndex = 1
		self._label2.Text = " "
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.LightSkyBlue
		self._label3.Location = System.Drawing.Point(148, 248)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 23)
		self._label3.TabIndex = 2
		self._label3.Text = " "
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.Location = System.Drawing.Point(62, 33)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 20)
		self._textBox1.TabIndex = 3
		# 
		# textBox2
		# 
		self._textBox2.Location = System.Drawing.Point(62, 59)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 20)
		self._textBox2.TabIndex = 4
		# 
		# textBox3
		# 
		self._textBox3.Location = System.Drawing.Point(62, 85)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 20)
		self._textBox3.TabIndex = 5
		# 
		# textBox4
		# 
		self._textBox4.Location = System.Drawing.Point(216, 33)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(100, 20)
		self._textBox4.TabIndex = 6
		# 
		# textBox5
		# 
		self._textBox5.Location = System.Drawing.Point(216, 59)
		self._textBox5.Name = "textBox5"
		self._textBox5.Size = System.Drawing.Size(100, 20)
		self._textBox5.TabIndex = 7
		# 
		# textBox6
		# 
		self._textBox6.Location = System.Drawing.Point(216, 85)
		self._textBox6.Name = "textBox6"
		self._textBox6.Size = System.Drawing.Size(100, 20)
		self._textBox6.TabIndex = 8
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(62, 132)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(89, 23)
		self._button1.TabIndex = 9
		self._button1.Text = "CALCUALTE"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(202, 132)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(89, 23)
		self._button2.TabIndex = 10
		self._button2.Text = "CLEAR TIMES"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self.ClientSize = System.Drawing.Size(553, 312)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox6)
		self.Controls.Add(self._textBox5)
		self.Controls.Add(self._textBox4)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "race1"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		n1 = str(self._textBox1.Text)
		n2 = str(self._textBox2.Text)
		n3 = str(self._textBox3.Text)
		n1T = str(self._textBox4.Text)
		n2T = str(self._textBox5.Text)
		n3T = str(self._textBox6.Text)
		if n1T < n2T < n3T:
			self._label1.Text = str(n1)
			self._label2.Text = str(n2)
			self._label3.Text = str(n3)
		if n1T > n2T > n3T:
			self._label1.Text = str(n3)
			self._label2.Text = str(n2)
			self._label3.Text = str(n1)
		if n1T < n3T < n2T:
			self._label1.Text = str(n1)
			self._label2.Text = str(n3)
			self._label3.Text = str(n2)
		if n2T < n3T < n1T:
			self._label1.Text = str(n2)
			self._label2.Text = str(n3)
			self._label3.Text = str(n1)
		if n3T < n2T < n1T:
			self._label1.Text = str(n3)
			self._label2.Text = str(n2)
			self._label3.Text = str(n1)
		if n2T < n1T < n3T:
			self._label1.Text = str(n2)
			self._label2.Text = str(n1)
			self._label3.Text = str(n3)
		
			
			
			

	def Button2Click(self, sender, e):
		self._textBox4.Text = ""
		self._textBox5.Text = ""
		self._textBox6.Text = ""