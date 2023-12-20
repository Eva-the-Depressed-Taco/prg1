import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._radioButton1 = System.Windows.Forms.RadioButton()
		self._radioButton2 = System.Windows.Forms.RadioButton()
		self._radioButton3 = System.Windows.Forms.RadioButton()
		self._checkBox1 = System.Windows.Forms.CheckBox()
		self._checkBox2 = System.Windows.Forms.CheckBox()
		self._checkBox3 = System.Windows.Forms.CheckBox()
		self._button1 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# radioButton1
		# 
		self._radioButton1.Location = System.Drawing.Point(13, 23)
		self._radioButton1.Name = "radioButton1"
		self._radioButton1.Size = System.Drawing.Size(75, 24)
		self._radioButton1.TabIndex = 0
		self._radioButton1.TabStop = True
		self._radioButton1.Text = "choice1"
		self._radioButton1.UseVisualStyleBackColor = True
		# 
		# radioButton2
		# 
		self._radioButton2.Location = System.Drawing.Point(12, 78)
		self._radioButton2.Name = "radioButton2"
		self._radioButton2.Size = System.Drawing.Size(76, 24)
		self._radioButton2.TabIndex = 1
		self._radioButton2.TabStop = True
		self._radioButton2.Text = "choice3"
		self._radioButton2.UseVisualStyleBackColor = True
		# 
		# radioButton3
		# 
		self._radioButton3.Location = System.Drawing.Point(13, 53)
		self._radioButton3.Name = "radioButton3"
		self._radioButton3.Size = System.Drawing.Size(75, 19)
		self._radioButton3.TabIndex = 2
		self._radioButton3.TabStop = True
		self._radioButton3.Text = "choice2"
		self._radioButton3.UseVisualStyleBackColor = True
		# 
		# checkBox1
		# 
		self._checkBox1.Location = System.Drawing.Point(118, 23)
		self._checkBox1.Name = "checkBox1"
		self._checkBox1.Size = System.Drawing.Size(104, 24)
		self._checkBox1.TabIndex = 3
		self._checkBox1.Text = "choice 4"
		self._checkBox1.UseVisualStyleBackColor = True
		# 
		# checkBox2
		# 
		self._checkBox2.Location = System.Drawing.Point(118, 78)
		self._checkBox2.Name = "checkBox2"
		self._checkBox2.Size = System.Drawing.Size(104, 24)
		self._checkBox2.TabIndex = 4
		self._checkBox2.Text = "choice 6"
		self._checkBox2.UseVisualStyleBackColor = True
		self._checkBox2.CheckedChanged += self.CheckBox2CheckedChanged
		# 
		# checkBox3
		# 
		self._checkBox3.Location = System.Drawing.Point(118, 48)
		self._checkBox3.Name = "checkBox3"
		self._checkBox3.Size = System.Drawing.Size(104, 24)
		self._checkBox3.TabIndex = 5
		self._checkBox3.Text = "choice 5"
		self._checkBox3.UseVisualStyleBackColor = True
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(12, 108)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(103, 23)
		self._button1.TabIndex = 6
		self._button1.Text = "reveal answers"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.FromArgb(220, 182, 230)
		self._label1.Location = System.Drawing.Point(28, 165)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(203, 70)
		self._label1.TabIndex = 7
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.FromArgb(255, 192, 255)
		self.ClientSize = System.Drawing.Size(284, 261)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._checkBox3)
		self.Controls.Add(self._checkBox2)
		self.Controls.Add(self._checkBox1)
		self.Controls.Add(self._radioButton3)
		self.Controls.Add(self._radioButton2)
		self.Controls.Add(self._radioButton1)
		self.Name = "MainForm"
		self.Text = "choices"
		self.ResumeLayout(False)


	def CheckBox2CheckedChanged(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		if self._radioButton1.Checked == True:
			strMessage = "You selected Choice 1"
		elif self._radioButton2. Checked == True:
			strMessage = "You selected Choice 2"
		elif self._radioButton3. Checked == True:
			strMessage = "You selected Choice 3"
		if self._checkBox1. Checked == True:
			strMessage += " and choice 4"
		if self._checkBox2. Checked == True:
			strMessage += " and choice 5"
		if self._checkBox3. Checked == True:
			strMessage += " and choice 6"
			
		self._label1.Text = str(strMessage)