import System.Drawing
import System.Windows.Forms
import math
from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._listBox1 = System.Windows.Forms.ListBox()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Pink
		self._button1.Location = System.Drawing.Point(678, 23)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(75, 23)
		self._button1.TabIndex = 1
		self._button1.Text = "calcualte"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Pink
		self._button2.Location = System.Drawing.Point(678, 76)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(75, 23)
		self._button2.TabIndex = 2
		self._button2.Text = "clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Pink
		self._button3.Location = System.Drawing.Point(678, 138)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(75, 23)
		self._button3.TabIndex = 3
		self._button3.Text = "exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.Color.Pink
		self._listBox1.ForeColor = System.Drawing.Color.Purple
		self._listBox1.FormattingEnabled = True
		self._listBox1.Location = System.Drawing.Point(26, 23)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(612, 407)
		self._listBox1.TabIndex = 4
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Plum
		self.ClientSize = System.Drawing.Size(961, 456)
		self.Controls.Add(self._listBox1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "prognumberidk"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		header = "Number\t\tSquare\t\tSquare Root"
		self._listBox1.Items.Add(header)
		for num in range(1, 50+1):
			numsqrd = num**2
			numsqrt = math.sqrt(num)
			msg = str(num) + "\t\t" + str(numsqrd) + \
					"\t\t" + str(round(numsqrt, 4))
			self._listBox1.Items.Add(msg)

	def Button3Click(self, sender, e):
		Application.Exit()

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()